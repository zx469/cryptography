#!/usr/bin/env python3
# hash_chain.py
# 实现哈希链文件认证的根哈希计算（h0）
# 1KB 块(1024 字节) -> 十六进制表示，块按从最后一个开始计算哈希链
# 将块数据 + 上一步的哈希（以字节形式拼接）后计算 SHA256，得到下一步的哈希
# 最终得到的哈希即为根哈希 h0，输出为十六进制字符串

import sys
import binascii
from Crypto.Hash import SHA256  # 需要安装 pycryptodome

# 配置：块大小为 1KB（1024 字节），在十六进制表示中是 2048 字符
BYTES_PER_BLOCK = 1024
HEX_PER_BLOCK = BYTES_PER_BLOCK * 2  # 2048 个十六进制字符

def read_file_as_hex(filename: str) -> str:
    """
    读取文件，返回其内容的十六进制字符串表示（不带前缀）。
    """
    with open(filename, 'rb') as f:
        data = f.read()
    hex_str = binascii.hexlify(data).decode('ascii')
    return hex_str

def chunk_hex_str(hex_str: str, block_hex_len: int) -> list:
    """
    将十六进制字符串按 block_hex_len 长度切分成块列表。
    注意：若最后一块短于 block_hex_len，仍作为最后一个块处理。
    """
    blocks = []
    total_len = len(hex_str)
    for i in range(0, total_len, block_hex_len):
        blocks.append(hex_str[i:i + block_hex_len])
    return blocks

def compute_root_hash_from_hex_blocks(hex_blocks: list) -> str:
    """
    给定按十六进制块组成的列表，从最后一个块开始计算哈希链，
    每一步将当前块数据（十六进制字符串）拼接上一次的哈希结果的十六进制表示，
    作为字节输入，计算 SHA256，得到新的哈希结果的十六进制字符串，作为下一次迭代的 append。
    初始时 append 为空。
    返回最终的根哈希值 h0 的十六进制字符串（小写或大写由最终输出格式决定）。
    """
    append_hex = ""  # 初始时没有附加哈希值
    # 反向迭代：从最后一个块开始
    for block_hex in reversed(hex_blocks):
        # 将当前块数据（十六进制）与 append 连接，构成要哈希的字节串
        combined_hex = block_hex + append_hex
        # 将十六进制字符串转换为字节
        if len(combined_hex) % 2 != 0:
            # 保险：确保偶数长度
            combined_hex = "0" + combined_hex
        combined_bytes = binascii.unhexlify(combined_hex.encode('ascii'))
        # 计算 SHA256
        h = SHA256.new()
        h.update(combined_bytes)
        append_hex = h.digest().hex()  # 作为十六进制字符串，用于下一轮拼接
    return append_hex  # 即根哈希 h0 的十六进制表示

def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_chain.py <intro.mp4> <test.mp4>")
        sys.exit(1)

    intro_path, test_path = sys.argv[1], sys.argv[2]

    # 1) 读取 intro.mp4，转换为十六进制字符串
    intro_hex = read_file_as_hex(intro_path)
    # 2) 将数据按 1KB 块分割（十六进制下为 2048 字符）
    intro_blocks = chunk_hex_str(intro_hex, HEX_PER_BLOCK)

    # 3) 反转处理：从最后一个块开始向前计算哈希链
    h0_intro_hex = compute_root_hash_from_hex_blocks(intro_blocks)

    # 输出 intro.mp4 的哈希链根哈希值（保持你要求的大小写）
    # 你给出的 intro 的哈希值示例使用大写，因此输出同样的大写形式
    print(h0_intro_hex.upper())

    # 验证：对 test.mp4 也计算，输出以便对比
    test_hex = read_file_as_hex(test_path)
    test_blocks = chunk_hex_str(test_hex, HEX_PER_BLOCK)
    h0_test_hex = compute_root_hash_from_hex_blocks(test_blocks)
    print("Test.mp4 h0 (hex):", h0_test_hex)

if __name__ == "__main__":
    main()

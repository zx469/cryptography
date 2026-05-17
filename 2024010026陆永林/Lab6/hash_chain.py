#!/usr/bin/env python3
"""
Lab6: 基于哈希链的文件认证系统
实现哈希链构建逻辑，计算文件的根哈希值 h0
"""

import sys
from Crypto.Hash import SHA256

def compute_hash_chain_root(file_path):
    """
    计算文件的哈希链根哈希值 h0
    
    步骤：
    1. 以二进制模式读取文件
    2. 将数据转换为十六进制字符串
    3. 按每2048个十六进制字符（对应1024字节）分割成块
    4. 反转块列表（从最后一个块开始处理）
    5. 从最后一个块向前构建哈希链：
       - 初始哈希值为空
       - 当前块数据 + 上一个哈希结果 -> SHA256
    6. 返回最终的哈希值 h0
    """
    
    # 1. 以二进制模式读取文件
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # 2. 将二进制数据转换为十六进制字符串
    hex_data = data.hex()
    
    # 3. 按每2048个十六进制字符（1024字节）分块
    block_size_hex = 2048  # 1024 bytes = 2048 hex chars
    blocks = []
    for i in range(0, len(hex_data), block_size_hex):
        blocks.append(hex_data[i:i + block_size_hex])
    
    print(f"文件大小: {len(data)} 字节")
    print(f"块数量: {len(blocks)}")
    print(f"最后一个块大小: {len(blocks[-1]) // 2} 字节")
    
    # 4. 反转块列表（从最后一个块开始向前计算）
    reversed_blocks = blocks[::-1]
    
    # 5. 构建哈希链
    # 初始时，append 为空（对应最后一个块后面没有要追加的哈希值）
    current_hash = b''  # 作为 bytes 类型存储
    
    for i, block_hex in enumerate(reversed_blocks):
        # 将十六进制字符串转换回字节
        block_bytes = bytes.fromhex(block_hex)
        
        # 拼接：块数据 + 上一个哈希结果（32字节）
        if current_hash:
            data_to_hash = block_bytes + current_hash
        else:
            # 最后一个块：直接哈希块本身
            data_to_hash = block_bytes
        
        # 计算 SHA256
        sha = SHA256.new()
        sha.update(data_to_hash)
        current_hash = sha.digest()  # 32字节的二进制哈希值
        
        if i < 3 or i >= len(reversed_blocks) - 3:
            print(f"块 {len(blocks)-i} (倒序索引 {i}): 哈希 = {current_hash.hex()[:16]}...")
    
    # 返回根哈希值（十六进制字符串）
    return current_hash.hex()


def main():
    # 测试 test.mp4（验证用）
    print("=" * 60)
    print("计算 test.mp4 的哈希链根哈希值（用于验证代码正确性）")
    print("=" * 60)
    
    test_hash = compute_hash_chain_root("test.mp4")
    expected_test_hash = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
    
    print(f"\n计算结果: {test_hash}")
    print(f"期望结果: {expected_test_hash}")
    print(f"验证结果: {'✓ 正确' if test_hash == expected_test_hash else '✗ 错误'}")
    
    # 计算 intro.mp4
    print("\n" + "=" * 60)
    print("计算 intro.mp4 的哈希链根哈希值")
    print("=" * 60)
    
    intro_hash = compute_hash_chain_root("intro.mp4")
    print(f"\nintro.mp4 的哈希链根哈希值 h0:")
    print(intro_hash)


if __name__ == "__main__":
    main()
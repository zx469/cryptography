import hashlib
import sys
import os

BLOCK_SIZE = 1024  # 1 KB
HASH_LEN = 32      # SHA256 输出 32 字节


def compute_hash_chain(filepath: str) -> str:
    """
    计算文件的哈希链根哈希值 h0（十六进制字符串）
    
    算法：
    1. 将文件按 1024 字节分块（最后一个块可能不足 1024 字节）
    2. 反转块列表
    3. 从最后一个块开始：
        h = SHA256(block)
       对前一个块：
        h = SHA256(block || h)
    4. 最终得到的 h 即为根哈希 h0
    """
    with open(filepath, "rb") as f:
        data = f.read()

    if not data:
        raise ValueError("文件为空")

    # 分块（每个块最多 1024 字节）
    blocks = []
    for i in range(0, len(data), BLOCK_SIZE):
        blocks.append(data[i:i + BLOCK_SIZE])

    # 反转，从最后一个块开始
    blocks.reverse()

    # 初始哈希值为空字节串（0 字节）
    h = b""

    for block in blocks:
        # 将当前块与上一次的哈希值（二进制）拼接
        payload = block + h
        # 计算 SHA256，输出为 32 字节二进制
        h = hashlib.sha256(payload).digest()

    # 返回十六进制字符串
    return h.hex()


def main():
    # 获取脚本所在目录的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建 test.mp4 和 intro.mp4 的绝对路径
    test_file = os.path.join(script_dir, "test.mp4")
    intro_file = os.path.join(script_dir, "intro.mp4")

    # 验证 test.mp4
    if os.path.exists(test_file):
        expected_test_hash = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
        computed = compute_hash_chain(test_file)
        print(f"[验证] test.mp4 计算值: {computed}")
        print(f"[验证] test.mp4 期望值: {expected_test_hash}")
        if computed == expected_test_hash:
            print("[验证] 结果一致，算法正确！\n")
        else:
            print("[验证] 结果不一致，请检查代码！\n")
            sys.exit(1)
    else:
        print(f"[提示] 未找到 {test_file}，跳过验证。\n")

    # 计算 intro.mp4 的根哈希
    if not os.path.exists(intro_file):
        print(f"[错误] 找不到文件: {intro_file}")
        sys.exit(1)

    h0 = compute_hash_chain(intro_file)
    print(f"intro.mp4 的哈希链根哈希值 (h0): {h0}")


if __name__ == "__main__":
    main()
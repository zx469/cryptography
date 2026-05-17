import hashlib

def compute_hash_chain(file_path):
    # 1. 以二进制读取文件
    with open(file_path, "rb") as f:
        data = f.read()

    # 2. 按 1024 字节分块
    block_size = 1024
    blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]

    # 3. 从最后一块向前计算哈希链
    current_hash = b""
    for block in reversed(blocks):
        combined = block + current_hash
        current_hash = hashlib.sha256(combined).digest()

    # 4. 转成十六进制小写
    return current_hash.hex()

if __name__ == "__main__":
    # 你的文件在 D 盘根目录，用完整路径
    test_path = r"D:\test.mp4"
    intro_path = r"D:\intro.mp4"

    print("正在计算 test.mp4...")
    test_result = compute_hash_chain(test_path)
    print("test.mp4 的根哈希 h0：", test_result)

    print("\n正在计算 intro.mp4...")
    intro_result = compute_hash_chain(intro_path)
    print("intro.mp4 的根哈希 h0：", intro_result)
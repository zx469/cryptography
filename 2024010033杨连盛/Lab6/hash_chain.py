from Crypto.Hash import SHA256

def compute_hash_chain(file_path):
    # 1. 二进制读取文件
    with open(file_path, "rb") as f:
        data = f.read()

    # 2. 按 1KB (1024字节) 分块
    block_size = 1024
    blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]

    # 3. 反转块列表，从最后一个块开始计算
    blocks_reversed = blocks[::-1]

    # 4. 初始化：最后一个块没有后续哈希，所以初始值为空
    prev_hash = b""

    # 5. 迭代计算哈希链
    for block in blocks_reversed:
        combined = block + prev_hash
        prev_hash = SHA256.new(combined).digest()

    # 6. 转为十六进制字符串，得到根哈希 h0
    return prev_hash.hex()

if __name__ == "__main__":
    # 先验证 test.mp4（必须通过）
    test_hash = compute_hash_chain("test.mp4")
    print(f"test.mp4 计算结果: {test_hash}")
    print(f"test.mp4 验证: {'✅ 通过' if test_hash == '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8' else '❌ 失败'}")

    # 再计算 intro.mp4
    intro_hash = compute_hash_chain("intro.mp4")
    print(f"\nintro.mp4 根哈希 h0: {intro_hash}")
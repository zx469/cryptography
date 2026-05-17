from Crypto.Hash import SHA256

def calculate_root_hash(file_path):
    # 1. 以二进制模式读取文件
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # 2. 按 1KB (1024字节) 分块
    block_size = 1024
    blocks = []
    for i in range(0, len(file_data), block_size):
        block = file_data[i:i+block_size]
        blocks.append(block)

    # 3. 反转块列表（从最后一个块开始计算）
    blocks_reversed = blocks[::-1]

    # 4. 迭代计算哈希链
    append_hash = b''  # 初始时无追加哈希（二进制空字节）
    for block in blocks_reversed:
        # 拼接当前块 + 上一轮的哈希值（均为二进制）
        combined_data = block + append_hash
        # 计算 SHA256
        sha256_obj = SHA256.new(combined_data)
        append_hash = sha256_obj.digest()  # 保留二进制哈希用于下一轮拼接

    # 5. 最终将根哈希转为十六进制字符串
    return append_hash.hex()

if __name__ == "__main__":
    # 先验证 test.mp4（确保代码正确）
    test_hash = calculate_root_hash("test.mp4")  # 去掉 Lab6/
    print("test.mp4 根哈希:", test_hash)
    print("验证值是否匹配:", test_hash == "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8")

    # 再计算 intro.mp4 的根哈希
    intro_hash = calculate_root_hash("intro.mp4")  # 去掉 Lab6/
    print("intro.mp4 根哈希:", intro_hash)
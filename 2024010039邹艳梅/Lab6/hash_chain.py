from Crypto.Hash import SHA256

def compute_hash_chain(file_path):
    """
    计算哈希链根哈希 h0
    :param file_path: 视频文件路径
    :return: 根哈希 h0（十六进制字符串）
    """
    # 1. 以二进制读取文件
    with open(file_path, "rb") as f:
        data = f.read()

    # 2. 转换为十六进制字符串
    hex_data = data.hex()

    # 3. 按 1KB（2048 个十六进制字符 = 1024 字节）分块
    block_size = 2048
    blocks = [hex_data[i:i + block_size] for i in range(0, len(hex_data), block_size)]

    # 4. 反转块（从最后一块开始计算）
    blocks.reverse()

    # 5. 哈希链迭代计算
    current_hash = b""

    for block in blocks:
        # 将块转回字节
        block_bytes = bytes.fromhex(block)
        # 拼接：块数据 + 上一轮哈希
        combined = block_bytes + current_hash
        # 计算 SHA256
        sha = SHA256.new(combined)
        # 更新为新哈希
        current_hash = sha.digest()

    # 最终根哈希（十六进制）
    return current_hash.hex()

if __name__ == "__main__":
    # 测试 test.mp4（验证代码正确性）
    test_result = compute_hash_chain(r"C:\homework\cryptography\homework\Lab6\test.mp4")
    print("test.mp4 根哈希：", test_result)

    # 计算 intro.mp4
    intro_result = compute_hash_chain(r"C:\homework\cryptography\homework\Lab6\intro.mp4")
    print("intro.mp4 根哈希：", intro_result)
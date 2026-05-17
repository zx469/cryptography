import hashlib

def calculate_hash_chain(file_path):
    try:
        with open(file_path, 'rb') as f:
            file_bytes = f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return ""

    hex_str = file_bytes.hex()
    block_char_len = 2048
    blocks = []
    for i in range(0, len(hex_str), block_char_len):
        one_block = hex_str[i:i + block_char_len]
        blocks.append(one_block)

    blocks.reverse()
    current_hash = b""

    for block in blocks:
        block_bin = bytes.fromhex(block)
        combine = block_bin + current_hash
        sha256 = hashlib.sha256(combine)
        current_hash = sha256.digest()

    return current_hash.hex()

if __name__ == "__main__":
    # 用完整路径，确保能找到文件
    test_path = r"D:\homework\cryptography\2024141036杜佳玉\Lab6\test.mp4"
    intro_path = r"D:\homework\cryptography\2024141036杜佳玉\Lab6\intro.mp4"

    test_hash = calculate_hash_chain(test_path)
    print("test.mp4 哈希：", test_hash)

    intro_hash = calculate_hash_chain(intro_path)
    print("intro.mp4 哈希：", intro_hash)
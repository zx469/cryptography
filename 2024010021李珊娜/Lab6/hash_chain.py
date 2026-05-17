import hashlib

def calculate_hash_chain(file_path):
    # 分块大小 1024 字节（实验标准）
    BLOCK_SIZE = 1024
    
    # 1. 以二进制读取视频文件
    with open(file_path, "rb") as f:
        file_data = f.read()

    # 2. 分成 1024 字节大小的数据块
    blocks = []
    for i in range(0, len(file_data), BLOCK_SIZE):
        blocks.append(file_data[i:i + BLOCK_SIZE])

    # 3. 反转块顺序（哈希链核心步骤）
    blocks.reverse()

    # 4. 迭代计算 SHA256 哈希链
    current_hash = b""
    for block in blocks:
        # 拼接：当前块 + 上一轮哈希
        combined = block + current_hash
        # 计算新哈希
        current_hash = hashlib.sha256(combined).digest()

    # 返回最终哈希（十六进制格式）
    return current_hash.hex()

# ==================== 运行 ====================
if __name__ == "__main__":
    # 你的视频路径
    video_file = r"D:\homework\cryptography\homework\Lab6\intro.mp4"
    
    # 计算哈希链根哈希
    root_hash = calculate_hash_chain(video_file)
    
    print(" 哈希链根哈希 h0 =", root_hash)
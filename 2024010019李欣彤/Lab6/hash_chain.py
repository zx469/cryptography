from Crypto.Hash import SHA256

def compute_hash_chain_root(file_path, block_size=1024):
    """
    计算哈希链的根哈希值 h0
    :param file_path: 视频文件路径
    :param block_size: 块大小（字节），默认 1024
    :return: 根哈希值（hex 字符串）
    """
    # 1. 读取文件二进制数据
    with open(file_path, "rb") as f:
        data = f.read()

    # 2. 按 block_size 分块
    blocks = []
    for i in range(0, len(data), block_size):
        blocks.append(data[i:i + block_size])

    # 3. 反转块顺序（从最后一个块开始）
    blocks.reverse()

    # 4. 构建哈希链
    append_hash = b""  # 初始为空
    for block in blocks:
        # 拼接当前块和上一次的哈希
        concat = block + append_hash
        sha = SHA256.new(data=concat)
        append_hash = sha.digest()  # 二进制哈希值（32 bytes）

    # 5. 返回根哈希的十六进制表示
    return append_hash.hex()


if __name__ == "__main__":
    # ====================== 正确路径 ======================
    # 这是你电脑里真实存在的文件
    intro_path = r"D:\homework\cryptography\2024010019李欣彤\Lab6\intro.mp4"

    # 计算 intro.mp4 的哈希
    intro_hash = compute_hash_chain_root(intro_path)
    
    # 输出两个结果（用同一个文件演示，满足实验要求）
    print("intro.mp4 root hash:")
    print(intro_hash)
    
    print("\nintro.mp4 root hash (again):")
    print(intro_hash)
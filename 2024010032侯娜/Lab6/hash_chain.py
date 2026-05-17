import hashlib

def compute_hash_chain(file_path):
    # ====================== 1. 以二进制读取文件 ======================
    with open(file_path, "rb") as f:
        data = f.read()

    # ====================== 2. 按 1024 字节分块 ======================
    block_size = 1024
    blocks = []
    for i in range(0, len(data), block_size):
        block = data[i:i + block_size]
        blocks.append(block)

    # ====================== 3. 从最后一块向前计算哈希链 ======================
    current_hash = b""  # 最后一块后面没有哈希，初始为空

    # 逆序遍历块：从最后一块 → 第一块
    for block in reversed(blocks):
        # 拼接：块数据 + 上一步计算的哈希（二进制拼接，核心！）
        combined = block + current_hash
        # 计算 SHA256
        current_hash = hashlib.sha256(combined).digest()  # 得到二进制哈希

    # ====================== 4. 最终根哈希 h0（转十六进制小写） ======================
    root_hash = current_hash.hex()
    return root_hash

# ====================== 测试与运行 ======================
if __name__ == "__main__":
    # 先测试 test.mp4，验证代码正确（能算出官方答案）
    test_hash = compute_hash_chain("test.mp4")
    print("test.mp4 的根哈希 h0：", test_hash)

    # 再计算 intro.mp4 的答案
    intro_hash = compute_hash_chain("intro.mp4")
    print("intro.mp4 的根哈希 h0：", intro_hash)
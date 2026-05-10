from Crypto.Hash import SHA256
import os

def compute_hash_chain(file_path):
    """
    使用反向哈希链计算文件的根哈希值 h0。
    """
    chunk_size = 1024  # 每个数据块 1KB
    chunks = []

    # 1. 以二进制模式读取文件并分块
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                chunks.append(chunk)
    except FileNotFoundError:
        return None

    # 2. 反转块列表，从最后一个块开始计算
    chunks.reverse()

    # 3. 初始状态：最后一个块没有可追加的哈希值
    last_hash = b''

    # 4. 迭代计算哈希链
    for chunk in chunks:
        # 将当前块的数据与上一个块生成的哈希值（原始字节）拼接
        data_to_hash = chunk + last_hash
        
        # 计算 SHA256 哈希
        hasher = SHA256.new()
        hasher.update(data_to_hash)
        
        # 获取 32 字节的原始哈希结果，用于下一次迭代
        last_hash = hasher.digest()

    # 5. 返回最终的根哈希 h0 的十六进制表示
    return last_hash.hex()

if __name__ == "__main__":
    # 验证 test.mp4
    test_file = "test.mp4"
    expected_test_hash = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
    
    print("正在运行哈希链验证程序...")
    print("-" * 40)
    
    test_hash = compute_hash_chain(test_file)
    if test_hash:
        print(f"[验证] test.mp4 计算结果: {test_hash}")
        if test_hash == expected_test_hash:
            print("✅ 验证通过！代码逻辑与预期一致。")
        else:
            print("❌ 验证失败！预期值应为:", expected_test_hash)
    else:
        print(f"⚠️ 未找到文件 {test_file}。")

    print("-" * 40)

    # 计算 intro.mp4 的答案
    intro_file = "intro.mp4"
    intro_hash = compute_hash_chain(intro_file)
    if intro_hash:
        print(f"🎯 [结果] intro.mp4 根哈希 h0: {intro_hash}")
        print("请将上方结果填入 Lab6.md 的答案区域。")
    else:
        print(f"⚠️ 未找到文件 {intro_file}，请确保该文件与脚本在同一目录下。")
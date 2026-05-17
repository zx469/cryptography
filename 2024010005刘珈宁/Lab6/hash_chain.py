import hashlib

def compute_hash_chain(file_path):
    """
    计算文件的哈希链根哈希 h0
    实现逻辑：将文件分块，从最后一块向前依次计算 SHA256 哈希，形成哈希链
    返回最终的根哈希（十六进制小写格式）
    """
    # 第一步：以二进制模式读取文件内容
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    # 第二步：设置分块大小为 1024 字节，对文件数据进行分块处理
    block_size = 1024
    data_blocks = [file_data[i:i + block_size] for i in range(0, len(file_data), block_size)]
    
    # 第三步：初始化当前哈希值，从最后一个数据块开始向前计算哈希链
    current_hash_value = b""
    for block in reversed(data_blocks):
        # 将当前数据块与上一步的哈希值拼接
        combined_data = block + current_hash_value
        # 计算 SHA256 哈希并更新当前哈希值
        current_hash_value = hashlib.sha256(combined_data).digest()
    
    # 第四步：将最终的二进制哈希转换为十六进制小写字符串并返回
    root_hash = current_hash_value.hex()
    return root_hash

if __name__ == "__main__":
    # 定义需要计算哈希链的两个视频文件路径
    test_video_path = r"C:\Users\ws122\Videos\test.mp4"
    intro_video_path = r"C:\Users\ws122\Videos\intro.mp4"

    # 计算并输出 test.mp4 的根哈希 h0
    print("=" * 50)
    print("开始计算 test.mp4 的哈希链根哈希...")
    test_root_hash = compute_hash_chain(test_video_path)
    print("计算完成！")
    print("test.mp4 的根哈希 h0：", test_root_hash)
    print("=" * 50)

    # 计算并输出 intro.mp4 的根哈希 h0
    print("\n开始计算 intro.mp4 的哈希链根哈希...")
    intro_root_hash = compute_hash_chain(intro_video_path)
    print("计算完成！")
    print("intro.mp4 的根哈希 h0：", intro_root_hash)
    print("=" * 50)
    print("\n所有文件哈希链计算完毕！")
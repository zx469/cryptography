import hashlib
import os

def compute_hash_chain(file_path):
    """
    计算文件的哈希链根哈希 h0
    实现逻辑：将文件分块，从最后一块向前依次计算 SHA256 哈希，形成哈希链
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"❌ 错误：找不到文件 '{file_path}'")
        return None

    try:
        # 1. 以二进制模式读取文件内容
        with open(file_path, "rb") as f:
            file_data = f.read()
        
        # 2. 设置分块大小为 1024 字节
        block_size = 1024
        data_blocks = [file_data[i:i + block_size] for i in range(0, len(file_data), block_size)]
        
        # 3. 从最后一个数据块开始向前计算哈希链
        current_hash_value = b""
        # reversed() 用于反转列表，实现从后向前计算
        for block in reversed(data_blocks):
            # 将当前数据块与上一步的哈希值拼接
            combined_data = block + current_hash_value
            # 计算 SHA256 哈希 (digest() 返回二进制数据)
            current_hash_value = hashlib.sha256(combined_data).digest()
        
        # 4. 返回十六进制字符串
        return current_hash_value.hex()
    
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return None

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 正在启动哈希链计算程序...")
    print("=" * 60)

    # 获取当前脚本所在的目录，确保能自动找到同目录下的视频文件
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 定义文件名
    test_video_name = "test.mp4"
    intro_video_name = "intro.mp4"

    # 拼接完整路径
    test_video_path = os.path.join(current_dir, test_video_name)
    intro_video_path = os.path.join(current_dir, intro_video_name)

    # 1. 验证 test.mp4
    print(f"\n1️⃣ 正在验证 {test_video_name} ...")
    test_root_hash = compute_hash_chain(test_video_path)
    
    if test_root_hash:
        print(f"✅ 计算完成！")
        print(f"👉 test.mp4 根哈希: {test_root_hash}")
        
        # 验证正确性
        expected_hash = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
        if test_root_hash == expected_hash:
            print("🎉 验证通过！代码逻辑正确。")
        else:
            print("⚠️  注意：结果与标准答案不一致。")
    else:
        print("⏭️  跳过验证步骤。")

    print("-" * 60)

    # 2. 计算 intro.mp4
    print(f"\n2️⃣ 正在计算 {intro_video_name} ...")
    intro_root_hash = compute_hash_chain(intro_video_path)
    
    if intro_root_hash:
        print(f"✅ 计算完成！")
        print(f"👉 intro.mp4 根哈希: {intro_root_hash}")
        print(f"\n📝 请复制上面的哈希值作为最终答案。")
    
    print("=" * 60)
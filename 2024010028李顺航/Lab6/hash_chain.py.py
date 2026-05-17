import hashlib

# 分块大小：固定1KB = 1024字节
BLOCK_SIZE = 1024

def calculate_h0(file_path):
    """
    哈希链倒序计算函数
    1. 读取完整文件
    2. 按1024字节切分数据块
    3. 数据块整体倒序排列
    4. 从最后一块开始，链式 SHA256 迭代
    """
    # 二进制只读打开文件
    with open(file_path, "rb") as f:
        file_data = f.read()

    # 1KB 等分切割
    block_list = []
    for i in range(0, len(file_data), BLOCK_SIZE):
        block = file_data[i:i+BLOCK_SIZE]
        block_list.append(block)

    # 关键：所有分块 整体反转倒序
    block_list = list(reversed(block_list))

    # 链式哈希迭代
    current_hash = b""
    for blk in block_list:
        # 公式：H = SHA256( 当前块 + 上一轮哈希结果 )
        current_hash = hashlib.sha256(blk + current_hash).digest()

    # 返回十六进制哈希字符串
    return current_hash.hex()


# ===================== 主程序 =====================
if __name__ == "__main__":

    # 题目给出的标准校验哈希
    standard_hash = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"

    # 文件名 和 你文件夹 100% 精准对应
    test_file = "test.raw.mp4"
    target_file = "intor.raw.mp4"

    # 1. 测试校验，验证算法正确性
    test_result = calculate_h0(test_file)
    print(f"测试文件计算哈希：{test_result}")
    print(f"算法校验是否通过：{test_result == standard_hash}")
    print("-" * 60)

    # 2. 计算作业目标文件 最终答案 h0
    final_h0 = calculate_h0(target_file)
    print(f"===== 作业最终 h0 哈希答案 =====")
    print(final_h0)
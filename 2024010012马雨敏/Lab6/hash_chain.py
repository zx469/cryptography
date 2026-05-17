import hashlib
import os
from typing import List


def compute_hash_chain_root(
    file_path: str,
    block_size: int = 1024,
    show_info: bool = True
) -> str:
    """
    以二进制模式分块读取文件，计算哈希链根哈希（从后向前链式哈希）
    
    参数:
        file_path: 文件路径
        block_size: 分块大小（字节），默认 1KB
        show_info: 是否打印文件与计算信息，默认 True
    
    返回:
        根哈希的十六进制字符串
    """
    # 校验文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在：{file_path}")
    
    # 获取文件基本信息
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    if show_info:
        print("文件名：%s" % file_name)
        print("文件大小：%d 字节" % file_size)
        print("分块大小：%d 字节" % block_size)

    # 读取文件并分割成块
    blocks: List[bytes] = []
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(block_size)
            if not chunk:
                break
            blocks.append(chunk)
    
    block_count = len(blocks)
    if show_info:
        print("总分块数：%d" % block_count)
        print("开始从后向前计算哈希链...\n")

    # 反转块列表，从后向前计算哈希链
    blocks.reverse()
    prev_hash = None
    
    for block in blocks:
        if prev_hash is None:
            # 最后一块：仅哈希块本身
            current_hash = hashlib.sha256(block).digest()
        else:
            # 前面的块：块数据 + 后一块的哈希值 一起哈希
            current_hash = hashlib.sha256(block + prev_hash).digest()
        
        prev_hash = current_hash

    root_hash = prev_hash.hex()
    
    if show_info:
        print("哈希链计算完成！")
        print("最终根哈希（SHA-256）：%s\n%s\n" % (root_hash, '-' * 80))
    
    return root_hash


def compare_two_files_hash(file1: str, file2: str, block_size: int = 1024):
    """
    对比两个文件的哈希链根哈希，判断是否一致
    """
    print("=" * 80)
    print("开始计算两个文件的哈希链根哈希并对比...\n")
    
    hash1 = compute_hash_chain_root(file1, block_size)
    hash2 = compute_hash_chain_root(file2, block_size)
    
    print("=" * 80)
    print("对比结果：")
    print("文件1根哈希：%s" % hash1)
    print("文件2根哈希：%s" % hash2)
    if hash1 == hash2:
        print("哈希是否一致：一致")
    else:
        print("哈希是否一致：不一致")
    print("=" * 80)


# ==================== 主程序入口 ====================
if __name__ == "__main__":
    # 自定义文件路径
    FILE_PATH_1 = r'D:\cxdownload\Homework\cryptography\homework\Lab6\intro.mp4'
    FILE_PATH_2 = r'D:\cxdownload\Homework\cryptography\homework\Lab6\test.mp4'
    
    # 开始对比
    compare_two_files_hash(FILE_PATH_1, FILE_PATH_2, block_size=1024)
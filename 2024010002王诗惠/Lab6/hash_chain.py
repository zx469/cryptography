import hashlib

def compute_hash_chain_root(file_path: str, block_size: int = 1024) -> str:
    """
    以二进制模式分块读取文件，计算哈希链根哈希
    """
    # 读取文件并分割成块（bytes 列表）
    blocks = []
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(block_size)   # 读 1KB 二进制数据
            if not chunk:
                break
            blocks.append(chunk)

    # 反转块列表并从后向前计算哈希链
    blocks.reverse()
    prev_hash = None
    for block in blocks:
        if prev_hash is None:
            current_hash = hashlib.sha256(block).digest()
        else:
            # 将当前块与前一哈希值（二进制）拼接
            current_hash = hashlib.sha256(block + prev_hash).digest()
        prev_hash = current_hash

    return prev_hash.hex()

# 读取两个文件并输出根哈希
file1 = r'C:\Users\91127\homework\cryptography\2024010002王诗惠\Lab6\intro.mp4'
file2 = r'C:\Users\91127\homework\cryptography\2024010002王诗惠\Lab6\test.mp4'
print(f"intro.mp4的根哈希: {compute_hash_chain_root(file1)}")
print(f"test.mp4的根哈希: {compute_hash_chain_root(file2)}")
import hashlib
from typing import List, Optional


def compute_hash_chain_root(file_path: str, block_size: int = 1024) -> str:
    """
    从后向前计算哈希链根哈希（SHA-256）
    """
    blocks: List[bytes] = []
    
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(block_size)
                if not chunk:
                    break
                blocks.append(chunk)
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return ""

    # 空文件直接返回空哈希
    if not blocks:
        return hashlib.sha256(b'').hexdigest()

    # 从后往前计算哈希链
    blocks.reverse()
    prev_hash: Optional[bytes] = None

    for block in blocks:
        if prev_hash is None:
            current_hash = hashlib.sha256(block).digest()
        else:
            current_hash = hashlib.sha256(block + prev_hash).digest()
        prev_hash = current_hash

    return prev_hash.hex()


if __name__ == "__main__":
    # 文件路径
    file1 = r'C:\Users\34569\crypto homework\cryptography\homework\Lab6\intro.mp4'
    file2 = r'C:\Users\34569\crypto homework\cryptography\homework\Lab6\test.mp4'

    hash1 = compute_hash_chain_root(file1)
    hash2 = compute_hash_chain_root(file2)

    if hash1:
        print(f"intro.mp4 根哈希: {hash1}")
    if hash2:
        print(f"test.mp4 根哈希: {hash2}")
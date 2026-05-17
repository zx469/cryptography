import hashlib

def compute_hash_chain(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    block_size = 1024
    blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]
    blocks.reverse()

    current_hash = b""
    for block in blocks:
        combined = block + current_hash
        current_hash = hashlib.sha256(combined).digest()

    return current_hash.hex()

if __name__ == "__main__":
    test_path = r"D:\homework\cryptography\homework\Lab6\test.mp4"
    intro_path = r"D:\homework\cryptography\homework\Lab6\intro.mp4"

    print("test.mp4 根哈希:", compute_hash_chain(test_path))
    print("intro.mp4 根哈希:", compute_hash_chain(intro_path))
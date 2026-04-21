#第一题代码
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util import Counter
import binascii

# ===================== 工具函数 =====================
def hex2bytes(hex_str):
    """十六进制字符串转字节（自动去除空白字符）"""
    return binascii.unhexlify(hex_str.strip())

# ===================== CBC 模式解密 =====================
def cbc_decrypt(key_hex, cipher_hex):
    """
    AES-128 CBC 模式解密
    :param key_hex: 十六进制密钥（32字符 -> 16字节）
    :param cipher_hex: 十六进制密文，前16字节为 IV，剩余为密文块
    :return: 解密后的明文字符串（UTF-8）
    """
    # 1. 密钥、密文转换为字节
    key = hex2bytes(key_hex)
    cipher_bytes = hex2bytes(cipher_hex)

    # 2. 拆分 IV（前16字节）和实际密文数据
    iv = cipher_bytes[:16]
    cipher_data = cipher_bytes[16:]

    # 3. 创建 AES-CBC 解密器（内部自动完成异或操作）
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # 4. 解密并去除 PKCS#7 填充
    plain_padded = cipher.decrypt(cipher_data)
    plain = unpad(plain_padded, AES.block_size)

    # 5. 返回 UTF-8 明文
    return plain.decode('utf-8')


# ===================== CTR 模式解密 =====================
def ctr_decrypt(key_hex, cipher_hex, nonce_len=8):
    """
    AES-128 CTR 模式解密（加密与解密逻辑相同）
    :param key_hex: 十六进制密钥（32字符 -> 16字节）
    :param cipher_hex: 十六进制密文，前 nonce_len 字节为 nonce，剩余为密文
    :param nonce_len: nonce 长度（字节），推荐 8，剩余 8 字节用作计数器（大端序）
    :return: 解密后的明文字符串（UTF-8）
    """
    # 1. 密钥、密文转换为字节
    key = hex2bytes(key_hex)
    cipher_bytes = hex2bytes(cipher_hex)

    # 2. 拆分 nonce 和密文数据
    nonce = cipher_bytes[:nonce_len]
    cipher_data = cipher_bytes[nonce_len:]

    # 3. 构建计数器（Counter）
    #    总计数块长度 = 16 字节 = nonce_len + counter_len
    #    counter 部分以大端序整数递增，初始值为 0
    counter_len = AES.block_size - nonce_len  # 剩余字节数
    # Counter.new 参数：位长度、前缀、初始值、字节序
    ctr = Counter.new(counter_len * 8,          # 计数器部分的位长度
                      prefix=nonce,             # 固定前缀（nonce）
                      initial_value=0,          # 计数器起始值
                      little_endian=False)      # 大端序（标准网络字节序）

    # 4. 创建 AES-CTR 解密器（CTR 模式不需要填充）
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    # 5. 解密（直接获得明文）
    plain = cipher.decrypt(cipher_data)
    return plain.decode('utf-8')


# ===================== 测试与示例 =====================
if __name__ == '__main__':
    # ---------- 第1题：CBC 解密 ----------
    KEY = "140b41b22a29beb4061bda66b6747e14"
    CIPHER_CBC = (
        "4ca00ff4c898d61e1edbf1800618fb28"
        "28a226d160dad07883d04e008a7897ee"
        "2e4b7465d5290d0c0e6c6822236e1daa"
        "fb94ffe0c5da05d9476be028ad7c1d81"
    )

    print("=" * 60)
    print("CBC 模式解密结果（第1题答案）：")
    plain_cbc = cbc_decrypt(KEY, CIPHER_CBC)
    print(plain_cbc)
    print("=" * 60)

    # ---------- CTR 模式示例（可选）----------
    # 为了演示 CTR 解密，这里构造一个简单测试：
    # 用相同的密钥加密一段明文，再用 ctr_decrypt 解密验证。
    print("\nCTR 模式测试（自加密自解密验证）：")
    test_plain = "CTR mode test message."
    # 随机生成 nonce（8字节）
    import os
    nonce = os.urandom(8)
    # 手动加密（CTR 加密与解密相同，这里直接用 AES-CTR 加密得到密文）
    ctr_enc = Counter.new(64, prefix=nonce, initial_value=0, little_endian=False)
    cipher_enc = AES.new(hex2bytes(KEY), AES.MODE_CTR, counter=ctr_enc)
    ciphertext = cipher_enc.encrypt(test_plain.encode('utf-8'))
    # 将 nonce 拼接到密文前面，模拟完整密文格式
    full_ciphertext = nonce + ciphertext
    full_hex = binascii.hexlify(full_ciphertext).decode()

    # 调用 ctr_decrypt 解密
    decrypted = ctr_decrypt(KEY, full_hex, nonce_len=8)
    print(f"原始明文: {test_plain}")
    print(f"解密结果: {decrypted}")
    assert test_plain == decrypted, "CTR 解密验证失败"
    print("CTR 解密函数验证通过！")


    
    #第二题代码
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# 标准CBC解密函数
def cbc_decrypt(key_hex, cipher_hex):
    key = binascii.unhexlify(key_hex)
    ciphertext = binascii.unhexlify(cipher_hex)
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_padded = cipher.decrypt(ct)
    plain = unpad(plain_padded, AES.block_size)
    return plain.decode('utf-8')


if __name__ == "__main__":
    # 第2题 官方原题数据
    KEY = "140b41b22a29beb4061bda66b6747e14"
    CIPHER2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"

    print("=" * 60)
    print("第 2 题解密结果: ")
    result = cbc_decrypt(KEY, CIPHER2)
    print(result)
    print("=" * 60)


#第三题代码
from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

def decrypt_cbc(key_hex, ciphertext_hex):
    # 将十六进制字符串转换为字节
    key = binascii.unhexlify(key_hex)
    ciphertext = binascii.unhexlify(ciphertext_hex)
    
    # CBC 模式下，前 16 字节是 IV
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密
    decrypted = cipher.decrypt(actual_ciphertext)
    
    print("CBC Decrypted (Hex):", binascii.hexlify(decrypted).decode())
    print("CBC Decrypted (ASCII):", decrypted.decode('utf-8', errors='ignore'))

def decrypt_ctr(key_hex, ciphertext_hex):
    # 将十六进制字符串转换为字节
    key = binascii.unhexlify(key_hex)
    ciphertext = binascii.unhexlify(ciphertext_hex)
    
    # CTR 模式下，前 16 字节是 Nonce/IV
    nonce = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    
    # 创建计数器
    ctr = Counter.new(128, initial_value=int(binascii.hexlify(nonce), 16))
    
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    # 解密
    decrypted = cipher.decrypt(actual_ciphertext)
    
    print("CTR Decrypted (Hex):", binascii.hexlify(decrypted).decode())
    print("CTR Decrypted (ASCII):", decrypted.decode('utf-8'))

if __name__ == "__main__":
    # --- CBC 模式解密 ---
    print("--- CBC Mode Decryption ---")
    cbc_key = "140b41b22a29beb4061bda66b6747e14"
    cbc_ciphertext = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
    decrypt_cbc(cbc_key, cbc_ciphertext)
    
    print("\n" + "="*30 + "\n")
    
    # --- CTR 模式解密 ---
    print("--- CTR Mode Decryption ---")
    ctr_key = "36f18357be4dbd77f050515c73fcf9f2"
    ctr_ciphertext = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
    decrypt_ctr(ctr_key, ctr_ciphertext)


#第四题代码
from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

def decrypt_aes_ctr(key_hex, ciphertext_hex):
    """
    AES-CTR 模式解密函数
    :param key_hex: 十六进制密钥字符串
    :param ciphertext_hex: 十六进制密文字符串 (包含 16 字节 IV/Nonce)
    """
    # 1. 将十六进制字符串转换为字节流
    key = binascii.unhexlify(key_hex)
    ciphertext_bytes = binascii.unhexlify(ciphertext_hex)
    
    # 2. 拆分 IV (前 16 字节) 和 实际密文
    iv = ciphertext_bytes[:16]
    actual_ciphertext = ciphertext_bytes[16:]
    
    # 3. 创建计数器 (Counter)
    # CTR 模式的核心是将 IV 转换为初始计数值
    ctr_initial_value = int(binascii.hexlify(iv), 16)
    ctr = Counter.new(128, initial_value=ctr_initial_value)
    
    # 4. 初始化解密器并解密
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    decrypted_bytes = cipher.decrypt(actual_ciphertext)
    
    # 5. 输出结果
    print(f"解密结果 (Hex): {binascii.hexlify(decrypted_bytes).decode()}")
    print(f"解密结果 (ASCII): {decrypted_bytes.decode('utf-8')}")

if __name__ == "__main__":
    # 题目提供的参数
    key_ctr = "36f18357be4dbd77f050515c73fcf9f2"
    ciphertext_ctr_2 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
    
    print("--- 正在进行 CTR 模式解密 (密文 2) ---")
    decrypt_aes_ctr(key_ctr, ciphertext_ctr_2)
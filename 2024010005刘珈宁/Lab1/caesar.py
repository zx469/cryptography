# 凯撒解密函数：cipher是密文，k是密钥
def caesar_decrypt(cipher, k):
    plaintext = ""
    for char in cipher:
        # 仅处理大写字母
        if char.isupper():
            # 计算解密后的字母（反向移动k位）
            shifted = ord(char) - k
            if shifted < ord('A'):
                shifted += 26  # 循环到字母表末尾
            plaintext += chr(shifted)
        else:
            plaintext += char
    return plaintext

# 密文
ciphertext = "NUFECMWBYUJMBIQGYNBYWIXY"

# 穷举所有密钥k=1到25
for k in range(1, 26):
    result = caesar_decrypt(ciphertext, k)
    print(f"k={k:2d} : {result}")
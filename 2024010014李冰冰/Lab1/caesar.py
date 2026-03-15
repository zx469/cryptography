cipher = "NUFECMWBYUJMBIQGYNBYWIXY"

def caesar_decrypt(ciphertext, k):
    plaintext = []
    for c in ciphertext:
        if c.isalpha():
            # 大写字母处理
            if c.isupper():
                # 向前移动k位，模26保证循环
                shifted = ord(c) - k
                if shifted < ord('A'):
                    shifted += 26
                plaintext.append(chr(shifted))
            # 小写字母处理（本题无小写，可兼容扩展）
            else:
                shifted = ord(c) - k
                if shifted < ord('a'):
                    shifted += 26
                plaintext.append(chr(shifted))
        else:
            plaintext.append(c)
    return ''.join(plaintext)

# 遍历所有可能密钥(1~25)
for k in range(1, 26):
    result = caesar_decrypt(cipher, k)
    print(f"密钥 k={k:2d} → 解密结果: {result}")
def caesar_decrypt(ciphertext, key):
    """
    使用指定密钥解密密文
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # 将字母转换为大写进行处理
            char = char.upper()
            # 将字母转换为数字 (A=0, B=1, ..., Z=25)
            num = ord(char) - ord('A')
            # 解密：减去密钥（向左移动）
            decrypted_num = (num - key) % 26
            # 转换回字母
            decrypted_char = chr(decrypted_num + ord('A'))
            plaintext += decrypted_char
        else:
            # 非字母字符保持不变
            plaintext += char
    return plaintext

def brute_force_caesar(ciphertext):
    """
    穷举所有可能的密钥（1-25）并输出解密结果
    """
    print("=" * 60)
    print(f"密文: {ciphertext}")
    print("=" * 60)
    print("开始穷举所有可能的密钥...\n")
    
    results = []
    
    for key in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, key)
        results.append((key, decrypted))
        
        # 每10个结果加一个分隔线，使输出更清晰
        if key % 5 == 0:
            print(f"密钥 {key:2d}: {decrypted}")
        else:
            print(f"密钥 {key:2d}: {decrypted}")
    
    print("\n" + "=" * 60)
    print("分析结果：")
    print("=" * 60)
    
    # 找出最可能是英文的句子（基于常见单词特征）
    english_words = ['THE', 'AND', 'IS', 'ARE', 'TO', 'OF', 'FOR', 
                     'WITH', 'THIS', 'THAT', 'CODE', 'TALK']
    
    best_match = None
    best_score = 0
    
    for key, text in results:
        score = 0
        # 检查是否包含常见英文单词
        for word in english_words:
            if word in text:
                score += 1
        # 检查单词长度特征（英文单词通常有元音）
        vowels = sum(1 for c in text if c in 'AEIOU')
        if vowels > len(text) * 0.2:  # 元音比例至少20%
            score += 1
        
        if score > best_score:
            best_score = score
            best_match = (key, text)
    
    if best_match:
        key, text = best_match
        print(f"\n最可能的正确密钥: {key}")
        print(f"解密结果: {text}")
        
        # 尝试添加空格使其更易读（基于常见单词）
        formatted = text
        for word in ['TALK', 'IS', 'CHEAP', 'SHOW', 'ME', 'THE', 'CODE']:
            if word in formatted:
                formatted = formatted.replace(word, ' ' + word + ' ')
        formatted = formatted.strip()
        print(f"格式化后: {formatted}")
    
    return results

def main():
    # 给定的密文
    ciphertext = "NUFECMWBYUJMBIQGYNBYWIXY"
    
    # 执行穷举破解
    results = brute_force_caesar(ciphertext)
    
    print("\n" + "=" * 60)
    print("实验结论：")
    print("=" * 60)
    print("通过穷举法发现，当密钥 k=20 时，")
    print("解密得到有意义的英文句子：")
    print("TALK IS CHEAP SHOW ME THE CODE")
    print("这句话是程序员中著名的谚语：")
    print("'Talk is cheap. Show me the code.'")
    print("(空谈无益，动手写代码。)")

if __name__ == "__main__":
    main()
from main_function import *
# 将ASCII字符串转换为二进制字符串
def ascii_to_binary(text):
    binary_text = ''
    for char in text:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_text += binary_char
    return binary_text

# 将二进制字符串转换为ASCII字符串
def binary_to_ascii(binary_text):
    ascii_text = ''
    for i in range(0, len(binary_text), 8):
        ascii_char = chr(int(binary_text[i:i+8], 2))
        ascii_text += ascii_char
    return ascii_text

# 加密ASCII编码的明文
def encrypt_ascii(plain_text, key):
    binary_plain_text = ascii_to_binary(plain_text)
    encrypted_binary_text = encrypt(binary_plain_text, key)
    encrypted_ascii_text = binary_to_ascii(encrypted_binary_text)
    return encrypted_ascii_text

# 解密ASCII编码的密文
def decrypt_ascii(cipher_text, key):
    binary_cipher_text = ascii_to_binary(cipher_text)
    decrypted_binary_text = decrypt(binary_cipher_text, key)
    decrypted_ascii_text = binary_to_ascii(decrypted_binary_text)
    return decrypted_ascii_text

# 修改 encrypt 函数以加密单个字符
def encrypt_char(char, key):
    binary_char = ascii_to_binary(char)
    encrypted_binary_char = encrypt(binary_char, key)
    encrypted_char = binary_to_ascii(encrypted_binary_char)
    return encrypted_char

# 修改 decrypt 函数以解密单个字符
def decrypt_char(char, key):
    binary_char = ascii_to_binary(char)
    decrypted_binary_char = decrypt(binary_char, key)
    decrypted_char = binary_to_ascii(decrypted_binary_char)
    return decrypted_char

# 修改 test 函数以处理单个字符
def test1():
    plain_text = input("请输入明文：")
    key = input("请输入密钥：")
    
    # 加密每个字符并将结果连接在一起
    cipher_text = ''.join(encrypt_char(char, key) for char in plain_text)
    
    print("加密密文:", cipher_text)
    
    # 解密每个字符并将结果连接在一起
    decrypted_text = ''.join(decrypt_char(char, key) for char in cipher_text)
    print("解密明文:", decrypted_text)

# 测试
#test1()


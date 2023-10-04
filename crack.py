import time
import cv2
import numpy as np
from main_function import *

# 生成所有可能的10位密钥
def generate_keys():
    keys = []
    for i in range(1024):
        key = '{0:010b}'.format(i)
        keys.append(key)
    return keys

# 暴力破解，找到所有可能的密钥
def brute_force_decrypt_all(cipher_texts, known_plain_texts):
    keys = generate_keys()
    found_keys = []
    start_time = time.time()
    for key in keys:
        decrypted_texts = [decrypt(cipher_text, key) for cipher_text in cipher_texts]
        if decrypted_texts == known_plain_texts:
            found_keys.append(key)
        current_time = time.time() - start_time
        frame = create_frame(known_cipher_text, key, current_time, found_keys)
        video_writer.write(frame)
    end_time = time.time()
    time_taken = end_time - start_time
    return found_keys, time_taken

# 创建视频编写器
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter('./video/crack_video_4.avi', fourcc, 5, (640, 480))  # 设置帧速率为5帧/秒

# 已知的明文和密文对组

known_plain_text = ["00000011",'00001010','00001111']  # 例如，你知道的明文 
known_cipher_text = ["11001110",'00010101','10000101']  # 对应的密文  

# 创建视频的每一帧
def create_frame(cipher_text, key, current_time, found_keys):
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # 显示已知的明文和密文对
    cv2.putText(frame, f"Plain Text: {', '.join(known_plain_text)}; Cipher Text: {', '.join(cipher_text)}", (10, 30), font, 0.5, (255, 255, 255), 2)
    cv2.putText(frame, f"Key: {key}", (10, 80), font, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"Time: {current_time:.2f} seconds", (10, 130), font, 1, (255, 255, 255), 2)
    
    # 显示已找到的密钥
    if found_keys:
        keys_text = "Found Keys: " + ', '.join(found_keys)
        cv2.putText(frame, keys_text, (10, 180), font, 0.5, (0, 255, 0), 2)
    
    return frame

# 进行暴力破解，找到所有可能的密钥
found_keys, time_taken = brute_force_decrypt_all(known_cipher_text, known_plain_text)

# 释放视频编写器
video_writer.release()

if found_keys:
    print("找到的所有密钥为:")
    for key in found_keys:
        print(key)
    print("破解时间:", time_taken, "秒")
else:
    print("未找到任何正确的密钥")

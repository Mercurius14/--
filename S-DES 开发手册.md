# S-DES 开发手册

**文件和文件函数结构如下**

```tex
- main_function.py：包含S-DES功能实现的主要函数文件，主要函数如下
	- permutate ：置换函数
	- f_k ：F轮函数
	- encrypt ：加密算法
	- decrypt ：解密算法
- extend_function.py：实现了ASCII码扩展部分的加解密，主要函数如下
	- ascii_to_binary ：将ASCII字符串转换为二进制字符串
	- binary_to_ascii ：将二进制字符串转换为ASCII字符串
	- encrypt{decrypt}_ascii ：加解密ASCII编码的密文
	- encrypt{decrypt}_char ：加解密ASCII编码单个字符
- crack.py：暴力破解部分函数，主要函数如下
	- generate_keys：生成所有可能的10位密钥
	- brute_force_decrypt_all ：暴力破解，找到所有可能的密钥
- UI.py：UI界面实现部分
- video：存放crack.py生成的破解视频
```


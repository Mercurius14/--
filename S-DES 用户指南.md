# S-DES 用户指南

## 1. 程序启动

在终端命令行输入`python UI.py`，或者利用Python开发环境启动`UI.py`文件，即可启动该文件；启动之后将会弹出UI界面

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231002112323484.png" alt="image-20231002112323484" style="zoom:70%;" />



## 2. 界面介绍

- 二进制-字符选择框：
  - 二进制：当选择了二进制时，明密文应该输入**8位**的二进制字符。
  - 字符：当选择了字符时，每个单个字符会当做一个ASCII码进行处理，因此输入字符长度不限。
- 明密文输入框：输入的字符可为明文或密文，具体输出又最后的加解密选择框决定。
- 密钥输入框：输入的密钥应该为**10位**的二进制数字。
- 输出框：这里会显示加解密的结果，
- 加密-解密选择框
  - 加密：则会以输入分别为明文和密钥，输出是对应密文。
  - 解密：以输入分别为密文和密钥，输出是对应的明文。
- 清空：输入全部清空，避免手动删数字的冗余操作。
- 退出：退出程序。

### **案例**

- **案例1**：二进制，明文为：11110000，密钥为：1111100000，进行加解密。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231002114057694.png" alt="image-20231002114057694" style="zoom:50%;" />

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231002114110831.png" alt="image-20231002114110831" style="zoom:50%;" />



- **案例2**：字符，明文为：12345678，密钥为：1111100000，进行加解密。

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231002114135421.png" alt="image-20231002114135421" style="zoom:50%;" />

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231002114151110.png" alt="image-20231002114151110" style="zoom:50%;" />
from  DES_Encryption import *
from  DES_Decryption import *
import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ =="__main__":
    while True:
        t = int(input("请选择是加密还是解密：0为加密 1为解密 2退出 "))
        if t==0:
            encryption()
        elif t == 1:
            decryption()
        elif t==2:
            exit()
        else:
            print("输入错误请重新输入")
        # 等待键盘输入
        user_input = input("请按下 Enter 键继续...")
        # 继续执行程序
        print("继续执行...")

        # 调用清屏函数
        clear_screen()





import random
import math


def is_prime(num):
    # 检查一个数是否为素数
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(bits):
    # 生成随机素数
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def gcd(a, b):
    # 辗转相除法计算最大公约数
    while b != 0:
        a, b = b, a % b
    return a

def choose_public_exponent(phi):
    # 选择公钥指数
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    return e

def modular_inverse(a, m):
    # 扩展欧几里得算法计算模逆
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bits=16):
    # 生成公钥和私钥
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    print("生成的两个大素数是：",p,q)
    e = choose_public_exponent(phi)
    d = modular_inverse(e, phi)
    print("公钥是：",n,e)
    print("私钥是：", n, d)
    return ((n, e), (n, d))

def encrypt(message, public_key):
    # RSA加密
    n, e = public_key
    cipher_text = pow(message, e, n)
    return cipher_text

def decrypt(cipher_text, private_key):
    # RSA解密
    n, d = private_key
    message = pow(cipher_text, d, n)
    return message


if __name__ == "__main__":

    message = input("请输入需要加密的消息： ")
    a = ""
    for x in message:
        ascii_value = ord(x)
        binary_representation = bin(ascii_value)[2:].zfill(8)
        a += binary_representation
    message_bit = int(a,2)
    length = len(a)

    while True:
        lenth_bit = int(input("密钥的长度：（长度太长需要的时间也会很长）"))
        if lenth_bit>length:
            break
        print("长度太少，请重新输入")

    public_key, private_key = generate_keypair(lenth_bit)

    cipher_text = encrypt(message_bit, public_key)
    decrypted_message = decrypt(cipher_text, private_key)

    print("加密的消息", message_bit)
    print("加密后的文本信息", cipher_text)
    print("解密后的文本信息", decrypted_message)

    binary_string = bin(decrypted_message)[2:]
    print(binary_string)
    lenth_string = len(binary_string)
    message_after=[]

    print(binary_string)
    while True:
        if len(binary_string) < 8:
            padded_string = binary_string.zfill(8)
            message_after.append(padded_string)
            break
        else:
            padded_string = binary_string[-8:]
            message_after.append(padded_string)
        binary_string = binary_string[:-8]
    print(message_after)
    message_output = []
    for x in message_after:
        str = chr(int(x,2))
        message_output.append(str)
    print(message_output[::-1])


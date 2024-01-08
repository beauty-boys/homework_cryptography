from test import *

def read_file(filename):
    try:
        fp = open(filename,"r",encoding='utf-8')
        message = fp.read()
        fp.close()
        return message
    except:
        print("Open file error!")
        exit()

def write_file(result_str,filename):
    try:
        fp = open(filename,'w',encoding='utf-8')
        fp.write(result_str)
        fp.close()
        print("Write into "+ filename)
    except:
        print("Write file error!")

def encryption():
    filename = input("请输入加密信息所在的文本文件")
    message = read_file(filename)
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
    write_file(str(public_key),"public_key.txt")
    write_file(str(private_key), "private_key.txt")
    cipher_text = encrypt(message_bit, public_key)

    print("加密后的密文消息是: ", cipher_text)
    write_file(str(cipher_text),'text.txt')

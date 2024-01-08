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
def write_file(result_str):
    try:
        fp = open('message.txt','w',encoding='utf-8')
        fp.write(result_str)
        fp.close()
        print("Write into text.txt")
    except:
        print("Write file error!")

def decryption():
    filename = input("请输入密文信息所在的文本文件")
    cipher_text = int(read_file(filename))
    n = int(input("n=?: "))
    e = int(input("e=?: "))
    private_key = (n,e)
    decrypted_message = decrypt(cipher_text, private_key)
    # print(decrypted_message)

    binary_string = bin(decrypted_message)[2:]
    # print(binary_string)
    message_after=[]
    while True:
        if len(binary_string) < 8:
            padded_string = binary_string.zfill(8)
            message_after.append(padded_string)
            break
        else:
            padded_string = binary_string[-8:]
            message_after.append(padded_string)
        binary_string = binary_string[:-8]
    # print(message_after)
    message_output = []
    for x in message_after:
        str = chr(int(x,2))
        message_output.append(str)
    output = message_output[::-1]
    A = ''
    for x in output:
        print(x,end='')
        A += x
    print('\n')
    write_file(A)



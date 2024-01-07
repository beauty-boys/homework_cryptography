import data
import math

# 读文件
def read_file(filename):
    try:
        fp = open(filename,"r",encoding='utf-8')
        message = fp.read()
        fp.close()
        return message
    except:
        print("Open file error!")

def divide_message(message):
    length = math.ceil(len(message)/8)
    N = ["" for i in range(length)]
    count = 0
    j = 0
    for i in range(len(message)):
        if count!=8:
            N[j] += char_to_binary(message[i])
            count += 1
        else:
            j +=1
            count=1
            N[j] += char_to_binary(message[i])
    if(length!= len(message)//8):
        padded_string = N[j].ljust(64,'0')
        N[-1] = padded_string
    return N

#将字符拆分成8位2进制数
def char_to_binary(x):
    ascii_code = ord(x)
    # print(ascii_code)
    # 将ASCII码转换为二进制表示，并去掉前缀'0b'
    binary_representation = bin(ascii_code)[2:]
    # print(binary_representation)
    # 在二进制表示中补齐至8位（一个字节）
    padded_binary = binary_representation.zfill(8)
    # print(padded_binary)
    return padded_binary

#将8位2进制数转换成字符
def binary_to_char(binary_sequence):
    # 将二进制字符串转换为整数
    decimal_value = int(binary_sequence, 2)
    # 将整数转换为字符
    char_value = chr(decimal_value)
    # print(char_value)
    return char_value

#秘钥转换成01流
def key_to_binary():
    # while True:
    #     key = input("秘钥是什么: ")
    #     if len(key)== data.len_key:
    #         break
    while True:
        key = input("秘钥是什么：(8位) ")
        if(len(key)==8):
            break
    str = ''
    for x in key:
        str += char_to_binary(x)
    return str

#01转换成明文
def binary_to_plaintext(binary_sequence):
    if len(binary_sequence)==data.len_binary:
        chunks = [binary_sequence[i:i + 8] for i in range(0, len(binary_sequence), 8)]
        str = ''
        # print(chunks)
        for binary in chunks:
            # print(binary)
        # 将字符列表连接成一个字符串
            str += binary_to_char(binary)
        result_string = ''.join(str)
    return result_string

# IP置换
def IP_change(bits):
    '''
    bits:一组64位的01比特字符串
    return：初始置换IP后64bit01序列
    '''
    ip_str = ""
    for i in data.IP:
        ip_str = ip_str + bits[i - 1]
    return ip_str

# 逆IP置换
def IP_INV_change(bits):
    '''
    bits:一组64位的01比特字符串
    return：初始置换IP后64bit01序列
    '''
    ip_str = ""
    for i in data.IP_INV:
        ip_str = ip_str + bits[i - 1]
    return ip_str

# 扩散置换函数 32->48
def E_change(bits):
    '''
    bits : 32bit01序列字符串
    return : 扩展置换E后的48bit01字符串
    '''
    e = ""
    for i in data.E:
        e = e + bits[i-1]
    return e

# S盒代替函数48->32
def S_change(bits):
    '''
    bits : 异或后的48bit01字符串
    return : 经过S盒之后32bit01字符串
    '''
    P_S32 = ''
    for i in range(8):
        temp = bits[i*6:(i+1)*6]
        row = int(temp[0] + temp[5], 2)
        col = int(temp[1:5], 2)
        num = bin(data.S_boxes[i][row * 16 + col])[2:]
        num = num.zfill(4)
        P_S32 = P_S32 + num
    return P_S32

# P置换
def P_change(bits):
    '''
    bits:一组64位的01比特字符串
    return：初始置换IP后64bit01序列
    '''
    ip_str = ""
    for i in data.P:
        # print(bits[i-1],i,sep = '-',end=' ')
        ip_str = ip_str + bits[i - 1]
    return ip_str

#两个xor
def xor(bits,ki):
    '''
    bits : 48bit01字符串 / 32bit01 F函数输出
    ki : 48bit01密钥序列 / 32bit01 Li
    return ：bits与ki异或运算得到的48bit01 / 32bit01
    '''
    bits_xor = ""
    for i in range(len(bits)):
       if bits[i] == ki[i]:
           bits_xor += '0'
       else:
           bits_xor += '1'
    return bits_xor

#秘钥64->56
def process_key(key):
    key2 = ''
    for i in range(len(key)):
        if (i+1)%8==0:
            continue
        else:
            key2 += key[i]
    return key2


def PC_1_change(bits):
    ip_str = ""
    for i in data.PC1:
        # print(bits[i-1],i,sep = '-',end=' ')
        ip_str = ip_str + bits[i - 1]

    return ip_str

#循环左移
def key_leftshift(key_str,num):
    '''
    key_str : 置换PC-1后的28bit01字符串
    return : 28bit01字符串左移num位后的结果
    '''
    left = key_str[num:28]
    left += key_str[0:num]
    return left

#置换选择2
def PC_2_change(key):
    '''
    key : 56bit移位后密钥01bit字符串
    return : 密钥置换PC-2后48bit序列字符串
    '''
    pc_2 = ""
    for i in data.PC2:
        pc_2 = pc_2 + key[i-1]
    return pc_2


def des_decrypt(key2,plaintext,test):

    # des.key_leftshift(key2,data.Rotated_Bits(i))
    # 左移
    key2_left28 = key2[0:28]
    key2_right28 = key2[28:]

    # print(len(key2_left28),len(key2_right28))
    key2_left28 = key_leftshift(key2_left28,data.Rotated_Bits[test])
    key2_right28 = key_leftshift(key2_right28,data.Rotated_Bits[test])
    key2 = key2_left28+key2_right28
    # print(len(key2))
    # 秘钥置换选择2
    key_choice =PC_2_change(key2)
    print(key_choice)

    # print('IP置换',plaintext_change_ip,len(plaintext_change_ip))
    #分成左右两部分 右侧移到下一论的左边 左侧进行F函数
    P_left32_i = plaintext[0:32]
    P_right32_i = plaintext[32:]

    # print('左秘钥 右秘钥',P_left32_i,P_right32_i)

    P_right48 = E_change(P_right32_i)
    # print('秘钥扩展',P_right48,len(P_right48))

    #少了一个xor/
    P_right48 = xor(P_right48, key_choice)

    P_S32 = S_change(P_right48)
    # print('S_boxs',P_S32,len(P_S32))

    #置换P
    P_S32 = P_change(P_S32)
    # print('P置换',P_S32, len(P_S32))

    # print('',len(P_S32),len(P_left32_i))

    P_right32_i_1 = xor(P_S32, P_left32_i)
    # print('xor异或2',P_right32_i_1,len(P_right32_i_1))

    text = P_right32_i+P_right32_i_1

    return key2,text

def write_file(result_str):
    try:
        fp = open('text.txt','w',encoding='utf-8')
        fp.write(result_str)
        fp.close()
    except:
        print("Write file error!")




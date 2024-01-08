import math
import data
import time

def read_file(filename):
    try:
        fp = open(filename,"r",encoding='utf-8')
        ciphertext = fp.read()
        fp.close()
        return ciphertext
    except:
        print("Open file error!")
        exit()

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


def divide_ciphertext(ciphertext):
    length = math.ceil(len(ciphertext)/8)
    N = ["" for i in range(length)]
    count = 0
    j = 0
    for i in range(len(ciphertext)):
        if count!=8:
            N[j] += char_to_binary(ciphertext[i])
            count += 1
        else:
            j +=1
            count=1
            N[j] += char_to_binary(ciphertext[i])
    if(length!= len(ciphertext)//8):
        padded_string = N[j].ljust(64,'0')
        N[-1] = padded_string
    return N


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

#3秘钥生成
def generate_key(key):
    '''
    key : 64bit01密钥序列
    return : 16轮的16个48bit01密钥列表按1-16顺序
    '''
    ## 置换选择1
    key_list = ["" for i in range(16)]
    key = PC_1_change(key) #置换PC_1
    # print(key,'key')
    key_left = key[0:28]
    key_right = key[28:]
    for i in range(len(data.Rotated_Bits)):
        ## 循环左移
        key_left = key_leftshift(key_left, data.Rotated_Bits[i])
        key_right = key_leftshift(key_right, data.Rotated_Bits[i])
        ## 置换选择2
        key_i = PC_2_change(key_left + key_right) #置换PC_2
        key_list[i] = key_i
        # print(key_left + key_right)
    return key_list

def IP_change(bits):
    '''
    bits:一组64位的01比特字符串
    return：初始置换IP后64bit01序列
    '''
    ip_str = ""
    for i in data.IP:
        ip_str = ip_str + bits[i - 1]
    return ip_str

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

def E_change(bits):
    '''
    bits : 32bit01序列字符串
    return : 扩展置换E后的48bit01字符串
    '''
    e = ""
    for i in data.E:
        e = e + bits[i-1]
    return e

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

def F(bits,ki):
    '''
    bits : 32bit 01 Ri输入
    ki : 48bit 第i轮密钥
    return : F函数输出32bit 01序列串
    '''
    bits = xor(E_change(bits),ki)
    bits = P_change(S_change(bits))
    return bits
def IP_INV_change(bits):
    '''
    bits:一组64位的01比特字符串
    return：初始置换IP后64bit01序列
    '''
    ip_str = ""
    for i in data.IP_INV:
        ip_str = ip_str + bits[i - 1]
    return ip_str

#将8位2进制数转换成字符
def bit_str(bits):
    '''
    bits :  01比特串(长度要是8的倍数)
    returns : 对应的字符
    '''
    temp = ""
    for i in range(len(bits)//8):
        temp += chr(int(bits[i*8:(i+1)*8],2))
    return temp

def write_file(result_str):
    try:
        fp = open('message.txt','w',encoding='utf-8')
        fp.write(result_str)
        fp.close()
    except:
        print("Write file error!")


def decryption():
    #密文获取
    filename = input("密文所在的文件位置： ")
    #秘钥获取
    key = key_to_binary()

    start_time = time.time()

    ciphertext = read_file(filename)
    # print(ciphertext)
    print("文本的长度为：",len(ciphertext))

    ##秘钥密文转01bit流
    # 消息拆分
    plain_bit= divide_ciphertext(ciphertext)
    ## 子秘钥生成
    key_list = generate_key(key)

    result_str = ''
    for x in plain_bit:
        ##IP置换
        bits = IP_change(x)
        L = bits[0:32]
        R = bits[32:]
        ##16抡加密
        for i in range(16):
            L_next = R
            R = xor(L,F(R,key_list[15-i]))
            L = L_next
        ##逆初始置换IP
        result_str += IP_INV_change( R + L)

    ##01bit转秘钥流 - 输出到文本文件text
    # result_str = 'aaaaaaaaaaaaaaaaa'
    result_str = bit_str(result_str)
    write_file(result_str)
    print(result_str)
    end_time = time.time()
    print("加密运行的时间是: ", end_time - start_time)
    # print(1)

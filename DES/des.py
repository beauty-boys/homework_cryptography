import data


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
    key = 'aaaaaaaa'
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




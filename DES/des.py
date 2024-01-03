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
    while True:
        key = input("秘钥是什么: ")
        if len(key)== data.len_key:
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


import data
import des
import math

if __name__ =="__main__":

    # 读取加密的文件（只含有加密的信息）
    filename = input("加密的文本内容在那个文件: ")
    ### 转成二进制流
    message = des.read_file(filename)
    text_plain = des.divide_message(message)

    # plaintext = "0110000101100001011000010110000101100001011000010110000101100001"#64位

    #字符串转01的比特流 返回的key是秘钥
    key = des.key_to_binary()

    # key = '1100001111000011110000111100001111000011110000111100001111000011'
    # key2 = des.PC_1_change(key)
    result_str = ''
    for plaintext in text_plain:
        # 秘钥置换选择1
        key2 = des.PC_1_change(key)

        #IP置换
        plaintext = des.IP_change(plaintext)

        #循环16轮
        for i in range(16):
            key2,plaintext = des.des_decrypt(key2,plaintext,int(i))
        #左右交换
        plaintext = plaintext[32:]+plaintext[0:32]
        #逆IP置换
        plaintext = des.IP_INV_change(plaintext)
        #01比特流转字符串
        plaintext = des.binary_to_plaintext(plaintext)
        result_str += plaintext
        print(plaintext)
    print(result_str)
    des.write_file(result_str)

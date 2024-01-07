import data
import des


if __name__ =="__main__":

    # plaintext = input("加密的文本内容是: ")

    plaintext = "0110000101100001011000010110000101100001011000010110000101100001"#64位
    #字符串转01的比特流 返回的key是秘钥
    key = des.key_to_binary()
    # key2 = des.process_key(key)
    # print(key,key2,sep='\n')
    # print(len(key2))
    #秘钥置换选择1
    # print(key)
    key = '1100001111000011110000111100001111000011110000111100001111000011'
    key2 = des.PC_1_change(key)
    # print(key2)

    # print(f'秘钥key2',key2,len(key2))
    #


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

    print(plaintext)

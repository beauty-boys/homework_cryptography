import data
import des


if __name__ =="__main__":

    plaintext = input("加密的文本内容是: ")

    #字符串转01的比特流 返回的key是秘钥
    key = des.key_to_binary()

    #01比特流转字符串
    plaintext = des.binary_to_plaintext(key)
    print(key,plaintext)

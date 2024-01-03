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
    key2 = des.PC_1_change(key)
    print(f'秘钥key2',key2,len(key2))

    #循环16轮
    for i in range(16):
        # des.key_leftshift(key2,data.Rotated_Bits(i))
        # 左移
        key2_left28 = key2[0:28]
        key2_right28 = key2[28:]
        print(len(key2_left28),len(key2_right28))
        key2_left28 = des.key_leftshift(key2_left28,2)
        key2_right28 = des.key_leftshift(key2_right28,2)
        key2 = key2_left28+key2_right28
        print(len(key2))
        # 秘钥置换选择2
        key_choice =des.PC_2_change(key2)

        #IP置换
        plaintext_change_ip = des.IP_change(plaintext)
        print('IP置换',plaintext_change_ip,len(plaintext_change_ip))
        #分成左右两部分 右侧移到下一论的左边 左侧进行F函数
        P_left32_i = plaintext_change_ip[0:32]
        P_right32_i = plaintext_change_ip[32:]

        print('左秘钥 右秘钥',P_left32_i,P_right32_i)

        P_right48 = des.E_change(P_right32_i)
        print('秘钥扩展',P_right48,len(P_right48))

        #少了一个xor/
        P_right48 = des.xor(P_right48, key_choice)

        P_S32 = des.S_change(P_right48)
        print('S_boxs',P_S32,len(P_S32))

        #置换P
        P_S32 = des.P_change(P_S32)
        print('P置换',P_S32, len(P_S32))

        # print('',len(P_S32),len(P_left32_i))

        P_right32_i_1 = des.xor(P_S32, P_left32_i)
        print('xor异或2',P_right32_i_1,len(P_right32_i_1))


    #01比特流转字符串
    plaintext = des.binary_to_plaintext(key)
    # print(key,plaintext)

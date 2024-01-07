


def read_file(filename):
    try:
        fp = open(filename,"r",encoding='utf-8')
        ciphertext = fp.read()
        fp.close()
        return ciphertext
    except:
        print("Open file error!")



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
    ciphertext = read_file(filename)
    print(ciphertext)
    #秘钥获取
    key = input("设置的秘钥是什么")
    print(key)
    ##秘钥密文转01bit流

    # 消息拆分
    ## 子秘钥生成
    ## 置换选择1
    ## 循环左移
    ## 置换选择2
    ##16抡加密

    ##IP置换

    ## E-table

    ## xor与子密钥

    ## S-box选择

    ##P置换

    ##逆初始置换IP

    ##左右交换

    ##01bit转秘钥流 - 输出到文本文件text
    result_str = ''
    write_file(result_str)
    print(1)

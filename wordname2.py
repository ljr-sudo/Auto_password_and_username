import random
import string

def GetRandomString(user_min,user_max,pre,userNum):
    letters1 = string.ascii_letters
    ranLen = random.randint(user_min,user_max)
    str = ""
    for i in range(1,3):
        str = str+userNum+letters1
        GetStr = ''.join(random.sample(str,ranLen))
        GetStr = pre+userNum+GetStr
    return GetStr

if __name__ == '__main__':
    user_min = int(input('请输入用户名的最小长度'))
    user_max = int(input('请输入用户名的最大长度'))
    pre = input('请输入前缀字符串')
    userNum = int(input('请输入需要构造的用户数量'))
    for i in range(1,userNum):
        userNum = ''
        str1 = GetRandomString(user_min,user_max,pre,userNum)
        print(str1)

"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
1.将数字num转换成数组，累加处理 

2.数学思想找到其规律，判断除以9，如果小于9，则返回本身，如果整除9，则返回9，如果不能整除9，则返回除9后的余数。
"""
class Solution:
    def addDigits(self,num:int)->int:
        while num>=10:
            list_num=list(map(int,str(num)))
            res=0
            for i in range(len(list_num)):
                res=res+list_num[i]
            num=res
        return  num

    # if num == 0:
    #         return 0
    #     elif num%9 == 0:
    #         return 9
    #     else:
    #         return num%9
result=Solution()
print(result.addDigits(38))
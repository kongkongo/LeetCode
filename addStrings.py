"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
提示：
num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return (intString(num1))+(intString(num2))
def intString(num:str)->str:
        s=0
        l=len(num)-1
        for i in range(len(num)):
            s=s+int(num[i])*pow(10,l)
            l-=1
        return s



result=Solution()
print(result.addStrings("55","44"))
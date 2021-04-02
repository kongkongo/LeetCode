"""
二进制其求和
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        return bin(a+b)[2:]


result=Solution()
print(result.addBinary("1010","1011"))
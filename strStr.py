# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
class  Solution:
    def  strStr(self,haystack:str,needle:str):
        """
        :type  haystack:str
        :type   needle:str
        :rtype:int
        """
        l,n=len(needle),len(haystack)
        for  start  in  range(n-l+1):
            if  haystack[start:start+l]==needle:
                return  start
        return  -1
        

solution=Solution
result=solution.strStr(haystack = "hello", needle = "ll")
print(result)

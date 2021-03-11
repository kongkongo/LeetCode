"""  电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 
提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""

class Solution:
    def letterCombinations(self, digits: str):
        
        ##先定义数字和字母的字典
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        ##特殊条件判断
        for  i  in  digits:
            if  res:
                temp=[]
                for j   in  res:
                    for  k  in  dic[i]:
                        temp.append(j+k)
                res=temp
            else:
                for j  in  dic[i]:
                    res.append(j)
        return  res

digits="23"
solution=Solution()
data=solution.letterCombinations(digits)
print(data)

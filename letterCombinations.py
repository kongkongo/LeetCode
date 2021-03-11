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

"""外观数列
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person='1'
        for i in range(1,n):
            next_person,num,count="",prev_person[0],1
            for j in range(1,len(prev_person)):
                 if prev_person[j] == num:
                    count += 1
                 else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person
    # def countAndSay(self, n):
    #     s = '1'
    #     for i in range(n-1):    #第一层，计算好需要的项数，上面已经初始化了第一项
    #         s = self.cns(s)     #不断更新上一项
    #     return s
    # def cns(self, string):
    #     res = ''
    #     string += '#'           #加上#之后，即使遍历到字符串末尾，i+1不会溢出，省去了溢出判断的步骤
    #     cnt = 1
    #     for i in range(len(string)-1):  #第二层，遍历当前项
    #         if string[i] == string[i+1]:#计算是否有重复字符
    #             cnt += 1
    #             continue
    #         else:
    #             res += str(cnt) + string[i] #数量和字符返回
    #             cnt = 1
    #     return res


if __name__=="__main__":    
    result=Solution()
    print(result.countAndSay(5))
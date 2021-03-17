# 杨辉三角
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 示例:

# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if  numRows==1:
            triangle=[[1]]
            return  triangle
        triangle=[[1],[1,1]]
        for i in range(2,numRows):        #已经给出前两行，所以求剩余行
            cur=[1]                                             #定义每行第一个元素
            pre=triangle[i-1]                           #上一行
            for j   in  range(i-1):                          #算几次
                cur.append(pre[j]+pre[j+1])
            cur.append(1)
            triangle.append(cur)
        return  triangle

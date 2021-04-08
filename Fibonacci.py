class Solution:
    def  fib(self,n:int)->int:
        """递归函数
        输出斐波那契数列
         """
        if  n<=1:
            return  n
        else:
            return  (self.fib(n-1)+self.fib(n-2))

# 获取用户输入
nterms = int(input("您要输出几项? "))
fibT=Solution()
# 检查输入的数字是否正确
if nterms <= 0:
   print("输入正数")
else:
   print("斐波那契数列:")


# 上面方法超时，需取模计算

def  fib(n:int)->int:
    a,b = 0,1
    for i in range(n):#和i是多少其实没关系，n是几就向前走几步
        c=a;a=b;b=c+b
        # a , b = b , a+b
    return a % 1000000007


if  "__main__":
    n=10
    print(fib(n))



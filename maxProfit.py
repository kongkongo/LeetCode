"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = start = 0
        for i in range(1, len(prices)):
            # 当最小价格小于start指针切换至当前
            if prices[i] - prices[start] < 0:
                start = i
            # 每次比较最优抛售价格
            ret = max(prices[i] - prices[start], ret)
        return ret

result=Solution()
print(result.maxProfit([1,2]))
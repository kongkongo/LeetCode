from typing import List
class Solution(object):
    def removeDuplicates(self, nums:List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=0      #定义一个指针变量
        for j in range(1,len(nums)):     #遍历数组
            if nums[j]!=nums[flag]:      # 若指针指向的元素与当前遍历数组的元素不同
                flag+=1                 #指针后移动一位
                nums[flag]=nums[j]
        print(nums)
        print(flag+1)   
        return flag+1


if __name__ == '__main__':
    result = Solution()
    result.removeDuplicates([1,1,2,1])
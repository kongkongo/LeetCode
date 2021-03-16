# 同时对两棵树进行先序遍历
# 情况一：有一个节点为None，返回False
# 情况二：两个节点都是None，返回True
# 情况三：两个节点都不是None，如果val不等，返回False；反之，进入下层子树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 先序遍历
        if (p is None and q is not None) or (p is not None and q is None):  # 有一个节点为None
            return False
        if p is None and q is None:     # 两个节点都是None
            return True
    
        else:   # 两个节点都不是None
            if p.val != q.val:  
                return False
    
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return True

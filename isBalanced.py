"""给定一个二叉树，判断它是否是高度平衡的二叉树。
从底至顶（提前阻断）:
思路是对二叉树做先序遍历，从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。
算法流程：recur(root):
递归返回值：
当节点root 左 / 右子树的高度差 < 2<2 ：则返回以节点root为根节点的子树的最大高度，即节点 root 的左右子树中最大高度加 11 （ max(left, right) + 1 ）；
当节点root 左 / 右子树的高度差 \geq 2≥2 ：则返回 -1−1 ，代表 此子树不是平衡树 。
递归终止条件：
当越过叶子节点时，返回高度 00 ；
当左（右）子树高度 left== -1 时，代表此子树的 左（右）子树 不是平衡树，因此直接返回 -1−1 ；
isBalanced(root) ：
返回值： 若 recur(root) != 1 ，则说明此树平衡，返回 truetrue ； 否则返回 falsefalse 。""" 
class   TreeNode:
    def    __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class   Solution(object):
    def     isBalanced(self,root:TreeNode)->bool:
        return  True  if self.recur(root)!=-1 else  False

    def     recur(self,root):
        if  not    root:
            return  0
        left=self.recur(root.left)
        if   left==-1:
            return  -1
        right=self.recur(root.right)
        if  right==-1:
            return  -1
        if  abs(left-right)<2:
            return  max(left,right)+1
        else:
            return  



a=Solution()
null=""
print(a.isBalanced(TreeNode([1,null,2,null,3])))    

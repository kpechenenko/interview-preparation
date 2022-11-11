class Solution:
    def recursive(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if (left == None) ^ (right == None):
            return False
        if (left == None) and (right == None):
            return True
        if left.val == right.val:
            return self.recursive(left.left, right.right) and self.recursive(left.right, right.left)
        else:
            return False


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root.left, root.right)

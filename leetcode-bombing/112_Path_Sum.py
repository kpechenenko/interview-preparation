class Solution:
    def recursive(self, cur_sum: int, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False
        cur_sum += root.val
        if (cur_sum == target_sum) and not root.left and not root.right:
            return True
        return self.recursive(cur_sum, root.left, target_sum) or self.recursive(cur_sum, root.right, target_sum)


    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        return self.recursive(0, root, target_sum)


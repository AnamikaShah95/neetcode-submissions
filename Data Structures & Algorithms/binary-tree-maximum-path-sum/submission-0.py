class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
            
            # Max gain from left and right subtrees (ignore negative sums)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Price of a new path with the current node as the highest root
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            max_sum = max(max_sum, current_path_sum)
            
            # For recursion, return the max gain if we continue through this node
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return max_sum
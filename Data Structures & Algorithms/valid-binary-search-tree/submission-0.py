class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # An empty tree is a valid BST
            if not node:
                return True
                
            # The current node's value must sit strictly between low and high boundaries
            if not (low < node.val < high):
                return False
                
            # For the left child, update the upper bound to node.val
            # For the right child, update the lower bound to node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
                    
        return validate(root, float('-inf'), float('inf'))
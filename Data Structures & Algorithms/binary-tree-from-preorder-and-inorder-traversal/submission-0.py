class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0
        
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left > right:
                return None
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            root_idx = inorder_map[root_val]
            
            root.left = array_to_tree(left, root_idx - 1)
            root.right = array_to_tree(root_idx + 1, right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
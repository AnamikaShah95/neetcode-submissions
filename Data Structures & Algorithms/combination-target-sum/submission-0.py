class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, cur, total):
            # Base Case: found a valid combination
            if total == target:
                res.append(cur.copy())
                return
            
            # Base Case: out of bounds or exceeded target sum
            if i >= len(nums) or total > target:
                return
            
            # Decision 1: Include nums[i]
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            
            # Decision 2: Don't include nums[i] (Backtrack)
            cur.pop()
            backtrack(i + 1, cur, total)
            
        backtrack(0, [], 0)
        return res
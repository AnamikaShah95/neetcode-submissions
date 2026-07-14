class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(idx, current, total):
            if total == target:
                res.append(current.copy())
                return
            if total > target or idx >= len(candidates):
                return

            current.append(candidates[idx])
            backtrack(idx + 1, current, total + candidates[idx])
            current.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            backtrack(idx + 1, current, total)

        backtrack(0, [], 0)
        return res
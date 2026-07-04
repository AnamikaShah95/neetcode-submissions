class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l=0
        r=rows*cols-1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid//cols][mid%cols] == target:
                return True
            elif matrix[mid//cols][mid%cols] > target:
                r = mid-1
            else:
                l = mid+1
        return False        


        
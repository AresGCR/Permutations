class Solution:
    def permutation(self,nums,l,r,pts):
        if(l==r):
            pts.append(nums.copy())
            return
        for i in range(l,r+1):
            nums[i],nums[l] =nums[l],nums[i]
            self.permutation(nums,l+1,r,pts)
            nums[i],nums[l] =nums[l],nums[i]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        r=len(nums)-1
        self.permutation(nums,0,r,permutations)
        return permutations

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult, r_mult = 1, 1
        l_arr, r_arr = [0]*len(nums), [0]*len(nums)

        for i in range(len(nums)):
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
            
        return [l*r for l, r in zip(l_arr, r_arr)]
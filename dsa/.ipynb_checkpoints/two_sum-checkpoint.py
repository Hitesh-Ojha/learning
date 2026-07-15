

from narwhals import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out_list = []
        ln = len(nums)
        for i in range(ln):
            for j in range (i+1,ln):
                sum1 = nums[i] + nums[j] 
                if sum1 == target:
                    out_list.append(i)
                    out_list.append(j) 
                    return out_list
arr = [2,7,11,15]
sum1 = Solution()
result = sum1.twoSum(arr, 9)
print(result)
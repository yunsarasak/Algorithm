class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        num_max = max(nums)
        #print(num_max)
        answer = num_max * k
        answer += (k * (k-1)) // 2

        return answer
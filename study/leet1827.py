class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0

        # 두번째 원소부터 끝까지
        for i in range(1, len(nums)):
            # 자기 앞거 +1 에서 자신을 뺀만큼 더하기
            if nums[i-1] < nums[i]:
                continue
            
            sub = nums[i-1] - nums[i]
            answer += sub + 1
            nums[i] += sub + 1
        
        return answer
            
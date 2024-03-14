from typing import List

# def get_sum(_list : List[int]):
#     ret_sum = 0
#     for i in _list:
#         ret_sum += i
        
#     return ret_sum

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)

        num_sorted = sorted(nums)

        # list_accumlated = list()

        answer = list()

        for i in range(m):
            # list_accumlated.clear()
            partial_sum = 0
            count = 0
            
            for j in range(n):
                if partial_sum + num_sorted[j] > queries[i]:
                    break
                # if get_sum(list_accumlated) + num_sorted[j] > queries[i]:
                #     break

                #list_accumlated.append(num_sorted[j])
                partial_sum += num_sorted[j]
                count+=1

                # if get_sum(list_accumlated) < queries[i]:
                #     continue
                # else:
                #     break
                if partial_sum < queries[i]:
                    continue
                else:
                    break
            answer.append(count)


        
        return answer
        

my_answer = Solution()
nums = [4,5,2,1]
queries = [3,10,21]
answer_list = my_answer.answerQueries( nums, queries)

print(answer_list)
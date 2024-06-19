#https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

#어느 한 숫자가 자리수가 세자리가 되지않도록 최소 2자리 * 2자리 수를 만들어야함.
#네자리 수를 오름차순으로 정렬해서
#10자리를 가장 작은수를 사용해서 더하면 된다.
#( 0도 10의 자리에 올 수 있음.)

class Solution:
    def minimumSum(self, num: int) -> int:
        num_string = str(num)
        sorted(num_string)

        print(num_string)
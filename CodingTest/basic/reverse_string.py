# 문자열 뒤집기
# https://leetcode.com/problems/reverse-string/
from typing import List

# 풀이 1: 투 포인터를 이용한 스왑
def reverseString1(s: List[str]) -> List[str]:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# 풀이 2: 파이썬다운 방식
def reverseString2(s: list) -> list:
    s.reverse()
    return s

import timeit
example_list = ["h","e","l","l","o"]

answer1 = reverseString1(s=example_list)
print(f"answer 1 : {answer1}")

# example case
execution_time_1 = timeit.timeit(lambda: reverseString1(example_list), number=10) 
print(f"풀이 1: 투 포인터를 이용한 스왑: {execution_time_1 / 10:.6f}초") 

answer2 = reverseString2(s=example_list)
print(f"answer 2 : {answer2}")

execution_time_2 = timeit.timeit(lambda: reverseString2(example_list), number=10) 
print(f"풀이 2: 파이썬다운 방식: {execution_time_2 / 10:.6f}초") 
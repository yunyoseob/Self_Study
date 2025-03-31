# 유효한 팰린드롬
# https://leetcode.com/problems/valid-palindrome/description/
import timeit
import collections
from collections import deque

# 풀이 1: 리스트로 변환
def isPalindrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

# 풀이 2: 데크 자료형을 이용한 최적화
def isPalindrome2(s: str) -> bool:
    strs: deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


import re
# 풀이 3: 슬라이싱 사용
def isPalindrome3(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1] # 슬라이싱

example_str1 = "A man, a plan, a canal: Panama"

# example case
execution_time_1 = timeit.timeit(lambda: isPalindrome1(example_str1), number=10) 
print(f"풀이 1: 리스트로 변환: {execution_time_1 / 10:.6f}초") 

execution_time_2 = timeit.timeit(lambda: isPalindrome2(example_str1), number=10) 
print(f"풀이 2: 데크 자료형을 이용한 최적화: {execution_time_2 / 10:.6f}초") 

execution_time_3 = timeit.timeit(lambda: isPalindrome3(example_str1), number=10) 
print(f"풀이 3: 슬라이싱 사용: {execution_time_3 / 10:.6f}초") 
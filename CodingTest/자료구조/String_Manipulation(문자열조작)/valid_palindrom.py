# 파이썬 알고리즘 인터뷰
# 2023-01-17
# Q01 : 유효한 팰린드롬 (뒤로 뒤집어도 똑같은 단어 또는 문장)
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다
# "A man, a plan, a canal: Panama" => true
# "race a car" => false

# 리스트로 접근해보기
class Solution:
    def isPalindrom(self, s: str)->bool:
        strs=[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        print(f"strs >>> : {strs}")
        # strs >>> : ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']

        # 팰린드롬 여부 판병
        while len(strs) >1:
            if strs.pop(0) != strs.pop():
                return False
        return True

s=Solution()
answer=s.isPalindrom("A man, a plan, a canal: Panama")
print(answer)
# True
# strs 리스트에서 pop(0)을 뽑기 위해 n개의 개수만큼 이동해서 a를 가져오고 (pop(0) => O(n))
# strs 리스트에서 pop()을 뽑아서 비교함 (pop() => O(1)) 


# Deque로 접근해보기
# Deque는 Double-Ended Queue의 줄임말로, 글자 그대로 양쪽 끝을
# 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형이다.
import time
from collections import deque

class Solution:
    def isPalindrom(self, s: str)->bool:
        # 자료형 데크로 선언
        strs= deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
    
        # 팰린드롬 여부 판병
        while len(strs) >1:
            if strs.popleft() != strs.pop():
                return False
        return True
s=Solution()
answer=s.isPalindrom("A man, a plan, a canal: Panama")
print(answer)
# True
# strs 리스트에서 popleft(), pop()이 O(1)

# 슬라이싱 사용
import re

class Solution:
    def isPalindrom(self, s: str)->bool:
        # 자료형 데크로 선언
        strs= s.lower()
        print(f"strs >>> : {strs}")
        # strs >>> : a man, a plan, a canal: panama

        s=re.sub('[^a-z0-9]','',s)
        print(f"s >>> : {s}")
        # s >>> : manaplanacanalanama
        return s==s[::1]
    
s=Solution()
answer=s.isPalindrom("A man, a plan, a canal: Panama")
print(answer)
# 정규표현식을 사용함으로써 
# for char in s:
#     if char.isalnum():
# 매번 문자열에 있는 문자들이 공백인지 여부를 점검할 필요가 없어졌다.
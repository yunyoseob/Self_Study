# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903
# 단어 s의 가운데 글자를 반환하는 함수,
#  solution을 만들어 보세요. 
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

string_1='abcdef'
len(string_1)//2
num_1=(len(string_1)//2)-1
num_2=(len(string_1)//2)
s1[2]+s1[3]

s1=list(string_1)
s1
s1[2]

def solution(s):
    s1=list(s)
    if len(s)%2==1:
        num=(len(s)//2)
        answer=s1[num]
    else:
        num_1=(len(s)//2)-1
        num_2=(len(s)//2)
        answer_1=s1[num_1]
        answer_2=s1[num_2]
        answer=answer_1+answer_2
    return answer

s="abcde"

solution(s)

s="qwer"

solution(s)
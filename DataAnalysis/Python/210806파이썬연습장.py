# 연습문제 2-1
apple=5
orange=3
total=apple+orange
print(total)


# 2번
kor=100
eng=88
math=94
avg=(kor+eng+math)/3
print(avg)

# 2번 다르게 풀어보기
import pandas as pd
score=pd.DataFrame(columns=['kor','eng','math'])
score=score.append({'kor':100, 'eng':88,'math':94}, ignore_index=True)
score=score.transpose()
score.mean()

# 문자열 반복
str_ex='문자열반복'
print(str_ex*10)

# 소문자 변환
str_lower="I Want Python"
print(str_lower.lower())

# 대문자 변환
str_upper="i want python"
print(str_upper.upper())

# count 
ex_sentence="I want Pyhon. Becuase I do not like R program and SQL"
ex_sentence.count('a')

# append 
list_1=['소주','맥주','막걸리']
list_1.append('동동주')
list_1

#insert
list_1.insert(0,'원하는주종')
list_1

#remove
list_1.remove('동동주')
list_1

#pop: 가장 마지막 요소를 꺼내옴.
list_1.pop()
list_1

# dictionary
dict_1={'key':'value'}
dict_1

dict_3={'홍길동':100,'홍계월':200}
dict_3['슈퍼맨']=300
dict_3

# dictionary 요소 수정
dict_3['홍길동']=1
dict_3

# dictionary 추가/삭제/수정
del dict_3['슈퍼맨']
dict_3

#key, value
dict_3['베트맨']=250
dict_3.keys() # key 접근
dict_3.values() # values 접근
dict_3.items() # key,values 같이 접근

# set (집합)
set_1=set()
set_2=set('Hello')
set_3=set([1,2,3])
set_4={3,5,'hi'}

print(set_2)
print(set_3)

set_5={1,2,3,4}
set_6={3,4,5,6}
set_5&set_6 #교집합
set_5|set_6 #합집합

# Formatting
# 1st method
"오늘은 %d월, %d일입니다."%(8,6)
"오늘은 8월 %s째주입니다."%('첫')

# 2nd method
"오늘은 {}요일".format('금')

# 3rd method 
# 다른 포맷팅과는 달리 표현식을 지원함
month=8
today=6
f'오늘은 {month}월, {today}일이다.'
f'내일은 {month}월, {today+1}일이다.'
f'다음달은 {month+1}월이다.'

#연습문제 5-1
a=34
b=4

if b%a >3:
    print('실패')
elif b%a==3:
    print("무승부")
else:
    print("성공")

# while (반복문)
i=1

while i<=10:
    if i%2==0:
        print(i)
    i+=1

i=90

while i:
    i+=1
    if i==100:
        print(f"축하합니다. {i}번째 방문자입니다.")
        break
    print("감사합니다. 이벤트가 종료되었습니다.")

i=0

while i<11:
    i+=1
    if i==6:
        continue
    if i%2==0:
        print(i)

# Toy example
sum=0
for i in range(0,11):
    sum=sum+i
    i+=1

print(sum)

#연습문제 3
x=[3,6,9,20,-7,5]

[x*10 for x in x]

# 구구단(반복문)
for i in range(1,10):
    print(f'{i}단')
    for j in range(1,10):
        print(i*j)

# 구구단(함수)
def gugu(num):
    for i in range(1,10):
        print(f'{num}*{i}={num*i}')

gugu(3)

# args
def test(*args):
    print(args)

test(1,2,3,4,5)

def add(**kwargs):
    print(kwargs)

add(a=1, b=2, c=3)

# add_all 함수
def add_all(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum

add_all(1,2,3,4,5,6,7,8,9,10)

# global 사용하기
# 함수 안의 변수를 밖에서도 쓸 수 있음
a=1

def myfunction():
    global a
    a+=1
    print(a)

myfunction()
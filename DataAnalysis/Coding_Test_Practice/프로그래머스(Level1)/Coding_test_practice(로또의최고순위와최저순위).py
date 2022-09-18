# 로또의 최소 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

# 로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 
# 6개를 찍어서 맞히는 대표적인 복권입니다. 
# 아래는 로또의 순위를 정하는 방식입니다.
#로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 
# 하지만, 민우의 동생이 로또에 낙서를 하여, 
# 일부 번호를 알아볼 수 없게 되었습니다. 
# 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 
# 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
#알아볼 수 없는 번호를 0으로 표기하기로 하고, 
# 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 
# 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 
# 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.
# 민우가 구매한 로또 번호를 담은 배열 lottos, 
# 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 
# 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 
# 담아서 return 하도록 solution 함수를 완성해주세요.

# 예시
# 민우의 복권, 여기서 0은 동생이 장난쳐서 구분 불가능한 숫자
lottos=[31,1,0,0,31,25]
win_nums=[31,10,45,1,6,19]

print(f"최소 겹치는 숫자는 {len(set(lottos)&set(win_nums))} 입니다.")
# 최소 겹치는 숫자는 2 입니다.

dontknow=[x for x in lottos if x==0]
print(f"민우동생이 아니였다면, 최대 {len(dontknow)}개 더 맞출 수 있습니다.")
# 민우동생이 아니였다면, 최대 2개 더 맞출 수 있습니다.

def solution(lottos, win_nums):
    answer=[]
    same=[]
    minimum=len(set(lottos)&set(win_nums))
    same.append(minimum)
    dontknow=[x for x in lottos if x==0]
    maximum=minimum+len(dontknow)
    same.append(maximum)
    for i in range(1,-1,-1):
        if same[i]<2:
            answer.append(6)
        elif same[i]==2:
            answer.append(5)
        elif same[i]==3:
            answer.append(4)
        elif same[i]==4:
            answer.append(3)
        elif same[i]==5:
            answer.append(2)
        else:
            answer.append(1)
    return answer

# 예시
lottos_1=[44,1,0,0,31,25]
win_nums_1=[31,10,45,1,6,19]

result=solution(lottos_1, win_nums_1)
result
# [3, 5]
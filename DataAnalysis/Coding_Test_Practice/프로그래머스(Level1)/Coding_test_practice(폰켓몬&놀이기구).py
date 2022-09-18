# 폰켓몬
# 당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 
# 홍 박사님의 연구실에 도착했습니다. 
# 홍 박사님은 당신에게 자신의 연구실에 있는 
# 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
# 홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다. 
# 따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다. 
# 예를 들어 연구실에 총 4마리의 폰켓몬이 있고, 
# 각 폰켓몬의 종류 번호가 [3번, 1번, 2번, 3번]이라면 
# 이는 3번 폰켓몬 두 마리, 1번 폰켓몬 한 마리, 2번 폰켓몬 
# 한 마리가 있음을 나타냅니다. 이때, 4마리의 폰켓몬 중 2마리를 
# 고르는 방법은 다음과 같이 6가지가 있습니다.

# 첫 번째(3번), 두 번째(1번) 폰켓몬을 선택
# 첫 번째(3번), 세 번째(2번) 폰켓몬을 선택
# 첫 번째(3번), 네 번째(3번) 폰켓몬을 선택 
# 두 번째(1번), 세 번째(2번) 폰켓몬을 선택
# 두 번째(1번), 네 번째(3번) 폰켓몬을 선택
# 세 번째(2번), 네 번째(3번) 폰켓몬을 선택
# 이때, 첫 번째(3번) 폰켓몬과 네 번째(3번) 폰켓몬을 
# 선택하는 방법은 한 종류(3번 폰켓몬 두 마리)의 폰켓몬만 가질 수 있지만, 
# 다른 방법들은 모두 두 종류의 폰켓몬을 가질 수 있습니다.
#  따라서 위 예시에서 가질 수 있는 폰켓몬 종류 수의 최댓값은 2가 됩니다.
# 당신은 최대한 다양한 종류의 폰켓몬을 
# 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 
# 포함해서 N/2마리를 선택하려 합니다. 
# N마리 폰켓몬의 종류 번호가 담긴 배열
#  nums가 매개변수로 주어질 때, N/2마리의 
# 폰켓몬을 선택하는 방법 중, 가장 많은 종류의
#  폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 
# 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.

nums=[3,3,3,2,2,4]

len(nums)//2

# combination 함수 만들어 보기 aCb라고 할 때, b=a//2인 경우에만 해당
# combination 함수 nCn//2
def combination_func(nums):
    answer=0
    num=len(nums)
    choice=len(nums)//2
    num_list=[]
    choice_list=[]
    for i in range(num, num-choice,-1):
        num_list.append(i)
    for j in range(1,choice+1):
        choice_list.append(j)
    mul=1
    for a in num_list:
        mul=mul*a
    cho=1
    for b in choice_list:
        cho=cho*b
    case=mul/cho
    return case

# 경우의 수 함수짜기
nums_1=[3,1,2,3]
# 이 경우에는 (1,2), (1,3), (2,3) 이렇게 최대 2마리만 챙길 수 있음.
combination_func(nums_1)
# 경우의 수는 총 6가지

nums_2=[3,3,3,2,2,4]
# 이 경우에는 (2,3,4) 이렇게 최대 3마리 챙길 수 있음.
combination_func(nums_2)
# 경우의 수는 총 20가지

nums_3=[3,3,3,2,2,2]
# 이 경우에는 (2,3) 이렇게 최대 2마리만 챙길 수 있음.
combination_func(nums_3)
# 경우의 수는 총 20가지

# 문제 풀이: set을 활용하면 매우 쉽게 풀 수 있음.
def solution(nums):
    answer=0
    number=len(set(nums))
    choice=len(nums)//2
    if number < choice:
        return number
    else:
        return choice


# 프로그래머스 위클리 챌린지 1주차
# https://programmers.co.kr/learn/courses/30/lessons/82612

# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
# 이 놀이기구의 원래 이용료는 price원인데, 놀이기구를 N번째
# 이용한다면 원래 이용료의 N배를 받기로 했습니다.
# 즉, 처음 이용료가 100이였다면, 2번째에는 200, 3번째에는
# 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액
# 에서 얼마가 모자라는지를 return하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.

# 제한사항
# 놀이기구의 이용료 price: 1<=price<=2500, price는 자연수
# 처음 가지고 있던 금액 money: 1<=money<=1000000000, money는 자연수
# 놀이기구의 이용 횟수 count: 1<=count<=2500, count는 자연수

# 제한 사항 없을 때는 이렇게 쉽게 풀면 된다.

def solution(price, money, count):
    now_price=0
    for i in range(0, count+1):
        now_price=now_price+(i*price)
        r_price=int(money)-int(now_price)
        if r_price >=0:
            result=0                                
        else:
            result=-1*r_price

    return result

solution(10000,10000, 1)

# 제한 사항 추가
def solution(price, money, count):
    if 1<=price<=25000:
        if 1<=money<=1000000000:
            if 1<=count<=2500:
                if type(price)==int:
                    if type(money)==int:
                        if type(count)==int:
                            now_price=0
                            for i in range(0, count+1):
                                now_price=now_price+(i*price)
                                r_price=int(money)-int(now_price)
                                if r_price >=0:
                                    result=0                                
                                else:
                                    result=-1*r_price
                        else:
                            result="Error"
                    else:
                        result="Error"
                else:
                    result="Error"
            else:
                result="Error"
        else:
            result="Error"
    else:
        result="Error"
    return result

solution(10000,10000, 1)
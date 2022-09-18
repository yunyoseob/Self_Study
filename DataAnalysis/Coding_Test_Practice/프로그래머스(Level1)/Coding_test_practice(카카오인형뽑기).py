# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061
# 게임개발자인 "죠르디"는 크레인 인형뽑기 가게를 모바일 게임으로 만드려고 합니다.
# "죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이
# 게임 로직에 반영하려고 합니다.
# 게임 화면은 "1*1"크기의 칸들로 이루어진 "N*N" 크기의 정사각
# 격자이며 위쪽에는 크레인이 있고, 오른쪽에는 바구니가 있습니다.
# 각 격자 칸에는 다양한 인형이 들어 있으며, 인형이 없는 칸은 빈칸입니다.
# 모든 인형은 "1*1" 크기의 격자 한 칸을 차지하며, 격자의
# 가장 아래칸부터 차곡차곡 쌓여있습니다.

# 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는
# 인형을 집어 올릴 수 있습니다.
# 집어 올린 인형은 바구니에 쌓이게 되는데, 이 때 바구니의 가장
# 아래 칸부터 인형이 순서대로 쌓이게 됩니다.
# 만일 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면
# 두 인형은 터뜨려지면서, 바구니에서 사라지게 됩니다.
# 크레인 작동 시 인형이 집어지지 않는 경우는 없으나
# 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
# 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다.
# 게임 화면의 격자의 상태가 담긴 2차원 배열  board와 인형을 잡기 위해 크레인을 작동시킨
# 위치가 담긴 배열 moves가 매개변수로 주어질 때,
# 크레인을 모두 작동시킨 후, 터뜨려져 사라진 인형의 개수를 return하도록
# solution 함수를 완성해주세요.

# 제한사항
# board 배열은 2차원 배열로 크기는 "5*5"이상, "30*30"이하입니다.
# board의 각 칸에는 0이상 100이하인 정수가 담겨있습니다.
# 0은 빈 칸을 나타냅니다.
# 1~100의 각 숫자는 각기 다른 인형의 모양을 의미하며
# 같은 숫자는 같은 모양의 인형을 타나냅니다.
# moves 배열의 크기는 1이상 1000이하 입니다.
# moves 배열의 각 원소들의 값은 1이상이며, board 배열의 가로 크기 이하인
# 자연수입니다.

# 입출력 예
board=[[0,0,0,0,0],
       [0,0,1,0,3],
       [0,2,5,0,1],
       [4,2,4,4,2],
       [3,5,1,3,1]]

moves=[1,5,3,5,1,2,1,4]

result=4

board[3][0]
# 첫 번째 네모칸이 행
# 두 번째 네모칸이 열
# board[3][0]은 4행 1열
# moves[i]가 board[n][i-1]의 i-1자리로 가야함.
# 가령, moves[i]가 1이라면, board[n][0]에서 뽑아야함.

board[2][1]
moves[0]
# 1
len(moves)
len(board)

answer=0
basket=[]
# moves[0]==1
board[0][0]
# 0
board[1][0]
# 0
board[2][0]
# 0
board[3][0]
# 4

# 이럴 경우 board[3][0]에 있는 4라는 인형이 basket에 가야함.
basket.append(board[3][0])
basket
# [4]

# 첫 번째 인형을 뽑아보자.
num=len(board)
print(num)
# 5
moves[0]
# 1
moves[1]
# 5

i=1
basket=[]
for j in range(0, num):
    if board[j][i-1]!=0:
        basket.append(board[j][i-1])
        board[j][i-1]=0 #바구니에 옮긴 인형은 빼줘야함.
        break
    else:
        j+=1    
basket
# 4

###################
def solution(board, moves):
    answer=0
    basket=[]
    num=len(board)
    for i in moves:
        for j in range(0, num):
            if board[j][i-1]!=0:
                basket.append(board[j][i-1])
                board[j][i-1]=0 #바구니에 옮긴 인형은 빼줘야함.
                break
        while True:
            if len(basket)>1 and basket[-1]==basket[-2]:
                basket.pop(-1)
                basket.pop(-1)
                answer=answer+2
            else:
                break

    return answer
    
board=[[0,0,0,0,0],
       [0,0,1,0,3],
       [0,2,5,0,1],
       [4,2,4,4,2],
       [3,5,1,3,1]]

moves=[1,5,3,5,1,2,1,4]

result=solution(board, moves)
result
# 4
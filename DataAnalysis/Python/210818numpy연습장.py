# 210818 numpy 연습장(python)
import numpy as np

# numpy 기초
A=[1,2,3,4]
a=np.array(A)
type(a)
print(a[0])

B=[5,6,7,8]
b=np.array(B)
c=a+b
c

10-c
# 원소별로 10에서 차감

c.shape

C=[[1,2,3],[4,5,6]]
c=np.array(C)
A=([100],[200])
a=np.array(A)

d=c+a
print(d)

#ndarray_asarray()
# np.assaray: Convert the input to an array
a=[1,2,3,4,5]
type(a)

b=np.array(a)
type(b)

c=np.asarray(a)
type(c)

arr=np.array([10,20,30,40])
arr.shape
arr.size
arr.ndim
# 1

arr2=np.array([[10,20,30,40],[50,60,70,80]])
arr2.ndim
# 2 

arr3=np.array([[[10,20,30],[40,50,60],[70,80,90]],[[10,20,30],[40,50,60],[70,80,90]]])
arr3
arr3.shape
arr3.ndim
# 3

# 배열 생성함수
np.zeros((5))
type(np.zeros((5))[0])
# <class 'numpy.float64'>
np.zeros((5), dtype=np.int8)
type(np.zeros((5), dtype=np.int8)[0])
# <class 'numpy.int8'>
np.ones((3,3))

np.full((4),5)
# array([5, 5, 5, 5])

np.empty((2,3), dtype=np.float64)
# array([[1.60218491e-306, 1.11261095e-306, 8.06639778e-308],
#       [6.23038336e-307, 1.50201822e-307, 3.56043053e-307]])


np.identity(5, dtype=int)
#array([[1, 0, 0, 0, 0],
#       [0, 1, 0, 0, 0],
#       [0, 0, 1, 0, 0],
#       [0, 0, 0, 1, 0],
#       [0, 0, 0, 0, 1]])

np.eye(5, dtype=int)

arr1=np.array([[1,2,3,1],[2,4,5,6]])
arr2=np.ones_like(arr1)
arr2
#array([[1, 1, 1, 1],
#       [1, 1, 1, 1]])

np.arange(5)
np.arange(-3,3)
# array([-3, -2, -1,  0,  1,  2])

np.arange(3,50,3)
# array([ 3,  6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) 

np.linspace(0,10,5)
# array([ 0. ,  2.5,  5. ,  7.5, 10. ])

# 배열결합함수
# Hstack, concatenate(axis=0)
# 두 배열을 왼쪽에서 오른쪽으로 붙이기
a=np.array([1,2,3])
b=np.array([4,5,6])
np.hstack([a,b])

np.concatenate((a,b), axis=0)


# Vstack, concatenate(axis=1)
# 두 배열을 위에서 아래로 붙이기
np.vstack([a,b])

c=np.array([[0,1,2],[3,4,5]])
d=np.array([[6,7,8],[9,10,11]])

np.concatenate((c,d), axis=1)

import matplotlib.pyplot as plt
data=np.random.rand(10000)
# (0,1) 범위의 균등분포에서 표본을 추출
plt.plot(data)
plt.show()

data=np.random.randn(10000)
# 표준편차 1, 평균값 0인 정규분포에서 표본을 추출
plt.plot(data)
plt.show()


# 연습 문제 1) 로또 번호 생성기를 만드세요.
line=np.arange(4)

for i, x in enumerate(line):
    x=np.random.randint(1,100,6)
    print(f"{i+1}.로또 번호: {x}")


# Flatten # (1,-1) 행렬로 바꿔줌
arr=np.identity(5, dtype=int)
#array([[1, 0, 0, 0, 0],
#       [0, 1, 0, 0, 0],
#       [0, 0, 1, 0, 0],
#       [0, 0, 0, 1, 0],
#       [0, 0, 0, 0, 1]])
arr.flatten()
#array([1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,      
#       0, 0, 1])


arr=np.identity(5, dtype=int)
arr=arr*5
arr=arr+5
arr[0][1]=6
arr[0][2]=6
arr.reshape(-1,1)
arr.transpose()


# Swapaxes
# np.swapaxes는 직관적으로 축을 선정함
a=np.arange(3).reshape(1,3)
print(a)
a.ndim
# [[0 1 2]]
# 2
y=np.swapaxes(a,0,1) # 0은 가장 높은 차수의 축. (2차원)
# 1은 그 다음 높은 차수의 축.(1차원)
# 원소의 행과 열을 바꾸라는 것
print(y)
#array([[0],
#       [1],
#       [2]])
y.ndim
# 2

# Swapaxes 2차원 사례
a=np.identity(10, dtype=int).reshape(-1,1)
print(a)
a.shape
# (100,1)
a.ndim
y=np.swapaxes(a,0,1)
y.shape
# (1,100)

# Swapaxes 3차원 사례
a=np.identity(10, dtype=int).reshape(-1,2,50)
print(a)
a.shape
# (1, 2, 50))
a.ndim
# 3
y=np.swapaxes(a,0,1)
print(y)
y.shape
# (2,1,50)
y.ndim
# 3

# T operation
x=np.arange(6).reshape((-1,3))
x
x.T

# 연습문제 2) 0~20까지의 숫자를 배열로 만든 다음에
# arr1에는 짝수, arr2는 홀수가 들어간 배열을 출력해보자.

arr=np.arange(21)
arr

arr1=[]
for i in range(0,20,2):
    arr1.append(arr[i])

arr1=np.array(arr1)
arr1

arr2=[]
for i in range(1,21,2):
    arr2.append(arr[i])

arr2=np.array(arr2)
arr2

# 연습문제 3) 주어진 배열을 이용하여 아래와 같은 결과를 만들어보자.
arr=np.arange(30).reshape(2,3,5)
arr

arr.flatten()

arr.reshape(6,5).transpose()

# ndarray vs list
# ndarray
arr1d=np.arange(8)
arr_part=arr1d
arr_part[1:]=-1
arr1d
# array([ 0, -1, -1, -1, -1, -1, -1, -1])
# 원본 데이터가 변경되어 있음.

arr1d=np.arange(8)
arr_part=arr1d.copy()
arr_part[1:]=-1
arr1d
# array([0, 1, 2, 3, 4, 5, 6, 7])
# copy를 쓰면 원본 데이터가 변하지 않음.

#list
lst=list(range(6))
lst_part=lst[2:]
lst_part[3]=100
lst_part
# [2, 3, 4, 100]
lst
# [0, 1, 2, 3, 4, 5]
# 원본 데이터가 변하지 않음.


# Boolean indexing
# 불리언 배열: 불리언 값으로 이루어진 배열
arr=np.array([True, False])
arr.dtype
# dtype('bool')

# 불리언 인덱싱: 불리언 배열을 이용한 인덱싱
# - True에 해당되는 위치에 있는 값만을 반환
arr=np.array([0,1,2,3,4], int)
arr[[True, False, True, False, True]]
# array([0, 2, 4])
# Ture에 해당되는 위치에 있는 값만을 반환

arr=np.array([10,20,30,40,50,60], int)
arr%3==0
# array([False, False,  True, False, False,  True])

arr[arr%3==0]
# array([30, 60])

arr2=arr[arr%20==0]
arr2
# array([20, 40, 60])

# Fancy indexing
arr2d=np.arange(20).reshape(4,5)
arr2d[[0,2]]
#array([[ 0,  1,  2,  3,  4],
#       [10, 11, 12, 13, 14]])

arr2d
#array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14],
#       [15, 16, 17, 18, 19]])
arr2d[[0,1], [4]]
# array([4, 9])

# 연습문제 3)
# 1번: 주어진 배열을 이용하여 아래와 같은 결과를 만들어보자.
arr=np.arange(24)
arr
#array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,    
#       17, 18, 19, 20, 21, 22, 23])
arr.reshape(2,4,3)
#array([[[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11]],
#
#       [[12, 13, 14],
#        [15, 16, 17],
#        [18, 19, 20],
#        [21, 22, 23]]])

# 2번: 주어진 배열과 불리언 인덱싱을 이용하여 아래와 같은 결과를 만들어보자.
arr=np.arange(30).reshape(3,2,5)
arr

a=arr[arr<10]
b=arr[arr>19]

np.vstack([a,b]).reshape(2,2,5)
#array([[[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9]],
#
#       [[20, 21, 22, 23, 24],
#        [25, 26, 27, 28, 29]]])

arr3=arr.copy()
arr3=arr3.flatten()
len(arr3) #30
arr3[29]

arr4=[]

for i in range(0,30):
    if arr3[i]<10:
        arr4.append(arr3[i])
    elif arr3[i]>=20:
        arr4.append(arr3[i])
    else:
        pass

np.array(arr4).reshape(2,2,5)
#array([[[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9]],
#
#       [[20, 21, 22, 23, 24],
#        [25, 26, 27, 28, 29]]])

#  유니버셜 함수
arr=np.arange(-3,3).reshape(3,-1)
arr
#array([[-3, -2],
#       [-1,  0],
#       [ 1,  2]])

np.exp(arr) #각 원수에 지수 e^x 계산
#array([[0.04978707, 0.13533528],
#       [0.36787944, 1.        ],
#       [2.71828183, 7.3890561 ]])

arr.dtype
# dtype('int32')
np.abs(arr) # 각 원소의 절대값
np.abs(arr).dtype
# dtype('int32')
np.fabs(arr) # 각 원소의 절대값
np.fabs(arr).dtype
# dtype('float64')

a=np.arange(30)
###
b=[pow(x, 2) for x in a]
b=np.array(b)
b
### 위의 과정을 단 한 줄로 쉽게 하는 방법

np.square(a) # 각 원소들의 제곱

###
c=[pow(x, 0.5) for x in b]
c=np.array(c)
c
### 위의 과정을 단 한 줄로 쉽게 하는 방법
np.sqrt(b) #각 원소들의 제곱근

a=list(range(100))
a

np.log(a)
a=np.array(a)
a[np.log10(a)==1]
# array([10])

np.log2(a)
a[np.log2(a)==4]
# array([16])

a[np.log1p(a)<2]
# array([0, 1, 2, 3, 4, 5, 6])
# np.log1p=log(1+x)

b=np.arange(-10,10)
np.sign(b)
# 부호를 알려줌.

np.ceil(2.9)
# 3.0
# 각 원소의 값보다 같거나 큰 정수 중 가장 작은 값

np.floor(3.1)
# 3.0
# 각 원소의 값보다 같거나 작은 정수 중 가장 큰 값

b=np.arange(-3,3,0.5)
print(b)
# [-3.  -2.5 -2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5  2.   2.5]
np.rint(b)
# array([-3., -2., -2., -2., -1., -0.,  0.,  0.,  1.,  2.,  2.,  2.])
# 각 원소의 소수자리를 반올림

np.modf(b)
# (array([-0. , -0.5, -0. , -0.5, -0. , -0.5,  0. ,  0.5,  0. ,  0.5,  0. ,     
#        0.5]), array([-3., -2., -2., -1., -1., -0.,  0.,  0.,  1.,  1.,  2.,  
#2.]))
# 각 원소의 몫과 나머지를 각각의 배열로 변환

b.shape
b[:5]='NaN'
b
#array([ nan,  nan,  nan,  nan,  nan, -0.5,  0. ,  0.5,  1. ,  1.5,  2. ,      
#        2.5])
np.isnan(b)
#array([ True,  True,  True,  True,  True, False, False, False, False,
#       False, False, False])
# 각 원소가 NaN인지 아닌지, 불리언 배열로 변환

b=np.arange(-3,3,0.5)
np.isfinite(b)
# 각 원소가 유한한지, 무한한지, 불리언 배열로 변환

np.isinf(b)
# 각 원소가 유한한지, 무한한지, 불리언 배열로 변환

import matplotlib.pyplot as plt
start=0
end=4*np.pi
dx=1000
x=np.linspace(start, end, dx)

# 일반 삼각함수
# sin 함수 
plt.plot(x, np.sin(x))
plt.show()
# 0->1->0->-1->0->1

# cos함수
plt.plot(x, np.cos(x))
plt.show()
# 1->0->-1->0->1->0

# tan 함수
plt.plot(x, np.tan(x))
plt.show()
# 우상향후 우하향 후 우상향 반복

# 쌍곡삼각함수
# sinh
plt.plot(x, np.sinh(x))
plt.show()
# 지수함수처럼 우상향

# cosh
plt.plot(x, np.cosh(x))
plt.show()
# 지수함수처럼 우상향

# tanh
plt.plot(x, np.tanh(x))
plt.show()

#역삼각함수
# arcsin
plt.plot(x, np.arcsin(x))
plt.show()
# 급격히 우상향후 그대로

# arcsinh
plt.plot(x, np.arcsinh(x))
plt.show()
# 우상향 곡선

# arccos
plt.plot(x, np.arccos(x))
plt.show()
# 우하향 곡선

# arccosh
plt.plot(x, np.arccosh(x))
plt.show()
# 우상향 곡선

# arctan
plt.plot(x, np.arctan(x))
plt.show()
# 우상향 곡선

# arctanh
plt.plot(x, np.arctanh(x))
plt.show()
# 우상향 곡선


# 로그함수 우상향 곡선
plt.plot(x, np.log(x))
plt.show()

# 지수함수 우상향곡선
plt.plot(x, np.exp(x))
plt.show()

# 이항 유니버셜 함수
arr1=np.arange(8).reshape(2,-1)
arr2=np.arange(-40,40,10).reshape(2,-1)
print(arr1)
#[[0 1 2 3]
# [4 5 6 7]]
print(arr2)
#[[-40 -30 -20 -10]
# [  0  10  20  30]]

np.maximum(arr1, arr2)
# array([[ 0,  1,  2,  3],
#       [ 4, 10, 20, 30]])

np.subtract(arr2, arr1) #  뺄셈
#array([[-40, -31, -22, -13],
#       [ -4,   5,  14,  23]])

np.multiply(arr1, arr2) # 원소곱셈 #주의: 행렬곱 아님
arr1.shape #(2,4)
arr2.shape # (2,4) 
#array([[  0, -30, -40, -30],
#       [  0,  50, 120, 210]])

arr1.sum() # 총 합
# 28

np.sum(arr1)
#28
 
 
arr1.mean()
np.mean(arr1)
 # 3.5
arr1
#array([[0, 1, 2, 3],
#       [4, 5, 6, 7]])
arr1.mean(axis=0)
# array([2., 3., 4., 5.])
arr1.mean(axis=1)
# array([1.5, 5.5])

np.var(arr1) # 분산
# 5.25

np.std(arr1) # 표준편차
# 2.29

arr=np.array([True, False, True])
arr.any()
# True
# 하나 이상 True면, True 반환

arr.all()
# False
# 모든 값이 True여야 True 반환

# np.where x if 조건 else  y 의 벡터화 버전
xarr=np.array([100,200,300,400]) # if에 해당
yarr=np.array([1,2,3,4])  #else에 해당
cond=np.array([True, False, True, False])

result=np.where(cond, xarr, yarr)
# cond: if~~~else~~ xarr: if일 때, yarr: else일 때
result
# array([100,   2, 300,   4])
# True일때는 xarr에 있는 값을,
# False일때는 yarr에 있는 값을 대입하여 반환

np.where(xarr>200, max(xarr), 0)
# array([  0,   0, 400, 400])
np.where(xarr%3==0, 1, 0)
# array([0, 0, 1, 0])

# sort
np.random.seed(10)
arr=np.random.randint(1,100, size=10)
arr
# array([10, 16, 65, 29, 90, 94, 30,  9, 74,  1])
arr.sort()
arr
# array([ 1,  9, 10, 16, 29, 30, 65, 74, 90, 94])

np.random.seed(20)
arr=np.random.randint(1,100, size=10)
arr
# array([91, 16, 96, 29, 91, 10, 21, 76, 23, 72])
np.sort(arr)
# array([10, 16, 21, 23, 29, 72, 76, 91, 91, 96])
arr
# array([91, 16, 96, 29, 91, 10, 21, 76, 23, 72])
# 전에 arr.sort()와는 다르게 원본이 변하지 않음

-np.sort(-arr)
# array([96, 91, 91, 76, 72, 29, 23, 21, 16, 10])
# 내림차순, -1를 한 번만 쓰면 원소에 -1이 곱해져버림.

# 선형대수
# 단위 행렬(Identity Matrix, Unit Matrix)
# 대각 원소가 1이고 나머지가 모두 0인 n차 정방행렬
Identity=np.eye(4)
print(Identity)

Identity=np.eye(2,3)
print(Identity)

# 대각 행렬
# 대각 성분 이외의 모든 성분이 모두 '0'인 n차 정방행렬
x=np.arange(9).reshape(3,-1)
print(x)
# [[0 1 2]
# [3 4 5]
# [6 7 8]]
np.diag(x) # 대각 원소
np.diag(np.diag(x))
#array([[0, 0, 0],
#       [0, 4, 0],
#       [0, 0, 8]])

a=np.arange(4).reshape(-1,2)
print(a)
#[[0 1]
# [2 3]]

a*a
#array([[0, 1],
#       [4, 9]])

np.dot(a,a)
#array([[ 2,  3],
#       [ 6, 11]])

a.dot(a)
#array([[ 2,  3],
#       [ 6, 11]])

# 행렬곱
a=np.random.randint(-3,3,10).reshape(2,5)
b=np.random.randint(0,5,15).reshape(5,3)
a.shape, b.shape
# ((2, 5), (5, 3))

ab=np.matmul(a,b)
print(ab.shape)
# (2,3)
print(ab)
#[[ -3 -15 -15]
# [ -9  -6   1]]

c=np.arange(24).reshape(2,3,4)
d=np.arange(2*4*5).reshape(2,4,5)
c.shape, d.shape
# ((2, 3, 4), (2, 4, 5))

arr=np.matmul(c,d)
arr.shape
# (2,3,5)
# 3차원 이상의 경우에는 마지막 2개 축으로 이루어진 행렬을
# 다른 축들에 따라 쌓는 것으로 파악
# 따라서 마지막 2개의 차원이 행렬곱을 할 수 있으면 matmul 가능


# 대각합
b=np.arange(16).reshape(4,-1)
print(b)
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]]

np.trace(b)
# 30

c=np.arange(27).reshape(3,3,3)
print(c)
#[[[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]]
#
# [[ 9 10 11]
#  [12 13 14]
#  [15 16 17]]
#
# [[18 19 20]
#  [21 22 23]
#  [24 25 26]]]
np.trace(c)
# array([36, 39, 42])

# 행렬식(Matrix Determinat)
# Determimat
# 역행렬이 존재하는지 여부를 확인하는 방법으로 행렬식
# (determinat, 줄여서 det)이라는 지표를 사용함.
# 이 행렬식이 '0'이 아니면 역행렬이 존재하고,
# 이 행렬식이 '0'이면 역행력이 존재하지 않습니다.

d=np.array([[1,2],[3,4]])
np.linalg.det(d)
# -2.0000000000000004

d=np.array([[1,2],[2,4]])
np.linalg.det(d)
# 0.0

# Inverse of a matrix (역행렬)
# 역행렬은 n차 정방행렬 Amn 과의 곱이 항등행렬 또는 단위행렬이 되는
# n차 정방행렬을 말합니다.
# A*B와 B*A 모두 순서에 상관없이 곱했을 때, 단위행렬이 나오는
# n차 정방행렬이 있다면, 역행렬이 존재함.
# 역행렬은 가우스 소거법(Gauss-Jordan elimination method) 혹은
# 여인수(Cofactor methd)로 풀 수 있음.

a=np.array(range(4)).reshape(2,-1)
print(a)
#[[0 1]
# [2 3]]

a_inv=np.linalg.inv(a)
a_inv
#array([[-1.5,  0.5],
#       [ 1. ,  0. ]])

# 유도 과정
adbc=1/((a[0][0]*a[1][1])-(a[0][1]*a[1][0]))
adbc
b=a.copy()
a=b[0][0]
d=b[1][1]
b[0][0]=d
b[1][1]=a

b[0][1]=-1*b[0][1]
b[1][0]=-1*b[1][0]
b=b*adbc
b
#array([[-1.5,  0.5],
#       [ 1. ,  0. ]])

a_inv
#array([[-1.5,  0.5],
#       [ 1. ,  0. ]])

b==a_inv
#array([[ True,  True],
#       [ True,  True]])
#####


# 선형대수_고유값(Eigenvalue), 고유벡터(Eigenvector)
# 정방 행렬 A에 대하여 Ax=lambda x (상수 lambda)가 성립하는
# 0이 아닌 벡터 x가 존재할 때, 상수 lambda를 행렬 A의 고유값(eigenvalue),
# x를 이에 대응하는 고유 벡터(eigenvector)라고 함.

e=np.array([[4,2],[3,5]])
print(e)
#[[4 2]
# [3 5]]

w,v=np.linalg.eig(e)
print(w)
# [2. 7.]

print(v)
#[[-0.70710678 -0.5547002 ]
# [ 0.70710678 -0.83205029]]

# 선형대수_ 특이값 분해(Singular Value Decomposition)
# 특이값 분해는 고유값 분해(eigen decomposition)처럼 행렬을
# 대각화하는 한 방법으로서, 정방행렬뿐만 아니라 모든 m*n행렬에 대해
# 적용 가능합니다. 특이값 분해는 차원축소, 데이터 압축 등에 사용할 수 
# 있습니다.

A=np.array([[3,6],[2,3],[0,0],[0,0]])
print(A)
#[[3 6]
# [2 3]
# [0 0]
# [0 0]]
A.shape
# (4, 2)

u,s,vh=np.linalg.svd(A)
u.shape
# (4, 4)
print(u)
#[[-0.8816746  -0.47185793  0.          0.        ]
# [-0.47185793  0.8816746   0.          0.        ]
# [ 0.          0.          1.          0.        ]
# [ 0.          0.          0.          1.        ]]
print(s)
# [7.60555128 0.39444872]
print(vh)
# [[-0.47185793 -0.8816746 ]
# [ 0.8816746  -0.47185793]]
# ADsP 제 4과목 데이터 분석
# 제 1장 R 기초와 데이터 마트

# 벡터
x=c(1,10,24,40)
y=c("사과","오렌지","바나나")
xy=c(x,y)
xy

# matrix
mx <- matrix(c(1,2,3,4,5,6), ncol=2)
mx

r1=c(10,10)

rbind(mx, r1) # 행추가

c1=c(20,20,20)

cbind(mx, c1) #  열 추가

# 데이터 프레임 만들기

income=c(100,200,150,300,900)
car=c("kia","hyundai","kia","toyota","lexus")
marriage=c(FALSE, FALSE, FALSE, TRUE, TRUE)
mydat=data.frame(income, car, marriage)
mydat

# 외부 데이터 불러오기
# header=T : csv파일의 첫 줄을 변수명으로 지정
# sep="," : 데이터가 쉼표로 구분된 데이터 파일임을 지정

# 타이타닉 데이터 불러오기
# https://www.kaggle.com/c/titanic

df_train <- read.csv('C:/Users/bella/Desktop/SelfStudy/ADsP&R/train.csv', header=T)

df_test <- read.csv('C:/Users/bella/Desktop/SelfStudy/ADsP&R/test.csv', header=T)

df_gender_submission <- read.csv('C:/Users/bella/Desktop/SelfStudy/ADsP&R/gender_submission.csv', header=T)

# R의 기초 함수
# 수열 생성하기

rep(1, 3) # 첫 번째 인수를 두 번째 인수만큼 반복하는 숫자 벡터 생성
seq(1, 3) # 첫 인수부터 두 번째 인수까지 1씩 증가하는 수열
1:3 # 같은 의미
seq(1, 11, 2) # 공차가 2
seq(1, 11, length=8) # 8등분

a=c(2,7,3)
a

# 파이썬에서 a.transpose()는 R에서 t(a)로 표현렬(전치행렬)
t(a)

A=a%*%t(a) # %*%는 행렬곱을 의미
A

# 역핼렬
mx=matrix(c(23,41,12,35,67,1,24,7,53), nrow=3)
mx

solve(mx) # solve는 역행렬

# 행렬 원소 곱
5*mx

# 평균, 분산, 표준편차
df_train[is.na(df_train)]<-0 #0으로 결측치 채움

mean(df_train$Age)
# train 데이터의 나이의 평균 값
# 23.79929

var(df_train$Age)
# train 데이터의 나이의 분산 값
# 309.6218

sd(df_train$Age)
# train 데이터의 표준편차 값
# 17.59607

sum(df_train$Age)
# train 데이터의 합
# 21205.17

median(df_train$Age)
# train데이터의 최빈값
# 24

log(df_train$Age)
# 로그 변환

#  이 외에도 cov(공분산), cor(상관계수)를 구할 수 있다.


# index 파이썬과 차이점
b= c("a","b","c","d","e")
b

# 파이썬은 시작점이 0, R은 시작점이 1
b[2]

# 파이썬은 앞에 음수를 붙이면 뒤에서 부터 count, R은 해당값 제외하고 # 출력

b[-4]

# 파이썬은 마지막 범위에 +1, R은 해당X
b[c(2,3)]

# 반복문과 조건문
a=c()
for (i in 1:9){a[i]=i*i}

a

# 1부터 100까지 합
isum=0

for (i in 1:100){isum=isum+i}
isum
# 5050

x=1

while(x<5){x=x+1
print(x)}


# 조건문
Statscore=1:100

for (i in 1:100){if (Statscore[i]>=20)
  Statscore[i]=100
else Statscore[i]=0}

Statscore

# 함수
addto=function(a){
  isum=0
  for (i in 1:a){
    isum=isum+i
    }
   print(isum)}

addto(100)

addto(50)


# paste: 문자열들 사이에 구분자 삽입 기능
# substr: 특정 문자열 추출 기능 

# 파이썬에 astype이 있다면 R에는 as
# as.data.frame(x)
# as.list(x)
# as.matrix(x)
# as.vector(x)
# as.factor(x)
# Sys.Date(): 현재 날짜를 반환
# as.Date(): 날짜 객체로 변환

# 시각화 그림
plot(df_train$Age)
hist(df_train$Age)
boxplot(df_train$Age)

# 앞 부분 만 보기
head(df_train, 10)
#변수명 보기
names(df_train)
#"PassengerId" "Survived"    "Pclass"      "Name"       
# "Sex"         "Age"         "SibSp"       "Parch"      
# "Ticket"      "Fare"        "Cabin"       "Embarked"  

# sqldf를 이용한 데이터 분석
install.packages('sqldf')
library(sqldf)

sqldf("select*from df_train")

# plyr (데이터 처리 기능)
# d=데이터 프레임(data.frame)
# a=배열(array)
# I=리스트(list)

# 결측치 처리와 이상값 탐색
sum(is.na(df_test))
# 87 개의 결측치

df_test[is.na(df_test)]<-0

names(df_train)
boxplot(df_train$Parch)
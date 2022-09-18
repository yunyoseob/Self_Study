# ADsP 제 4과목 데이터 분석
# 제 2장 통계분석
# 모집단: 우리가 아는 전체
# 표본: 일부분만 조사
# 표본추출방법: 단순랜덤추출법, 계통추출법, 집략추출법, 층화추출법
# 단순랜덤추출법: 랜덤으로 추출
# 계통추출법: n개의 구간으로 나누어 추출
# 집락추출법: cluster한 뒤, 원소들에게 일련번호를 부여후 추출
# 층화추출법: 각 계층을 고루 대표할 수 있는 표본 추출
# 집락추출법 vs 층화추출법:
# 층화추출법은 집단 내 동질, 집단 간 차이 이질
# 집락추출법은 집단 내 이질, 집단 간 차이 동질
# 확률
# 배반사건: 교집합이 공집합인 사건
# 독립사건: P(A 교집합 B)=P(A)P(B)

# iris 데이터 불러오기
data(iris)
names(iris)
#"Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width" 
# "Species"

summary(iris)

head(iris)

mean(iris$Sepal.Length)
median(iris$Sepal.Length)
sd(iris$Sepal.Length)
var(iris$Sepal.Length)
quantile(iris$Sepal.Length)


#회귀분석
# 회귀분석: 하나나 그 이상의 변수들이 또다른 변수에 미치는 영향에 대해 추론할 수 있는 통계기법

# 단순 회귀분석 예쩨
# 쌍으로 묶인 관찰들인 두 벡터 x와 y를 생성하고,
# x와 y사이에 선형관계가 있다고 가정하고,
# lm() 함수를 이용해 단순선형회귀분석을 해보자

set.seed(2)
x=runif(10,0,11) # runif는 난수 생성
y=2+93*x+rnorm(10,0,0.2) #rnorm 정규분포를 따르는 난수 생성
dfrm=data.frame(x,y)
dfrm
#x        y
#2.033705 191.1610
#7.726114 720.6702
#6.306590 588.4649
#1.848571 174.3140
#10.382233 967.5199
#10.378225 967.2584
#1.420749 134.3260
#9.167937 854.5396
#5.148204 480.5750
#6.049821 564.9898

lm(y~x, data = dfrm)
#Coefficients:
#  (Intercept)      x  
#   2.213       92.979  
# 2.213은 beta0, x는 beta1

# 다중선형회귀 예제
# 여러개의 독립변수(u,v,w)와 하나의 반응변수(y)를
# 생성하고, 이들 간에 선형관계가 있다고
# 생각하며, 데이터에 다중선형회귀를 실시해보자.

set.seed(2)
u=runif(10,0,11)
v=runif(10,11,20)
w=runif(10,1,30)

y=3+0.1*u+2*v-3*w+rnorm(10,0,0.1)
dfrm=data.frame(y,u,v,w)
dfrm

m <- lm(y~u+v+w)
m
#Coefficients:
#  (Intercept)            u            v            w  
#3.0417       0.1232       1.9890      -2.9978  

summary(m)
# 결정계수, F통계량, 잔차의 표준오차 등 주요통계량 정보 
# 출력 가능
#Call:
#  lm(formula = y ~ u + v + w)

#Residuals:
#  Min        1Q    Median        3Q       Max 
#-0.188562 -0.058632 -0.002013  0.080024  0.143757 

#Coefficients:
#  Estimate Std. Error  t value Pr(>|t|)    
#(Intercept)  3.041653   0.264808   11.486 2.62e-05 ***
#  u            0.123173   0.012841    9.592 7.34e-05 ***
#  v            1.989017   0.016586  119.923 2.27e-11 ***
#  w           -2.997816   0.005421 -552.981 2.36e-15 ***
#  ---
#  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ ##.1 ‘ ’ 1

#Residual standard error: 0.1303 on 6 degrees of freedom
#Multiple R-squared:      1,	Adjusted R-squared:      1 
#F-statistic: 1.038e+05 on 3 and 6 DF,  p-value: 1.564e-14


# 예제 cars 데이터
data(cars)
head(cars)

# spped2 칼럼 만들어주기
speed2 <- cars$speed^2
cars <- cbind(speed2, cars)
head(cars)

# 회귀분석 적용
m=lm(dist~speed+speed2, data=cars)
m
summary(m)


# 예제 다음과 같은 데이터세트를 적절한
# 회귀모형에 적합한 회귀모형을 찾으시오.

# 예제 데이터 생성
x<-c(1,2,3,4,5,6,7,8,9)
y<-c(5,3,2,3,4,6,10,12,18)
df1<-data.frame(x,y)
df1
plot(df1)

# 산점도를 봤을 때, 2차식이 필요한 것처름 보임

x2<-x^2
x2
df2<-cbind(x2,df1)
df2

# df1과 df2 다항회귀분석 해보기
### df1
lm(y~x, data=df1)
summary(lm(y~x, data=df1))
plot(lm(y~x, data=df1))

### df2
lm(y~x+x2, data=df2)
summary(lm(y~x+x2, data=df2))
plot(lm(y~x+x2, data=df2))


# 최적회귀방정식의 선택: 설명변수의 선택
# 모든 가능한 조합의 회귀분석
# 단계적 변수선택
# 전진선택법, 후진제거법, 단계별 방법

# 예제
# 다음과 같은 데이터가 있다. Y를 반응변수로 하고,
# X1, X2, X3, X4를 설명변수로 하는 선형회귀 모형을
# 고려하고, 후진제거법을 이용하여 변수를 선택하시오.

X1<-c(7,1,11,11,7,11,3,1,2,21,1,11,10)
X2<-c(26,29,56,31,52,55,71,31,54,47,40,66,68)
X3<-c(6,15,8,8,6,9,17,22,18,4,23,9,8)
X4<-c(60,52,40,47,33,22,6,44,22,26,34,12,12)
Y<-c(78.5,74.3,104.3,87.6,95.9,109.2,102.7,72.5,93.1,115.9,83.8,113.3,109.4)

df <- data.frame(X1,X2,X3,X4,Y)
head(df)

a<-lm(Y~X1+X2+X3+X4, data=df)
a
summary(a)

#Coefficients:
#  Estimate Std. Error t value Pr(>|t|)    
#(Intercept)  58.5885    14.8221   3.953 0.004220 ** 
#  X1            1.5966     0.2504   6.375 0.000215 ***
#  X2            0.5542     0.1481   3.742 0.005687 ** 
#  X3            0.1321     0.2493   0.530 0.610555    
#X4           -0.1053     0.1445  -0.729 0.487018 거

# X3의 p-value가 제일 높으므로 제거
b<-lm(Y~X1+X2+X4, data=df)
b
summary(b)
# 수정 R계수가 더 높아짐가
# 그러나 X4의 경우 p-value가 0.05 초고

c<-lm(Y~X1+X2, data=df)
c
summary(c)
# p-value가 모두 0.05미만
# 변수 제거 Stop

# 꿀팁
# step(lm(종속변수~설명변수, 데이터세트), score=list(lower=~1, upper=~설명변수), direction="변수선택방법") 함수로 변수를 쉽게 선택 할 수 있다.
# direction= forward, backward, both

step(lm(Y ~1,df),scope=list(lower=~1, upper=~X1+X2+X3+X4), direction = "forward")

#tep:  AIC=24.62
#Y ~ X2 + X1 + X4
#
#Df Sum of Sq    RSS    AIC
#<none>              46.700 24.624
#+ X3    1    1.5837 45.117 26.176
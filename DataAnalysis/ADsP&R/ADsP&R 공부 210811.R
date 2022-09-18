# ADsP 제 4과목 데이터 분석
# 제 3절 다변량 분석

install.packages("Hmisc")
library(Hmisc)
data(mtcars)
head(mtcars)

drat <- mtcars$drat
disp <- mtcars$disp

plot(drat,disp)
cor(drat, disp)
# -0.7로 음의 상관관계를 가짐.

# 피어슨 상관계수 확인 해보기
rcorr(as.matrix(mtcars), type='pearson')
# rcorr 함수는 모든 변수들 사이의 상관계수와 함께
# 가설 H0: rho =0 에 대한 p-값을 출력한다.

cov(mtcars)


# 스피어만 상관계수 확인 해보기기
rcorr(as.matrix(mtcars), type="spearman")

# 예제: 다음은 국어, 수학, 영어, 과학 점수를 
# 데이터 프레임 형식으로 만든 데이터 세트다.

korean <- c(85,75,65,78,59,60,90,100,99,91,70)
math <- c(80,60,75,40,50,64,70,78,90,98,50)
english <- c(80,70,69,79,80,95,98,97,67,80,59)
science <- c(90,100,50,80,67,89,60,79,89,80,100)
test <- data.frame(korean, math, english, science)
test

# 스피어만 상관분석

rcorr(as.matrix(test), type="spearman")

# 다차원 척도법
# R: euridist -> 도시 사이의 거리를 매핑한 자료

data(eurodist)

head(eurodist)

eurodist

loc <- cmdscale(eurodist)

x <- loc[,1]
y <- loc[,2]

plot(x,y,type='n', main='eurodist')
text(x,y,rownames(loc), cex=0.8)
abline(v=0, h=0)
# cmdscale 함수: 각 도시의 상대적 위치를 도식화
# 할 수 있는 X, Y 좌표를 계산하고 그래프로 표현
# 이처럼 각 개체에 대한 특정 변수들의 
# 관측치는 없더라도 개체 간의
# 유사성에 대한 자료를 사용하여 
# 산점도를 그릴 수 있다.

# 주성분 분석
# USArrests 예시
# USArrests: 미국의 50개 주의 인구 10만명 당 살인, 
# 폭행, 강간으로 인한 체포의 수와
# 도시 인구의 비율을 포함하고 있다.

library(datasets)
data("USArrests")
summary(USArrests)

head(USArrests)


fit <- princomp(USArrests, cor=TRUE)
# 주성분분석 실시

summary(fit)
# 4개의 주성분의 표준편차, 분산의 비율 등
#Importance of components:
#  Comp.1    Comp.2    Comp.3
#Standard deviation     1.5748783 0.9948694 0.5971291
#Proportion of Variance 0.6200604 0.2474413 0.0891408
#Cumulative Proportion  0.6200604 0.8675017 0.9566425
#Comp.4
#Standard deviation     0.41644938
#Proportion of Variance 0.04335752
#Cumulative Proportion  1.00000000

# Proportion of Variance는 n번째 주성분 하나가 전체의 
# 몇 %를 설명하고 있는지,
# Cumulative Proportion은 이들의 누적 


loadings(fit)등
# 주성분들의 로딩 벡터들을 보여준다.
plot(fit, type="lines")
# Scree plot(스크리 그림)이라고 한다.

fit$scores
# 각 관측치를 주성분들로 표현한 값  


biplot(fit)값
# 관측치들을 첫 번째와 두 번째 주성분의 좌표에 그린 그림


# 새로운 컴퓨터를 구입했을 때, 가격, 소프트웨어, 외형,
# 브랜드에 대한 만족도를 1~7까지의 척도로
# 점수를 부여한 분석

Price <- c(6,7,6,5,7,6,5,6,3,1,2,5,2,3,1,2)
Software <- c(5,3,4,7,7,4,7,5,5,3,6,7,4,5,6,3)
Aesthetics <- c(3,2,4,1,5,2,2,4,6,7,6,7,5,6,5,7)
Brand <- c(4,2,5,3,5,3,1,4,7,5,7,6,6,5,5,7)

data <- data.frame(Price, Software, Aesthetics, Brand)
data

pca <- princomp(data, cor=T)
pca


summary(pca, loadings=T)
#Loadings:
#  Comp.1 Comp.2 Comp.3 Comp.4
#Price       0.523         0.848       
#Software    0.177  0.977 -0.120       
#Aesthetics -0.597  0.134  0.295  0.734
#Brand      -0.583  0.167  0.423 -0.674

# 해석: Comp.1은 Aesthetics와 Brand가 클수록,
# Price가 낮을수록 높은 값을 가지고
# Software의 영향은 적게 받는다.

# Comp.2는 Software의 영향만을 크게 받는다.

# Comp.1은 패션 추구형, 
# Comp.2는 기능 추구형을 측정하는 변수로 해석 할 수 있다.

biplot(pca)

# 시계열 예측
# 시계열 자료 불러오기
# 예제1: 다음은 1871년도부터 1970년도까지 아스완 댐에서 측정한 나일강의 연간 유입량에 관한 시계열 데이터이다. 
# 이 데이터는 R에 기본적으로 내장되어 있는 Nile 데이터이다.
data(Nile)
Nile

# 일반 데이터 셋을 시계열 자료 형식으로 변환하려면 ts 함수를 사용하면 된다.

# 예제2: 1974년부터 1979년까지의 영국 내의 월별 폐질환 사망자에 관한 시계열 자료(mdeath: 남성 사망자, fdeath: 여성 사망자)
ldeaths
# 주기는 12개월

# 예제1
plot(Nile)



# 예제 2
plot(ldeaths)

# 분해 시계열
ldeaths.decompose <- decompose(ldeaths)
ldeaths.decompose$seasonal
plot(ldeaths.decompose)

# 원 시계열 자료에서 계절요인을 제거한 후 그림 그리기
ldeaths.decompose.adj <- ldeaths - ldeaths.decompose$seasonal
plot(ldeaths.decompose.adj)

# ARIMA 모형 적용
 
# 예제 1(나일강 연간 유입량 데이터)
# 예제 1의 경우 그림으로 고찰해 보았을 때 시간에 따라 평균이 일정하지 않은
# 비정상시계열 자료였다. 따라서 diff  함수를 이용하여 차분을 한다.

Nile.diff1 <- diff(Nile, differences=1)
plot(Nile.diff1)
# 1번 차분한 겨로가로는 아직 평균이 일정하지 않아 보이므로, 2번 차분한 결과와 비교해보자.

Nile.diff2 <- diff(Nile, differences=2)
plot(Nile.diff2)
# 2번 차분한 결과로 평균과 분산이 시간이 지남에 따라 어느정도 일정한 정상성을 만족하는 것으로 보인다.

# ARIMA 모델 적합 및 결정
# 자기상관함수

acf(Nile.diff2, lag.max=20)
acf(Nile.diff2, lag.max=20, plot=FALSE)

# lag가 20개로 설정한 것을 볼 수 있는데, lag 개수를 너무 많이 설정하면 자기상관함수 그래프를 보고
# 모형 식별을 위한 판단이 힘들기 때문에 적절한 값을 선택한다.
# 위 결과 자기상관함수가 lag=1, 8을 제외하고 모두 신뢰구간 안에 있는 것을 확인할 수 잇다.
# 다음으로 부분자기상관함수 그래프를 그려보면 아래와 같다.

pacf(Nile.diff2, lag.max=20)
pacf(Nile.diff2, lag.max=20, plot=FALSE)

# 부분자기상관함수가 lag=1~8에서 신뢰구간을 넘어서 음의 값을 가지고, lag=9에서 절단 된 것을
# 볼 수 있다. 이와 같이 자기상관함수와 부분자기상관함수의 그래프를 종합해보면
# 다음과 같은 ARMA 모형이 존재하게 된다.
# - ARMA(8,0): 부분자기상관함수 그래프에서 lag=9에서 절단되었음
# - ARMA(0,1): 자기상관함수 그래프에서 lag=2에서 절단되었음
# - ARMA(p,q): AR 모형과 MA 모형을 혼합하여 모형을 식별하고 결정해야 함.

# forecast 패키지에 있는 auto.arima 함수를 사용하여 적절한 ARIMA 모형을 결정하기
install.packages("forecast")
library(forecast)
auto.arima(Nile)
# arima(1,1,1)

# ARIMA  모형을 이용한 예측
Nile.arima<-arima(Nile, order=c(1,1,1))
Nile.arima

Nile.forecasts <- forecast(Nile.arima, h=10)
# h=10은 10개년도만 예측한다는  뜻
Nile.forecasts
plot(Nile.forecasts)

# 예제 2 ARIMA 모형 적용
auto.arima(ldeaths)
# arima(0,0,2) MA모형
ldeaths.arima <- arima(ldeaths, order=c(0,0,2))
ldeaths.arima

ldeaths.forecasts <- forecast(ldeaths.arima, h=10)
ldeaths.forecasts
plot(ldeaths.forecasts)
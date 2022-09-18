# ADsP $ R 210816 (정형데이터마이닝) 
# 로지스틱 회귀분석 예제
# R에서 로지스틱회귀모형은 glm() 함수를 이용하여 수행한다.
# iris 데이터로 실습

data(iris)
head(iris)
names(iris)

unique(iris$Species)

# 이진 분류로 만들어 주기 위해
# Species가 setosa 와 versicolor인 100개의 자료만 이용

a <- subset(iris, Species=="setosa"|Species=="versicolor")
str(a)

b <- glm(Species~Sepal.Length, data=a, family = binomial)
summary(b)

#Deviance Residuals: 
#  Min        1Q    Median        3Q       Max  
#-2.05501  -0.47395  -0.02829   0.39788   2.32915  
#
#Coefficients:
#  Estimate Std. Error z value Pr(>|z|)    
#(Intercept)   -27.831      5.434  -5.122 3.02e-07 ***
#  Sepal.Length    5.140      1.007   5.107 3.28e-07 ***
#  ---
#  Signif. codes:  
#  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
#(Dispersion parameter for binomial family taken to be #1)
#
#Null deviance: 138.629  on 99  degrees of freedom
#Residual deviance:  64.211  on 98  degrees of freedom
#AIC: 68.211
#
#Number of Fisher Scoring iterations: 6

# Null deviance: 절편만 포함하는 모형(H0: beta=0 하의 모형)의 완전모형(또는 포화모형)으로부터의 이탈도(deviance)를 나타낸다. 판단 근거: p-value
# Residual deviance는 예측변수가 추가된 적합 모형의 이탈도를 나타낸다. 판단 근거: p-value

coef(b)
exp(coef(b)["Sepal.Length"])

# 회귀 계수 beta와 오즈의 증가량 exp(beta)에 대한 
# 신뢰구간은 다음고 같다.

confint(b, parm='Sepal.Length')

exp(confint(b, parm="Sepal.Length"))

# fitted() 함수를 통해 적합 결과를 확인 할 수 있다.
fitted(b)[c(1:5, 96:100)]

# predict() 함수를 이용하여 새로운 자료에 대한 예측을 수행한다. 여기서는 편의상 모형 구축에 사용된 자료를 다시 사용한다,

predict(b, newdata=a[c(1,50,51,100),], type="response")

# cdplot() 함수는 Sepal.Length(연속형 변수)의 변화에 따른 범주형 변수의 조건부 분포를 보여준다.
# 아래 그림은 Sepal.Length가 커짐에 따라 versicolor의 확률이 증가함을 보여준다. 이 함수는 로지스틱 회귀의 탐색적 분석에 유용하다.

cdplot(Species~Sepal.Length, data=iris)

plot(a$Sepal.Length, a$Species, xlab="Sepal.Length")
x=seq(min(a$Sepal.Length), max(a$Sepal.Length), 0.1)
lines(x, 1+(1/(1+(1/exp(-27.831+5.140*x)))), type="l", col="red")


# 예제 2 1973~1974년도에 생산된 32종류의 자동차에 대해
# 11개 변수값 측정한 자료

attach(mtcars)
str(mtcars)
head(mtcars)
names(mtcars)
unique(mtcars$vs)
glm.vs <- glm(vs~mpg+am, data=mtcars, family=binomial)

summary(glm.vs)

# 변수 선택법 적용
step.vs <- step(glm.vs, direction = "backward")
summary(step.vs)

ls(glm.vs)
str(glm.vs)

# anova() 함수는 모형의 적합(변수가 추가되는) 단계
# 별로 이탈도의 감소량과 유의성 검정 결과를 제시해준다

anova(glm.vs, test="Chisq")
#Df Deviance Resid. Df Resid. Dev  Pr(>Chi)    
#NULL                    31     43.860              
#mpg   1   18.327        30     25.533 1.861e-05 ***
#  am    1    4.887        29     20.646   0.02706 *  

# 위의 결과는 절편항만 포함하는 영(null)모형에서 mpg와 am 변수가 차례로 모형에 추가됨에 따라 발생하는 이탈도의 감소량을 제시하며, p-값은 P(x^2(1)>18.327)과 P(x^2(1) > 4.887)을 계산한 값이다.


1-pchisq(18.327, 1)
# 1.860515e-05

1-pchisq(4.887, 1)
# 0.02705967
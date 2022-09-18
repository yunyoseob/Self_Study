# ADsP&R 공부 210819(의사결정나무, 배깅, 부스팅 모형)
# ADsP 제 4과목 데이터 분석

# 의사결정나무 모형

library(rpart)

c<-rpart(Species~., data=iris)
c

plot(c, compress = T, margin=0.3)
text(c, cex=1.5)

head(predict(c, newdata=iris, type="class"))
tail(predict(c, newdata=iris, type="class"))

install.packages('rpart.plot')
library(rpart.plot)
prp(c, type=4, extra=2)

ls(c)
#[1] "call"                "control"            
#[3] "cptable"             "frame"              
#[5] "functions"           "method"             
#[7] "numresp"             "ordered"            
#[9] "parms"               "splits"             
#[11] "terms"               "variable.importance"
#[13] "where"               "y"     

c$cptable
#CP nsplit rel error xerror       xstd
#1 0.50      0      1.00   1.13 0.05279520
#2 0.44      1      0.50   0.58 0.05964338
#3 0.01      2      0.06   0.10 0.03055050

# $cptable은 트리의 크기에 따른 비용-복잡도 모수를
# 제공하며, 교차타당성오차(cross-validation error)를
# 함께 제공한다. 이 값들은 prune() 또는 rpart.control()함수에서 가지치기(pruning)와 트리의 최대크기를 조절하기 위한 옵션으로 사용된다.


opt <- which.min(c$cptable[, "xerror"])
cp <- c$cptable[opt, "CP"]
prune.c <- prune(c, cp=cp)
plot(prune.c)
text(prune.c, use.n=T)
plotcp(c)

# 예제2: 146명의 전립선 암 환자의 자료
# 7개의 예측변수를 이용하여 범주형의 반응변수(ploidy)를 예측(또는 분류)한다.
install.packages(('party'))
library(party)
data(stagec)
str(stagec)
head(stagec)
names(stagec)

# 결측치 제거
stagec1<-subset(stagec, !is.na(g2))
stagec2<-subset(stagec1, !is.na(gleason))
stagec3<-subset(stagec2, !is.na(eet))
str(stagec3)

# train, test 분ㄹ
set.seed(1234)
ind <- sample(2, nrow(stagec3), replace=TRUE, prob=c(0.7, 0.3))
ind

trainData<-stagec3[ind==1,]
testData<-stagec3[ind==2,]

tree <- ctree(ploidy~., data=trainData)
tree
plot(tree)
testPred=predict(tree, newdata=testData)
table(testPred, testData$ploidy)

# 예제 3
# airquality 자료에 대해 의사결정나무모형 적합
airq <- subset(airquality, !is.na(Ozone))
head(airq)

airct <- ctree(Ozone~., data=airq)
airct
plot(airct)

head(predict(airct, data=airq))
predict(airct, data=airq, type='node')

mean((airq$Ozone - predict(airct))^2)
# 403.6668

#### 앙상블 모형
## bagging(배깅: bootstrap aggregating)
# 예제1: iris 자료에 대해 R 패키지 (adabag)의
# bagging() 함수를 통해 분석 수행
install.packages(("adabag"))
library(adabag)
data(iris)
iris.bagging <- bagging(Species~., data=iris, mfinal=10)
iris.bagging$importance

plot(iris.bagging$trees[[10]])
text(iris.bagging$trees[[10]])

pred<-predict(iris.bagging, newdata=iris)
table(pred$class, iris[,5])

## boosting

# ada boost
library(adabag)
data(iris)
boo.adabag <- boosting(Species~., data=iris, boos = TRUE, mfinal = 10)
boo.adabag$importance
plot(boo.adabag$trees[[10]])
text(boo.adabag$trees[[10]])

pred <- predict(boo.adabag, newdata=iris)
tb <- table(pred$class, iris[,5])

# 오분류율 계산하기
error.rpart<-1-(sum(diag(tb))/sum(tb))
error.rpart
# [1] 0

# iris 자료 중 setosa를 제외한 versicolor와 
# virginica 자료만으로 분석을 수행한다.
install.packages("ada")
library(ada)
data(iris)
iris[iris$Species != "setosa",] -> iris
n <- dim(iris)[1]

# 총 100개의 자료를 60개의 훈련용 자료와
# 검증용 자료로 나누었다.
trind<-sample(1:n, floor(.6*n), FALSE)
teind<-setdiff(1:n, trind)

iris[,5]<-as.factor((levels(iris[,5])[2:3])[as.numeric(iris[,5])-1])

gdis<-ada(Species~., data=iris[trind,], iter=20, nu=1, type="discrete")

gdis<-addtest(gdis, iris[teind, -5], iris[teind, 5])

gdis

varplot(gdis)
# varplot() 함수는 변수의 중요도를 나타내는
# 그림을 제공한다.
# Petal.Width가 가장 중요한 변수로 사용되었음을 보여준다.

pairs(gdis, iris[trind, -5], maxvar=4)
# pairs() 함수는 두 예측변수의 조합별로
# 분류된 결과를 그려준다.
# maxvar= 옵션을 통해 변수의 수
# (중요도가 높은 상위 변수의 수)를 지정
# 할 수 있다.

### 랜덤포레스트
install.packages("randomForest")
library(randomForest)
library(rpart)
data(stagec)
stagec3 <- stagec[complete.cases(stagec),  ]
set.seed(1234)
ind <- sample(2, nrow(stagec3), replace=TRUE, prob=c(0.7,0.3))
# train, test 분할
trainData <- stagec3[ind==1,]
testData<-stagec[ind==2, ]
rf <- randomForest(ploidy~., data=trainData, ntree=100, proximity=TRUE)
table(predict(rf), trainData$ploidy)
#diploid tetraploid aneuploid
#diploid         45          0         3
#tetraploid       1         51         0
#aneuploid        2          0         0

print(rf)
plot(rf)
# 검은색: 전체 오분류율

importance(rf)
#MeanDecreaseGini
#pgtime         4.6800225
#pgstat         2.0635061
#age            3.5726107
#eet            0.7875501
#g2            37.5032896
#grade          1.2084410
#gleason        2.0820408

varImpPlot(rf)

rf.pred <- predict(rf, newdata=testData)
table(rf.pred, testData$ploidy)
#rf.pred      diploid tetraploid aneuploid
#diploid         12          0         0
#tetraploid       0         17         0
#aneuploid        0          0         2

plot(margin(rf))
# 마진(margin)은 랜덤포레스트의 분류기(classifiers) 
# 가운데 정분류를 수행한 비율에서
# 다른 클래스로 분류한 비율의 최대치를 뺀 값을
# 나타낸다.
# 즉, 양(positive)의 마진은 정확한 분류를 나타내며,
# 음(negative)은 그 반대이다.


# 랜덤포레스트는 다음과 같이  R패키지 [party]의
# cforest() 함수를 이용할 수도 있다.
set.seed(1234)
cf <- cforest(ploidy~., data=trainData)
cf.pred <- predict(cf, newdata=testData, OOB=TRUE, type="response")
# ADsP&R 공부 210819(의사결정나무, 배깅, 부스팅 모형)
# ADsP 제 4과목 데이터 분석

# 모형 평가
data(iris)
nrow(iris)
# 150
set.seed(1234)
idx <- sample(2, nrow(iris), replace=TRUE, prob=c(0.7, 0.3))

trainData<-iris[idx==1,]
testData<-iris[idx==2,]


nrow(trainData)
# 112

nrow(testData)
# 38

# KFold (k=10)
k=10
iris <- iris[sample(nrow(iris)),]
folds <- cut(seq(1, nrow(iris)), breaks=k, labels=FALSE)
trainData=list(0) # an ampty list of length k
testData=list(0)

for (i in 1:k) {
  testIdx <- which(folds==i, arr.ind = TRUE)
  testData[[i]] <- iris[testIdx, ]
  trainData[[i]] <- iris[-testIdx, ]
}

head(trainData[[1]])
head(trainData[[2]])

## 성능이 좋은 모형을 찾기 위한 평가지표
iris<-subset(iris, Species =="setosa"|Species =="versicolor")

iris$Species <- factor(iris$Species)
set.seed(1234)
iris <- iris[sample(nrow(iris)),] #Randomly shuffle the data

trainData<-iris[1:(nrow(iris)*0.7),]
testData<-iris[((nrow(iris)*0.7)+1):nrow(iris),]
nrow(trainData)
# [1] 70

library(nnet)
library(rpart)
# 신경망 모형을 nnet을 통해 학습, 의사결정나무 모형은 {rpart}의 rpart() 함수를 이용하여 모형을 학습한다.
nn.iris<-nnet(Species~., data=trainData, size=2, rang=0.1, decay=5e-4, maxit=200) # Neural network

dt.iris<-rpart(Species~., data=trainData) #Decision Tree

nn_pred<-predict(nn.iris, testData, type="class")
dt_pred<-predict(dt.iris, testData, type="class")

# 각 모형의 오분류표를 도출하기 위해 R패키지 {caret}의
# confusionMatrix() 함수를 이용한다. 

install.packages("e1071")
# R패키지 {e1071}가 설치되어 있지 않은 경우 에러가 발생

library(caret)
nn_con <- confusionMatrix(nn_pred, testData$Species)
#Error: `data` and `reference` should be factors with the same levels.

# Error solution
nn_pred<-predict(nn.iris, testData, type="class")
nn_pred<-unlist(nn_pred)
nn_pred<-as.factor(nn_pred)
nn_con <- confusionMatrix(nn_pred, testData$Species)


dt_con <- confusionMatrix(dt_pred, testData$Species)


nn_con$table

dt_con$table

accuracy <- c(nn_con$overall['Accuracy'], dt_con$overall['Accuracy'])

precision<-c(nn_con$brClass['Pos Pred Value'],dt_con$brClass['Pos Pred Value'])

recall<-c(nn_con$byClass['Sensitivity'], dt_con$byClass['Sensitivity'])

f1<-2*((precision*recall)/(precision+recall))

result<-data.frame(rbind(accuracy, precision, recall, f1))

names(result) <- c("Neural Network", "Decision Tree")
result
#             Neural Network Decision Tree
#accuracy              1             1
#recall                1             1

# ROC 그래프 예제
# 예제 4: 자연유산과 인공유산 후의 불임에 대한
# 자료인 infert에 대하여 목표변수를 분류하는
#(1: 사례, 0: 대조) 의사결정나무 모형과
# 신경망 모형의 ROC 그래프 분석 결과 예제이다.
# infert 자료에 대한 분류 분석 모형 평가 비교를 위하여
# 의사결정나무 모형은 R패키지 {C50}의 C5.0() 함수를 
# 사용하고, 신경망 모형은 {neuralnet}의 neuralnet()함수
# 를 사용한다. 모형 학습 및 검증을 위하여
# 70%의 훈련용 자료와 30%의 검증용 자료로 구분한다.

set.seed(1234)
data("infert")
infert <- infert[sample(nrow(infert)),] #Randomly shuffle the data

infert <-infert[,c("age","parity","induced","spontaneous","case")]
trainData<-infert[1:(nrow(infert)*0.7),]
testData<-infert[((nrow(infert)*0.7)+1):nrow(infert),]

library(neuralnet)
net.infert<-neuralnet(case~age+parity+induced+spontaneous, data = trainData, hidden = 3, err.fct="ce", linear.output=FALSE, likelihood = TRUE)

n_test <- subset(testData, select=-case)
nn_pred<-compute(net.infert, n_test)

testData$net_pred<-nn_pred$net.result
head(testData)
#age parity induced spontaneous case  net_pred
#123  28      1       1           0    0 0.3737403
#5    35      3       1           1    1 0.1620298
#240  26      2       1           1    0 0.2437085
#147  31      2       0           0    0 0.1615092
#120  36      1       0           0    0 0.1616207
#50   38      3       0           2    1 0.9999993

install.packages("C50")
library(C50)
trainData$case <-factor(trainData$case)
dt.infert <-C5.0(case~age+parity+induced+spontaneous, data = trainData)
testData$dt_pred<-predict(dt.infert, testData, type="prob")[,2]
head(testData)
#age parity induced spontaneous case  net_pred   dt_pred
#123  28      1       1           0    0 0.3737403 0.2095227
#5    35      3       1           1    1 0.1620298 0.2661850
#240  26      2       1           1    0 0.2437085 0.2661850
#147  31      2       0           0    0 0.1615092 0.2095227
#120  36      1       0           0    0 0.1616207 0.2095227
#50   38      3       0           2    1 0.9999993 0.7402055

# 각 모형의 예측 결과값을 기반으로 ROC 그래프를 작성하기 위해서는
#  R패키지 {Epi}의 ROC() 함수를 사용한다.
install.packages("Epi")
library(Epi)
neural_ROC <- ROC(form = case~net_pred, data=testData, plot="ROC")
# AUC: 0.787

dtree_ROC <- ROC(form=case~dt_pred, data=testData, plot="ROC")
# AUC: 0.774

# 신경망 모형의 AUC가 의사결정나무의 AUC보다 크게 나와
# 신경망 모형의 분류 분석 모형이 더 높은 성과를 보인다고 
# 할 수 있다.

### 이익도표와 향상도 곡선
# 예제 4에서 신경망 모형과 의사결정 모형간의 향상도 곡선 비교 평가를 위해 R패키지 {ROCR}을 사용한다.
# {Epi} 패키지의  ROC()함수의 경우 두 그래프를 함께 
# 나타내기 어려운 반면 {ROCR} 패키지는 여러 모형의
# ROC 그래프 및 향상도 곡선을 함께 나타낼 수 있다는 
# 장점이 있다.

install.packages("ROCR")
library(ROCR)
n_r<-prediction(testData$net_pred, testData$case)
d_r<-prediction(testData$dt_pred, testData$case)
n_p<-performance(n_r, "tpr","fpr") # ROC graph for neural network
d_p<-performance(d_r, "tpr", "fpr") # ROC graph for decision tree

plot(n_p, col="red") # neural network (Red)
par(new=TRUE)
plot(d_p, col="blue") # decision tree (Blue)
abline(a=0, b=1)

# 신경망 모형의 향상도 곡선 예제
n_lift <-performance(n_r, "lift", "rpp")
plot(n_lift, col="red")
abline(v=0.2) # black line

# 신경망 모형의 경우 상위 20%의 집단에 대하여 랜덤 모델과 비교할 때 약 2배의 성과 향상을 보인다.
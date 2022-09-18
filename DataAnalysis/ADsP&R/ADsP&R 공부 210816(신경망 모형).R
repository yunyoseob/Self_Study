# ADsP&R 공부 210816(신경망 모형)
# ADsP 제 4과목 데이터 분석
# 인공신경망
# iris 자료에 대해 신경망 모형을 이용하여 분석한 예제
# 자료의 수: 150개, 입력변수 차원 4, 목표값 3개의 범주


library(nnet)
nn.iris <- nnet(Species~., data=iris, size=2, rang=0.1, decay=5e-4, maxit=200)

summary(nn.iris)
# 연결선의 방향과 가중치를 나타냄.
# 초기값 별도 지정 안하면 nnet()함수 실행될옴 때마다 결과 다르게 나옴.

install.packages("devtools")
library(devtools)
source_url('https://gist.githubusercontent.com/Peque/41a9e20d6687f2f3108d/raw/85e14f3a292e126f1454864427e3a189c2fe33f3/nnet_plot_update.r')
plot.nnet(nn.iris)

install.packages("clusterGeneration")
library(clusterGeneration)
library(scales)
library(reshape)
plot(nn.iris)

# confusion matrix
table(iris$Species, predict(nn.iris, iris, type="class"))

# 예제 2: 자연유산과 인공유산 후의 불임에 대한
# 사례-대조 연구 자료로 8개의 변수와
# 248개의 관측치를 가지고 있다.
# 반응변수  case변수는 (1:사례, 0: 대조)를 나타낸다.

data(infert, package="datasets")
str(infert)
head(infert)
names(infert)
unique(infert$case)

install.packages("neuralnet")
library(neuralnet)
net.infert <- neuralnet(case~age+parity+induced+spontaneous, data=infert, hidden=2, err.fct="ce", linear.output = FALSE, likelihood = TRUE)

net.infert
plot(net.infert)
# neuralnet() 함수는 다양한 역전파(back-propagation)알고리즘을 통해 모형을 적합한다.

names(net.infert)
net.infert$result.matrix

out <- cbind(net.infert$covariate, net.infert$net.result[[1]])

dimnames(out)<-list(NULL, c("age","parity","induced","spontaneous","nn-output"))

head(out)

head(net.infert$generalized.weights[[1]])
# 일반화 가중치 (generalized weights)는 각 공변량들의 효과를 나타내는 것으로 로지스틱 회귀모형에서의 회귀계수와 유사하게 해석됨,
# 다만, 로지스틱회귀와는 달리 일반화 가중치는 다른 모든 공변량에 의존하므로 각 자료점에서 국소적인 기여도를 나타낸다,

# 일반화 가중치 시각화
par(mfrow=c(2,2))
gwplot(net.infert, selected.covariate = "age", min=-2.5, max=5)
gwplot(net.infert, selected.covariate = "parity", min=-2.5, max=5)
gwplot(net.infert, selected.covariate = "induced", min=-2.5, max=5)
gwplot(net.infert, selected.covariate = "spontaneous", min=-2.5, max=5)
par(mfrow=c(1,1))

# compute() 함수는 각 뉴런의 출력값을 계산해준다. 이를 이용하여 새로운 공변량 조합(또는 결측 조합)에 대한 예측값도 구할 수 있다.

# 예시: age=22, parity=1, induced <= 1, spontaneous <= 1 을 가지는 결측 공변량 조합에 대한 예측결과

new.output <- compute(net.infert, covariate = matrix(c(22,1,0,0,
                                                       22,1,1,0,
                                                       22,1,0,1,
                                                       22,1,1,1), byrow=TRUE, ncol=4))
 
new.output$net.result

#      [,1]
#[1,] 0.1499343
#[2,] 0.1956788
#[3,] 0.3111008
#[4,] 0.8527731

# 위 결과는 주어진 공변량 좋바에 대한 예측결과로,
# 사전 낙태의 수에 따라 예측 확률이 증가함을 보여줌

# 다층신경망 예시 
# 0과 100사이의 난수 50개를 발생시키고, 제곱근을
# 취한 값을 결과로 하는 자료를 구축한다. 이 자료를
# 신경망으로 학습하여 새로운 자료에 대한 예측을 
# 수행한다.

library(neuralnet)
train.input <- as.data.frame(runif(50, min=0, max=100))
train.output <- sqrt(train.input)
train.data <- cbind(train.input, train.output)
colnames(train.data) <- c("Input","Output")
head(train.data)

net.sqrt <- neuralnet(Output~Input, train.data, hidden = 10, threshold = 0.01)

print(net.sqrt)
plot(net.sqrt)

# 몇 개의 검증용 자료에 대해 구축된 신경망 모형을 적용한다. 1~10 정수값의 제곱을 취하여 검증용 자료( test.data) 를 만든 후, 이 자료에 대해 compute()함수를 통해 신경망 모형(net.sqrt) 을 적용하고 그 결과를 출력한다.

test.data <- as.data.frame((1:10)^2)
test.out <- compute(net.sqrt, test.data)
ls(test.out)
print(test.out$net.result)

# 은닉층이 2개인 모형을 적용해보면 다음과 같다. 각각의 은닉노드의 수는 10개, 8개로 한다. 이를 위해 neuralnet() 함수의 옵션을 hidden=c(10,8)으로 수정하여 위 과정을 실행한다. 그 결과는 다음과 같다.

net2.sqrt <- neuralnet(Output~Input, train.data, hidden=c(10,8), threshold = 0.01)
plot(net2.sqrt)

test2.out <- compute(net.sqrt, test.data)

print(test2.out$net.result)
# Kaggle House Price 변수선택 적용

train<-read.csv('C:/Users/bella/Desktop/SelfStudy/회귀분석/train.csv', header=T)
test<-read.csv('C:/Users/bella/Desktop/SelfStudy/회귀분석/test.csv', header=T)

head(train)
head(test)

names(train)

m <-lm(formula=SalePrice~., data=train)
summary(m) # adf-R: 0.8075
#plot(m)

# both
m2 <- step(m, direction="both")
summary(m2) # adj-R: 0.8091, AIC=30554.62


# foward
m3 <- step(m, direction = "forward")
summary(m3) # adj-R: 0.8075, AIC=30585.52

# backward
m4 <- step(m, direction = "backward")
summary(m4) # adj-R: 0.8091, AIC=30554.62
plot(m4)

#SalePrice ~ MSSubClass + LotArea + Street + LotShape + LandContour +
#  LandSlope + Neighborhood + Condition2 + BldgType + OverallQual + 
#  OverallCond + YearBuilt + RoofStyle + RoofMatl + ExterQual + 
#  HeatingQC + X1stFlrSF + X2ndFlrSF + BedroomAbvGr + KitchenAbvGr + 
#  TotRmsAbvGrd + Fireplaces + WoodDeckSF + ScreenPorch + YrSold + 
#  SaleCondition
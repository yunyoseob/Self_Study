# 빅데이터분석기사실기연습 20211127
# 작업형 제 2유형 1번 문제
# 주어진 데이터는 각 고객이 가입한 서비스와 계정 정보,
# 인구에 대한 통계 정보들이다. 주어진 훈련 데이터를 이용하여
# 모델을 훈련한 후 테스트 데이터로 고객의 이탈 여부를 예측하고
# csv 포맷으로 제출하시오. (단, 이탈: "Yes", 유지: "No")
import pandas as pd
import numpy as np
import sklearn
import scipy
import xgboost

df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
df.head()
#Content
#Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

#The data set includes information about:

#Customers who left within the last month – the column is called Churn
#Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
#Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
#Demographic info about customers – gender, age range, and if they have partners and dependents
# https://www.kaggle.com/blastchar/telco-customer-churn

df.info()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

print(len(df.columns))
# 21

x_test=df.copy()
x_test


for i in range(0,21):
    name=x_test.columns[i]
    if type(x_test.iloc[0, i])==int:
        pass
    else:
        x_test[name]=le.fit_transform(x_test[name])
        
        
x_test.info()
# YES: 1, NO: 0

x=x_test.drop("Churn", axis=1)
y=x_test['Churn']

from sklearn.model_selection import train_test_split
x_test, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=42)
print(x_test.shape, x_test.shape, y_train.shape, y_test.shape)

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score

ada=AdaBoostClassifier(random_state=42)
gb=GradientBoostingClassifier(random_state=42)
rf=RandomForestClassifier(random_state=42)
dt=DecisionTreeClassifier(random_state=42)
xgb=XGBClassifier(random_state=42)

def result(model, x_test, x_test, y_train, y_test):
    model.fit(x_test, y_train)
    y_pred=model.predict(x_test)
    print(model.score(x_test, y_train), roc_auc_score(y_test, y_pred))

result(ada, x_test, x_test, y_train, y_test)
# 0.8058217962371317 0.7249811090293663
result(gb, x_test, x_test, y_train, y_test)
# 0.8274760383386581 0.7169925574751312
result(xgb, x_test, x_test, y_train, y_test)
# 0.9689385871494498 0.7173664951815086


x_test=x_test.copy()

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

mm=MinMaxScaler()
ss=StandardScaler()
rr=RobustScaler()

new_xtn=mm.fit_transform(x_test)
new_xte=mm.fit_transform(x_test)

# minmax가 가장 좋음
result(ada, new_xtn, new_xte, y_train, y_test)
# 0.8058217962371317 0.7254637345119919
result(gb, new_xtn, new_xte, y_train, y_test)
# 0.8274760383386581 0.7196735226225843
result(xgb, new_xtn, new_xte, y_train, y_test)
# 0.9689385871494498 0.7190822093637108

print(len(x_test.columns))
# 21

for i in range(0,21):
    name=x_test.columns[i]
    print(name, len(x_test[name].unique()))

d_1=pd.get_dummies(x_test['gender'], prefix='gender')
d_2=pd.get_dummies(x_test['SeniorCitizen'], prefix='SeniorCitizen')
d_3=pd.get_dummies(x_test['Partner'], prefix='Partner')
d_4=pd.get_dummies(x_test['Dependents'], prefix='Dependents')
d_5=pd.get_dummies(x_test['PhoneService'], prefix='PhoneService')
d_6=pd.get_dummies(x_test['MultipleLines'], prefix='MultipleLines')
d_7=pd.get_dummies(x_test['InternetService'], prefix='InternetService')
d_9=pd.get_dummies(x_test['OnlineSecurity'], prefix='OnlineSecurity')
d_10=pd.get_dummies(x_test['OnlineBackup'], prefix='OnlineBackup')
d_11=pd.get_dummies(x_test['DeviceProtection'], prefix='DeviceProtection')
d_12=pd.get_dummies(x_test['TechSupport'], prefix='TechSupport')
d_13=pd.get_dummies(x_test['StreamingTV'], prefix='StreamingTV')
d_14=pd.get_dummies(x_test['StreamingMovies'], prefix='StreamingMovies')
d_15=pd.get_dummies(x_test['Contract'], prefix='Contract')
d_16=pd.get_dummies(x_test['PaperlessBilling'], prefix='PaperlessBilling')
d_17=pd.get_dummies(x_test['PaymentMethod'], prefix='PaymentMethod')

dd=pd.concat([d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_9,d_10,d_11,d_12,d_13,d_14,d_15,d_16,d_17], axis=1)
print(len(dd.columns))
# 46
ee=pd.concat([d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_9,d_10,d_11,d_12,d_13,d_14,d_15,d_16,d_17], axis=1)
print(len(ee.columns))
# 46

new_xtn=pd.concat([x_test,dd], axis=1)

new_xte=pd.concat([x_test, ee], axis=1)

new_xte.drop(['gender','SeniorCitizen','Partner','Dependents',
              'PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup',
              'DeviceProtection','TechSupport','StreamingTV','StreamingMovies',
             'Contract','PaperlessBilling','PaymentMethod' ], axis=1, inplace=True)

# 더미변수 결과
result(ada, new_xtn, new_xte, y_train, y_test)
# 0.8040468583599574 0.7361345451157782
result(gb, new_xtn, new_xte, y_train, y_test)
# 0.8251686190983316 0.7276090241907937
result(xgb, new_xtn, new_xte, y_train, y_test)
# 0.9680511182108626 0.720047460328961

# 더미변수 + minmax scaler
mm_xtn=mm.fit_transform(new_xtn)
mm_xte=mm.fit_transform(new_xte)

result(ada, mm_xtn, mm_xte, y_train, y_test)
#0.8040468583599574 0.7343114370594264
result(gb, mm_xtn, mm_xte, y_train, y_test)
#0.8251686190983316 0.7257859161344417
result(xgb, mm_xtn, mm_xte, y_train, y_test)
# 0.9680511182108626 0.7236936764416658

# 결론 더미변수 결과한 결과로 최종 제출
ada.fit(new_xtn, y_train)
y_pred=ada.predict(new_xte)
print(ada.score(new_xtn, y_train), roc_auc_score(y_test, y_pred))
# 0.8040468583599574 0.7361345451157782

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))
# [[942  94]
# [163 210]]

pred=pd.DataFrame(y_pred, columns=['Churn'])

pred

########## 끝 ############

# 작업형 제 2유형 2번 문제
# 다음은 mtcars 데이터 세트로 32개 자동차들의 디자인과 성능을 비교한 데이터이다.
# 훈련 데이터와 평가데이터를 7:3으로 분할한 후 연비(mpg)를 예측하는 최적 모델을 만들고
# RMSE로 평가 결과를 구하시오.
import pandas as pd
import numpy as np
import sklearn
import xgboost
import scipy

df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df.info()
df.isna().sum()
print(len(df.columns), len(df.index))

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df['model']=le.fit_transform(df['model'])

x=df.drop('mpg', axis=1)
y=df['mpg']

from sklearn.model_selection import train_test_split
x_test, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3, random_state=42)
print(x_test.shape)
print(x_test.shape)

df['mpg'].value_counts
df.corr()
df['vs'].value_counts # 더미변수 고려
df['cyl'].unique() # 더미변수 고려
df['am'].unique()
df['gear'].unique()

# model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

lr=LinearRegression()
lasso=Lasso(random_state=42)
ridge=Ridge(random_state=42)
en=ElasticNet(random_state=42)
dt=DecisionTreeRegressor(random_state=42)
rf=RandomForestRegressor(random_state=42)
ada=AdaBoostRegressor(random_state=42)
gb=GradientBoostingRegressor(random_state=42)
xgb=XGBRegressor(random_state=42)

def result(model, x_test, x_test, y_train, y_test):
    model.fit(x_test, y_train)
    y_pred=model.predict(x_test)
    print(f"model score: {model.score(x_test, y_train)}, rmse: {np.sqrt(mean_squared_error(y_test, y_pred))}")

result(lr, x_test, x_test, y_train, y_test)
# model score: 0.8710422157892772, rmse: 2.595361223814531
result(lasso, x_test, x_test, y_train, y_test)
# model score: 0.7587557865438904, rmse: 3.1625685570214084
result(ridge, x_test, x_test, y_train, y_test)
# model score: 0.86, rmse: 2.3041
result(en, x_test, x_test, y_train, y_test)
# model score: 0.77 , rmse: 3.099

result(dt, x_test, x_test, y_train, y_test)
# model score: 1.0 , rmse: 2.7949
result(rf, x_test, x_test, y_train, y_test)
# model score: 0.9677 , rmse: 2.2115
result(ada, x_test, x_test, y_train, y_test)
# model score: 0.99 , rmse: 2.92
result(gb, x_test, x_test, y_train, y_test)
# model score: 0.9999 , rmse: 2.4477
result(xgb, x_test, x_test, y_train, y_test)
# model score: 0.999999 , rmse: 1.8961    

# xgb, rf, ridge
# make dummies
d1=pd.get_dummies(x_train['vs'], prefix="vs")
d2=pd.get_dummies(x_train['cyl'], prefix="cyl")
d3=pd.get_dummies(x_train['am'], prefix="am")
d4=pd.get_dummies(x_train['gear'], prefix="gear")

e1=pd.get_dummies(x_test['vs'], prefix="vs")
e2=pd.get_dummies(x_test['cyl'], prefix="cyl")
e3=pd.get_dummies(x_test['am'], prefix="am")
e4=pd.get_dummies(x_test['gear'], prefix="gear")

d5=pd.concat([d1,d2,d3,d4], axis=1)
e5=pd.concat([e1,e2,e3,e4], axis=1)

n_train=pd.concat([x_train, d5], axis=1)
n_test=pd.concat([x_test, e5], axis=1)

# xgb, rf, ridge
result(xgb, n_train, n_test, y_train, y_test)
# model score: 0.9999999880087002, rmse: 1.880784885484692
result(rf, n_train, n_test, y_train, y_test)
#model score: 0.9695969084386112, rmse: 2.12367754143608
result(ridge, n_train, n_test, y_train, y_test)
# model score: 0.8741238036772061, rmse: 2.0980530827648027


xgb.fit(n_train, y_train)
y_pred=xgb.predict(n_test)
print(f"model score: {xgb.score(n_train, y_train)}, rmse: {np.sqrt(mean_squared_error(y_test, y_pred))}")
# model score: 0.9999999880087002, rmse: 1.880784885484692



####### 끝 ########
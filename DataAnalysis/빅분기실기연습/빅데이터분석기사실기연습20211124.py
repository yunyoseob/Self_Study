#빅데이터분석기사실기연습20211124
import pandas as pd
import numpy as np
import sklearn
import xgboost

# 빅데이터분석기사 TEST체험하기 작업형 dataframe
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df=df.set_index('model')

df.isna().sum()
# 결측치 없음

df.info()
print(len(df.index))
# 32줄

#이상치 조회 및 제거
# 3-sigma
# disp 칼럼 이상치를 조회후 제거한 데이터를 출력하라.
print([x for x in df['disp'] if (x <= df['disp'].mean()-(df['disp'].std()*3)) or (x >= df['disp'].mean()+(df['disp'].std()*3))])
# 조회 결과 없음.

df_1=df.copy()
df_1['disp']
# 1,3,5,19,20,31에 의도적으로 이상치 넣어주기
df_1.iloc[1, 2]=df_1.iloc[1, 2]*1000
df_1.iloc[3, 2]=df_1.iloc[3, 2]*1000
df_1.iloc[5, 2]=df_1.iloc[5, 2]*1000
df_1.iloc[19, 2]=df_1.iloc[19, 2]*0.00000001
df_1.iloc[20, 2]=df_1.iloc[20, 2]*0.00000001
df_1.iloc[31, 2]=df_1.iloc[31, 2]*0.00000001

df_1.disp.mean()
df_1.std()

print([x for x in df_1['disp'] if (x <= df_1['disp'].mean()-(df_1['disp'].std()*3)) or (x >= df_1['disp'].mean()+(df_1['disp'].std()*3))])

print(len(df_1.index))

disp_mean=df_1.disp.mean()
disp_std=df_1.disp.std()

over=disp_mean+(3*disp_std)
under=disp_mean-(3*disp_std)

df_1=df_1.loc[df_1.disp <= over]
df_1=df_1.loc[df_1.disp >= under]
df_1

# IQR을 통해 이상치 제거

df_1=df.copy()
df_1['disp']
# 1,3,5,19,20,31에 의도적으로 이상치 넣어주기
df_1.iloc[1, 2]=df_1.iloc[1, 2]*1000
df_1.iloc[3, 2]=df_1.iloc[3, 2]*1000
df_1.iloc[5, 2]=df_1.iloc[5, 2]*1000
df_1.iloc[19, 2]=df_1.iloc[19, 2]*0.00000001
df_1.iloc[20, 2]=df_1.iloc[20, 2]*0.00000001
df_1.iloc[31, 2]=df_1.iloc[31, 2]*0.00000001

df_1.disp.mean()
df_1.std()

q1=np.percentile(df['disp'], 25)
q3=np.percentile(df['disp'], 75)

IQR=q3-q1

df_1=df_1.loc[df_1['disp']>=q1-1.5*IQR]
df_1=df_1.loc[df_1['disp']<=q3+1.5*IQR]
df_1

# 작업형 제 2유형: 모형 구축 및 평가 영역
X_train=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/X_train.csv", encoding="CP949")
X_test=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/X_test.csv", encoding="CP949")
y_train=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/y_train.csv", encoding="CP949")

print(X_train.head())
print(X_test.head())
print(y_train.head())

print(X_train.info())
print(X_test.info())
print(y_train.info())

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

X_train['주구매상품']=le.fit_transform(X_train['주구매상품'])
X_train['주구매지점']=le.fit_transform(X_train['주구매지점'])

X_train.isna().sum()
# 결측치 2295, 환불금액

X_test['주구매상품']=le.fit_transform(X_test['주구매상품'])
X_test['주구매지점']=le.fit_transform(X_test['주구매지점'])

X_test.isna().sum()
# 결측치 1611, 환불금액

X_train['환불금액']=X_train['환불금액'].fillna(X_train['환불금액'].mean())
X_test['환불금액']=X_test['환불금액'].fillna(X_test['환불금액'].mean())

Y_train=y_train[['gender']]

X_train.columns

a=pd.get_dummies(X_train['주구매지점'], prefix="주구매지점")
a

b=pd.concat([X_train, a], axis=1)
b

# 빅데이터분석기사 실기 (수제비 2022)
# 기출문제 작업형 제 1유형
from sklearn import datasets
df_1=datasets.load_boston()

df_1.keys()

df=pd.DataFrame(df_1.data, columns=df.feature_names)
df['PRICE']=df_1.target

df

# 작업형 제 1유형
# 다음은 BostonHousing 데이터 세트이다. crim 항목의 상위에서 10번째 값(즉, 상위 10번째 값중에서 가장 적은 값)으로 상위 10개의 값을 변환하고,
# age 80 이상인 값에 대하여 crim 평균을 구하시오. (21년 2회)# 작업형 제 2유형: 모형 구축 및 평가 영역

print(df.columns)
df_c=df.sort_values(by="CRIM", ascending=False)
상위_10개의_값=df_c.iloc[0:10, 0].values
print("상위 10개 의 값 :", 상위_10개의_값)
# 상위 10개 의 값 : [88.9762 73.5341 67.9208 51.1358 45.7461 41.5292 38.3518 37.6619 28.6558, 25.9406]
print("상위 10번째 값중에서 가장 적은 값 :", df_c.iloc[9, 0])
# 상위 10번째 값중에서 가장 적은 값 : 25.9406

df_A=df.loc[df['AGE'] >=80]
age_mean=df_A['CRIM'].mean()
print("age 80 이상인 값에 대하여 crim 평균 :", age_mean)

df_A['CRIM'].describe()
df_A['AGE'].describe()

# 작업형 제 1유형 2번
# 주어진 데이터 첫 번째 행부터 순서대로 80%까지의 데이터를 훈련 데이터로 추출 후 housing_office 항목에서 
# total_bedrooms 변수의 결측값을 total_bedrooms 변수의 중앙값으로 대체하고 대체 전의 total_bedrooms 변수 표준편차값과
# 대체 후의 'total_bedrooms' 변수 표준편차 값을 산출하려고 한다. 결측값을 중앙값으로 변환한 후, 변환 이전과 이후의 표준편차 차이를 구하시오.
#git clone https://github.com/ageron/handson-ml.git
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/handson-ml/datasets/housing/housing.csv")

# 첫 번째: 주어진 데이터 첫 번째 행부터 순서대로 80% 까지의 데이터를 훈련 데이터로 추출
print(len(df.index))
# 20640
len_df=len(df.index)
len_train=len_df*0.8
print(len_train)
#16512
train=df.iloc[0:16512, :]
print(len(train.index))
#16512

# 두 번째: housing_office 항목에서 total_bedrooms 변수의 결측값을 total_bedrooms 변수의 중앙값으로 대체
train.isna().sum()
# total_bedrooms: 159 개의 결측치 발생

train_before=train.copy()
train_after=train.copy()

total_bedrooms_median=train['total_bedrooms'].median()
print(total_bedrooms_median)
# 436.0

train_after['total_bedrooms']=train['total_bedrooms'].fillna(total_bedrooms_median)
train_after.isna().sum()
# 0개의 결측치

# 대체 전의 total_bedrooms 변수 표준편차값과
# 대체 후의 'total_bedrooms' 변수 표준편차 값을 산출하려고 한다.

# 대체 전의 total_bedrooms 변수 표준편차값
before_std=train_before['total_bedrooms'].std()
print(before_std)
# 435.9005

#  대체 후의 total_bedrooms 변수 표준편차값
after_std=train_after['total_bedrooms'].std()
print(after_std)
# 433.9254

print("변환 이전과 이후의 표준편차 차이 :", before_std-after_std)
# 1.97514

# 작업형 제 1유형 3번
# 다음은 Insurance 데이터 세트이다. Charges 항목에서 이상값의 합을 구하시오. (이상값은 평균에서 1.5표준편차 이상인 값)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/insurance.csv")
df.isna().sum()
df.describe()
print(df.columns)
# Index(['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'], dtype='object')
over_out_lier=df['charges'].mean() + (1.5*df['charges'].std())
print(over_out_lier)
# 31435
under_out_lier=df['charges'].mean() - (1.5*df['charges'].std())
print(under_out_lier)
# -4894
df['charges'].min()
# 1121.8739
df['charges'].max()
# 63770.42801
df['charges'].describe()
df['charges'].mean()
# 13270.4222


df_1=df.loc[df['charges']>=over_out_lier]
df_1

outlier_sum=df_1['charges'].sum()
print("Charges 항목에서 이상값의 합 :", outlier_sum)
# 이상값의 합: 6421430

# 작업형 제 2유형
# 기업에서 생성된 주문데이터이다. 10,009건의 데이터에 대하여
# 정시도착 가능여부 예측 모델을 만들고,
# 평가데이터에 대하여 정시도착 가능여부 예측 확률을 기록한 CSV를 생성하시오.
Train=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/Train.csv")
print(len(Train.columns))
# 칼럼 개수: 12
print(Train.isna().sum())
# 결측치 없음
Train.info()
# Object: Warehouse_block, Mode_of_Shipment, Product_importance, Gender
Train['Warehouse_block'].value_counts()
Train['Mode_of_Shipment'].value_counts()
Train['Product_importance'].value_counts()
Train['Gender'].value_counts()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

Train['Warehouse_block']=le.fit_transform(Train['Warehouse_block'])
Train['Mode_of_Shipment']=le.fit_transform(Train['Mode_of_Shipment'])
Train['Product_importance']=le.fit_transform(Train['Product_importance'])
Train['Gender']=le.fit_transform(Train['Gender'])

Train.describe()

Train.columns

x=Train.drop('Reached.on.Time_Y.N', axis=1)
y=Train['Reached.on.Time_Y.N']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=42)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

y.value_counts()

# Regression
from sklearn.linear_model import LinearRegression
lr=LinearRegression(random_state=42)

lr.fit(x_train, y_train)
lr.score(x_train, y_train)
# 0.21938

y_pred=lr.predict(x_test)

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)
# 0.1881


np.array(y_test).reshape(-1,1)
y_pred.reshape(-1,1)

from sklearn.linear_model import Lasso, Ridge, ElasticNet
lasso=Lasso(random_state=42)
ridge=Ridge(random_state=42)
en=ElasticNet(random_state=42)

# classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

logi=LogisticRegression(random_state=42)
ada=AdaBoostClassifier(random_state=42)
gb=GradientBoostingClassifier(random_state=42)
rf=RandomForestClassifier(random_state=42)
dt=DecisionTreeClassifier(random_state=42)
xgb=XGBClassifier(random_state=42)

result(logi, x_train, x_test, y_train, y_test) 
# 0.6559 0.6544
result(ada, x_train, x_test, y_train, y_test)
# 0.6970 0.7181
result(gb, x_train, x_test, y_train, y_test)
# 0.7205 0.7172
result(rf, x_train, x_test, y_train, y_test)
# 1.0 0.6964
result(dt, x_train, x_test, y_train, y_test)
# 1.0 0.6347
result(xgb, x_train, x_test, y_train, y_test)
# 0.9303 0.6666

from sklearn.metrics import roc_auc_score
def result(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    print(model.score(x_train, y_train))
    y_pred=model.predict(x_test)
    print(roc_auc_score(y_test, y_pred))

# lr lasso ridge en / logi ada gb rf dt xgb
result(lr, x_train, x_test, y_train, y_test)
# 0.219 0.7447
result(lasso, x_train, x_test, y_train, y_test)
# 0.194 0.74615
result(ridge, x_train, x_test, y_train, y_test)
# 0.219 0.7447
 result(en, x_train, x_test, y_train, y_test)
 # 0.21 0.7463
 
# regressor로 다시 접근
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

adaR=AdaBoostRegressor(random_state=42)
gbR=GradientBoostingRegressor(random_state=42)
rfR=RandomForestRegressor(random_state=42)
dtR=DecisionTreeRegressor(random_state=42)
xgbR=XGBRegressor(random_state=42)

result(adaR, x_train, x_test, y_train, y_test) 
# 0.26 0.7433
result(rfR, x_train, x_test, y_train, y_test) 
# 0.89 0.747
result(dtR, x_train, x_test, y_train, y_test) 
# 1.0 0.640
result(gbR, x_train, x_test, y_train, y_test) 
# 0.31 0.743
result(xgbR, x_train, x_test, y_train, y_test) 
# 0.729 0.7408

rfR.fit(x_train, y_train)
y_pred=rfR.predict(x_test)
df_y_pred=pd.DataFrame(y_pred)
df_y_test=pd.DataFrame(y_test)

print(len(df_y_pred.index))


for i in range(0,2200):
    if df_y_pred.iloc[i, 0]<0.500000:
        df_y_pred.iloc[i,0]=0
    else:
        df_y_pred.iloc[i,0]=1

(roc_auc_score(df_y_test, df_y_pred))
# 0.6697

from sklearn.metrics import confusion_matrix
confusion_matrix(df_y_test, df_y_pred)

x_train.corr()

x_train.describe()

# 심화과정
def new_df(data):
    for i in range(0,2200):
        if data.iloc[i, 0]<0.500000:
            data.iloc[i,0]=0
        else:
            data.iloc[i,0]=1
    return data

def modeling(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    model_score=model.score(x_train, y_train)
    pred=model.predict(x_test)
    df_pred_1=pd.DataFrame(pred)
    df_test=pd.DataFrame(y_test)
    df_pred=new_df(df_pred_1)
    print(model_score, roc_auc_score(df_test, df_pred))    

modeling(gb, x_train, x_test, y_train, y_test)
# 현재 가장 높은 점수: 0.72053 0.717217

df_x_tn=x_train.copy()
df_x_te=x_test.copy()

df_x_tn.head()
print(len(df_x_tn.columns))
# 11
print(len(df_x_te.columns))
# 11

def name_unique(df):
    for i in range(0,11):
        name=df.columns[i]
        print(name, len(df[name].unique()))
        
        
name_unique(df_x_tn)
# 8799,5,3,6,5,215,8,3,2,65,3759
name_unique(df_x_te)
# 2200,5,3,6,5,212,8,3,2,65,1709

# Warehouse_block, Mode_of_Shipment, Customer_care_calls, Customer_rating, Prior_purchases, Product_impotance, Gender
df_x_1=pd.get_dummies(df_x_tn['Warehouse_block'], prefix="Warehouse_block")
df_x_2=pd.get_dummies(df_x_tn['Mode_of_Shipment'], prefix="Mode_of_Shipment")
df_x_3=pd.get_dummies(df_x_tn['Customer_care_calls'], prefix="Customer_care_calls")
df_x_4=pd.get_dummies(df_x_tn['Customer_rating'], prefix="Customer_rating")
df_x_5=pd.get_dummies(df_x_tn['Prior_purchases'], prefix="Prior_purchases")
df_x_6=pd.get_dummies(df_x_tn['Product_importance'], prefix="Product_importance")
df_x_7=pd.get_dummies(df_x_tn['Gender'], prefix="Gender")

new_x_tn=pd.concat([df_x_1, df_x_2, df_x_3, df_x_4, df_x_5, df_x_6, df_x_7,], axis=1)

df_x_tn_1=pd.concat([df_x_tn, new_x_tn], axis=1)
df_x_tn_1.drop(['Warehouse_block','Mode_of_Shipment','Customer_care_calls','Customer_rating','Prior_purchases','Product_importance','Gender'], axis=1, inplace=True)
df_x_tn_1

df_x_1=pd.get_dummies(df_x_te['Warehouse_block'], prefix="Warehouse_block")
df_x_2=pd.get_dummies(df_x_te['Mode_of_Shipment'], prefix="Mode_of_Shipment")
df_x_3=pd.get_dummies(df_x_te['Customer_care_calls'], prefix="Customer_care_calls")
df_x_4=pd.get_dummies(df_x_te['Customer_rating'], prefix="Customer_rating")
df_x_5=pd.get_dummies(df_x_te['Prior_purchases'], prefix="Prior_purchases")
df_x_6=pd.get_dummies(df_x_te['Product_importance'], prefix="Product_importance")
df_x_7=pd.get_dummies(df_x_te['Gender'], prefix="Gender")

new_x_te=pd.concat([df_x_1, df_x_2, df_x_3, df_x_4, df_x_5, df_x_6, df_x_7,], axis=1)

df_x_te_1=pd.concat([df_x_te, new_x_te], axis=1)
df_x_te_1.drop(['Warehouse_block','Mode_of_Shipment','Customer_care_calls','Customer_rating','Prior_purchases','Product_importance','Gender'], axis=1, inplace=True)
df_x_te_1


modeling(gb, df_x_tn_1, df_x_te_1, y_train, y_test)
# 0.7272, 0.7189

# Scaler 적용
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

mm=MinMaxScaler()
ss=StandardScaler()
rs=RobustScaler()

ss_x_tn=ss.fit_transform(df_x_tn_1)
ss_x_te=ss.fit_transform(df_x_te_1)
modeling(gb, ss_x_tn, ss_x_te, y_train, y_test)
# 0.7272 0.7189

# 최종안
# 최종안 1
gb.fit(x_train, y_train)
y_pred=gb.predict(x_test)
df_y_pred=pd.DataFrame(y_pred)
df_y_test=pd.DataFrame(y_test)

print(len(df_y_pred.index))


for i in range(0,2200):
    if df_y_pred.iloc[i, 0]<0.500000:
        df_y_pred.iloc[i,0]=0
    else:
        df_y_pred.iloc[i,0]=1

(roc_auc_score(df_y_test, df_y_pred))
# 0.7172

from sklearn.metrics import confusion_matrix
confusion_matrix(df_y_test, df_y_pred)
# 801, 94
# 601, 704

# 최종안 2
gb.fit(df_x_tn_1, y_train)
y_pred=gb.predict(df_x_te_1)
df_y_pred=pd.DataFrame(y_pred)
df_y_test=pd.DataFrame(y_test)

print(len(df_y_pred.index))


for i in range(0,2200):
    if df_y_pred.iloc[i, 0]<0.500000:
        df_y_pred.iloc[i,0]=0
    else:
        df_y_pred.iloc[i,0]=1

(roc_auc_score(df_y_test, df_y_pred))
# 0.7189

from sklearn.metrics import confusion_matrix
confusion_matrix(df_y_test, df_y_pred)
# 802 93
# 598 707

############# 끝 ############

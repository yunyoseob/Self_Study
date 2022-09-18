# 빅데이터분석기사실기연습 20211129
# 최종모의고사 3회
# 11번 다음은 음주, 흡연과 식도암의 관계를 분석하기 위한 
# 환자와 대조군의 데이터인 R의 esoph 데이터 세트이다.
# 환자 수 (ncases)와 대조군 수(ncontrols)를 합한
# 새로운 칼럼인 관측자 수(nsums)를 생성하고,
# 음주량과 흡연량에 따른 관측자 수(nsums)의
# 이원 교차표(two-way table)를 생성하여
# 확인하고 음주량과 흡연량에 따른 관측자 수(nsums)의
# 카이제곱 값을 구하시오.

import pandas as pd
import numpy as np
import scipy
import sklearn
import xgboost

df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets-master/csv/datasets/esoph.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

# 이원 교차표를 생성, 카이제곱 값 구하기 (?)

#12번 다음은 MASS 패키지의 ChickWeight 데이터 세트이다.
# weight를 최소-최대 척도(Min-Max Scaling)로 변환한 결과가
# 0.5이상인 레코드 수를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/ChickWeight.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
df

from sklearn.preprocessing import MinMaxScaler
mm=MinMaxScaler()

df[["weight"]]=mm.fit_transform(df[["weight"]])
df[['weight']].info()

print(len(df[['weight']].loc[df['weight']>=0.5].index))
# 81

# 13번 문제
# 다음은 mlbench 패키지의 PimalndiansDiabetes2 데이터세트이다.
# glucose, pressure, mass 칼럼의 결측값이 있는 행을 제거하고
# 나이(age)를 조건에 맞게 그룹화 (1:20~40세, 2:41~60세, 3:60세 이상)한 후
# 발병률이 가장 높은 나이 그룹의 발병률을 구하시오. (발병률=diabetes 중 pos의 수/인원 수)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/diabetes2.csv")

df.columns
df.drop("Unnamed: 0", axis=1, inplace=True)
df['diabetes'].value_counts()

df['Age_group']=0
df['age']

len(df.index)
# 768

df.loc[df['age']==60]

null_age=[]

for i in range(0,768):
    if 40>=df['age'][i]>=20:
        df['Age_group'][i]=1
    elif 60>df['age'][i]>=41:
        df['Age_group'][i]=2
    elif df['age'][i]>=60:
        df['Age_group'][i]=3
    else:
        null_age.append(df['age'][i])

for i in range(0,768):
    if df['diabetes'][i]=="neg":
        df['diabetes'][i]=0
    else:
        df['diabetes'][i]=1

# 0: neg, 1: pos

group_1=df.loc[df['Age_group']==1]
group_2=df.loc[df['Age_group']==2]
group_3=df.loc[df['Age_group']==3]
        

def change(g):
    h=g.reset_index()
    i=h.drop("index", axis=1)
    return i


g_1=change(group_1)
g_2=change(group_2)
g_3=change(group_3)

len_g1=len(g_1.index)
len_g2=len(g_2.index)
len_g3=len(g_3.index)

p_1=g_1.loc[g_1['diabetes']==1]
pos_1=change(p_1)
p_2=g_2.loc[g_2['diabetes']==1]
pos_2=change(p_2)
p_3=g_3.loc[g_3['diabetes']==1]
pos_3=change(p_3)

len_p1=len(pos_1.index)
len_p2=len(pos_2.index)
len_p3=len(pos_3.index)

g1_ratio=len_p1/len_g1
g2_ratio=len_p2/len_g2
g3_ratio=len_p2/len_g2

if g1_ratio>g2_ratio:
    if g1_ratio>g3_ratio:
        most=g1_ratio
    else:
        most=g3_ratio
else:
    if g2_ratio<g3_ratio:
        most=g3_ratio
    else:
        most=g2_ratio
        
print(most)
# 0.57407

# 다음은 insurance 데이터 세트이다. 다양한 모형을 이용하여 훈련 데이터를 이용하여
# 데이터를 학습하여 테스트 데이터의 가격(charges)을 가격을 예측하고
# csv 파일로 저장후 제출하시오.
# 채점 기준은 RMSE 값이 낮은 모형
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/insurance.csv")
df
df.info()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['sex']=le.fit_transform(df['sex'])
df['smoker']=le.fit_transform(df['smoker'])
df['region']=le.fit_transform(df['region'])

from sklearn.model_selection import train_test_split
df.columns
x=df.drop("charges", axis=1)
y=df['charges']

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=42)

# Regression
df.corr()
# smoker가 charges와 관련이 매우 높음, 더미변수 고려해볼 것
df['smoker'].value_counts()

# model
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
lr=LinearRegression()
lasso=Lasso(random_state=42)
ridge=Ridge(random_state=42)
en=ElasticNet(random_state=42)

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from xgboost import XGBRegressor
dt=DecisionTreeRegressor(random_state=42)
ada=AdaBoostRegressor(random_state=42)
gb=GradientBoostingRegressor(random_state=42)
rf=RandomForestRegressor(random_state=42)
xgb=XGBRegressor(random_state=42)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

def modeling(model, new_x_tn, x_test, y_train, y_test):
    model.fit(new_x_tn, y_train)
    train_score=model.score(new_x_tn, y_train)
    pred=model.predict(x_test)
    test_score=model.score(x_test, y_test)
    r2=r2_score(y_test, pred)
    rmse=np.sqrt(mean_squared_error(y_test, pred))
    print("train_score :", train_score, "test_score :", test_score, "r2 :", r2, "rmse :", rmse)

# best 3
modeling(lr, x_train, x_test, y_train, y_test)
# train_score : 0.7417049283233981 test_score : 0.7833463107364539 r2 : 0.7833463107364539 rmse : 5799.587091438355
modeling(rf, x_train, x_test, y_train, y_test)
# train_score : 0.9742678958500105 test_score : 0.8640399709835349 r2 : 0.8640399709835349 rmse : 4594.30321576525
modeling(gb, x_train, x_test, y_train, y_test)
# train_score : 0.8980459663933704 test_score : 0.8779726251291786 r2 : 0.8779726251291786 rmse : 4352.538932159728

tn1=pd.get_dummies(x_train['children'], prefix="children")
tn2=pd.get_dummies(x_train['smoker'], prefix="smoker")
tn3=pd.get_dummies(x_train['region'], prefix="region")

tn=pd.concat([tn1,tn2,tn3], axis=1)

new_x_tn_1=x_train.copy()
new_x_tn=pd.concat([new_x_tn_1, tn], axis=1)
new_x_tn

te1=pd.get_dummies(x_test['children'], prefix="children")
te2=pd.get_dummies(x_test['smoker'], prefix="smoker")
te3=pd.get_dummies(x_test['region'], prefix="region")

te=pd.concat([te1,te2,te3], axis=1)

new_x_te_1=x_test.copy()
new_x_te=pd.concat([new_x_te_1, te], axis=1)

# best 2
modeling(gb, new_x_tn, new_x_te, y_train, y_test)
# train_score : 0.8990929514658432 test_score : 0.881889146155949 r2 : 0.881889146155949 rmse : 4282.1209972044435

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
mm=MinMaxScaler()
ss=StandardScaler()
rr=RobustScaler()

scale_tn=mm.fit_transform(new_x_tn)
scale_te=mm.fit_transform(new_x_te)

modeling(gb, scale_tn, scale_te, y_train, y_test)
# train_score : 0.8990929514658432 test_score : 0.8865638753267868 r2 : 0.8865638753267868 rmse : 4196.524092729484 (minmax)

model=GradientBoostingRegressor(random_state=42)
model.fit(scale_tn, y_train)
train_score=model.score(scale_tn, y_train)
pred=model.predict(scale_te)
test_score=model.score(scale_te, y_test)
r2=r2_score(y_test, pred)
rmse=np.sqrt(mean_squared_error(y_test, pred))
print("train_score :", train_score, "test_score :", test_score, "r2 :", r2, "rmse :", rmse)

submit=pd.DataFrame(pred, columns=["charges"])
submit

# submit.to_csv("수험번호.csv", index=False)

# 기출문제 2회
# 11번 문제
# 다음은 BostonHousing 데이터 세트이다.
# crim 항목의 상위에서 10번째 값(즉, 상위 10번째 값중에서 가장 적은 값)으로
# 상위 10개의 값을 변환하고,
# age 80 이상인 값에 대하여 crim 평균을 구하시오.
from sklearn import datasets
import pandas as pd
import numpy as np
import sklearn
import scipy
import xgboost

df_1=datasets.load_boston()

df_1.keys()

df=pd.DataFrame(df_1.data, columns=df_1.feature_names)
df['MEDV']=df_1.target

df_1=df.sort_values(by="CRIM", ascending=False)
df_2=df_1.iloc[:10, :]
df_2=df_2.reset_index()
df_2.drop('index', axis=1, inplace=True)
df_2

min_crim=df_2.iloc[9, 0]
min_crim
# 25.9406

df_1=df_1.reset_index()
df_1.drop("index", axis=1, inplace=True)

for i in range(0,9):
    df_1['CRIM'][i]=min_crim
    
print(df_1.loc[df_1['AGE']>=80]['CRIM'].mean())
# 5.7593

#12번 문제
# 주어진 데이터의 첫 번째 행부터 순서대로 80% 까지
# 의 데이터를 훈련 데이터로 추출 후 "total_bedrooms"변수의
# 결측값(NA)을 "total_bedrooms" 변수의 중앙값으로 대체하고
# 대체 전의 total_bedrooms" 변수 표준편차 값과
# 대체 후의 "total_bedrooms" 변수 표준편차 값의 차이의
# 절댓값을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/handson-ml/datasets/housing/housing.csv")
eight=int(len(df.index)*0.8)
df_1=df.iloc[:eight, :]

df_2=df_1.copy()

before_std=df_1['total_bedrooms'].std()

med=df_2['total_bedrooms'].median()
df_2['total_bedrooms']=df_2['total_bedrooms'].fillna(med)

after_std=df_2['total_bedrooms'].std()

print(np.abs(after_std-before_std))
# 1.97514

# 다음은 Insurance 데이터 세트이다. Charges 항목에서 이상값의 합을 구하시오.
# (이상값은 평균에서 1.5 표준편차 이상인 값)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/insurance.csv")
avg=df['charges'].mean()
std=df['charges'].std()

df_outlier=df.loc[df['charges']>=avg+(1.5*std)]
print(df_outlier['charges'].sum())
# 6421430.0206699995

# 작업형 제 2 유형
# 다음은 iris 데이터 세트이다. 주어진 데이터를 이용하여 Species decision tree, svm 예측 모형을 만든 후
# 높은 Accuracy 값을 가지는 모델의 예측값을 CSV 파일로 제출하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/iris.csv")

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df['Species']=le.fit_transform(df['Species'])

from sklearn.model_selection import train_test_split
x=df.drop('Species', axis=1)
y=df['Species']

x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.5, random_state=42)

from sklearn.tree import DecisionTreeClassifier
rpart=DecisionTreeClassifier(random_state=42)

from sklearn import svm
svm_model=svm.SVC(random_state=42)

from sklearn.metrics import r2_score

rpart.fit(x_train, y_train)
rpart.score(x_train, y_train)
pred=rpart.predict(x_test)

r2_score(y_test, pred)
# 1.0

svm_model.fit(x_train, y_train)
svm_model.score(x_train, y_train)
# 0.9916
pred_2=svm_model.predict(x_test)
r2_score(y_test, pred_2)
# 0.9805

submit=pd.DataFrame(pred, columns=['Species'])
#submit.csv("수험번호.csv", index=False)


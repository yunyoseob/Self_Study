#빅데이터분석기사실기연습20211123
import pandas as pd
import numpy as np
import sklearn
import xgboost

# 빅데이터분석기사 TEST체험하기 작업형 dataframe
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df=df.set_index('model')
print(df.head())
print(df.info())
print(df.columns)
print(df.describe())
print(df.isna().sum())
# 결측치 없음
print(len(df.columns))

# 작업형 1 mtcarrs 데이터셋의 qsec 컬럼을 minmax scale로 변환한 후,
# 0.5보다 큰 값을 가지는 레코드 수를 구하시오. (직접 구하기)
# MinMax Scaler 공식: x_i - min(x) / max(x) - min(x)
print(df['qsec'].describe())
qsec_mean=df['qsec'].mean()
qsec_max=df['qsec'].max()
qsec_min=df['qsec'].min()

df['qsec']=df['qsec'].apply(lambda x:(x-qsec_min)/(qsec_max-qsec_min))
record=[x for x in df['qsec'] if x>0.5]
len_record=len([x for x in df['qsec'] if x>0.5])
print(record[:])
print(len_record)

#sklearn min-max scaler 사용하기
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df=df.set_index('model')

from sklearn.preprocessing import MinMaxScaler
minmax=MinMaxScaler()

df['qsec']=minmax.fit_transform(df[['qsec']])
df['qsec']

record=[x for x in df['qsec'] if x>0.5]
len_record=len([x for x in df['qsec'] if x>0.5])

print(record)
print(len(record))

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

from xgboost import XGBClassifier
xgb=XGBClassifier(random_state=42)

xgb.fit(X_train, Y_train)

y_pred=xgb.predict(X_train)

xgb.score(X_train, Y_train)

y_test_pred=xgb.predict(X_test)
len(y_test_pred)

y_test_pred=pd.DataFrame(y_test_pred, columns=['gender'])
y_test_pred

y_test=y_train
y_test[['gender']]=y_test_pred
y_test.dropna(axis=0, inplace=True)
y_test

# 구름 cloud에서 xgboost error 발생
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(random_state=42)

Y_train=y_train['gender']
model.fit(X_train, Y_train)

print(model.score(X_train, Y_train))

y_pred=model.predict(X_test)
y_pred=pd.DataFrame(y_pred, columns=['gender'])

y_test=y_train
y_test['gender']=y_pred['gender']
y_test.dropna(axis=0, inplace=True)
y_test


# 심화과정(코드 참고해서 기술)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

logi=LogisticRegression(random_state=42)
gb=GradientBoostingClassifier(random_state=42)
rf=RandomForestClassifier(random_state=42)
ab=AdaBoostClassifier(random_state=42)

x_train, x_test, y_train, y_test=train_test_split(X_train, Y_train['gender'], test_size=0.2, random_state=42)
logi.fit(x_train, y_train)
print(logi.score(x_train, y_train))
# 0.6275
y_pred=logi.predict(x_test)
print(roc_auc_score(y_test, y_pred))
# 0.5

gb.fit(x_train, y_train)
print(gb.score(x_train, y_train))
# 0.73
y_pred=gb.predict(x_test)
print(roc_auc_score(y_test, y_pred))
# 0.57

rf.fit(x_train, y_train)
print(rf.score(x_train, y_train))
# 1.0
y_pred=rf.predict(x_test)
print(roc_auc_score(y_test, y_pred))
# 0.58

ab.fit(x_train, y_train)
print(ab.score(x_train, y_train))
# 0.68
y_pred=ab.predict(x_test)
print(roc_auc_score(y_test, y_pred))
# 0.5899

xgb.fit(x_train, y_train)
print(xgb.score(x_train, y_train))
# 0.99285
y_pred=xgb.predict(x_test)
print(roc_auc_score(y_test, y_pred))
# 0.55917

from xgboost import XGBClassifier
xgb=XGBClassifier(random_state=42)
xgb.fit(X_train, Y_train)

print(xgb.score(X_train, Y_train))

y_test=y_train

y_pred=xgb.predict(X_test)
y_pred=pd.DataFrame(y_pred, columns=['gender'])

print(y_pred)

y_test['gender']=y_pred['gender']
y_test.dropna(axis=0, inplace=True)

print(y_test.info())


y_test['gender']=y_test['gender'].astype(int)
y_test









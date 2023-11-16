# Kafka 1편

- 발표 일자 : 2022.11.06

- [참고한 도서 : 실전 카프카 개발부터 운영까지](https://github.com/onlybooks/kafka2)

<img src="https://camo.githubusercontent.com/52a8678699c5cdd6436d8b302d3ccb4a58f0d094f058f255a4f7918e92283875/68747470733a2f2f696d67312e6461756d63646e2e6e65742f7468756d622f523132383078302f3f73636f64653d6d746973746f72793226666e616d653d6874747073253341253246253246626c6f672e6b616b616f63646e2e6e6574253246646e2532464f75774d6a2532466274726850426372633372253246416b74316137517758616d4b574271424c784331554b253246696d672e706e67" height=300, width=270>

## 1. Kafka란?

```
아파치 카프카(Apache Kafka)는 아파치 소프트웨어 재단이 스칼라로 개발한 오픈 소스 메시지 브로커 프로젝트이다. 이 프로젝트는 실시간 데이터 피드를 관리하기 위해 통일된, 높은 처리량, 낮은 지연시간을 지닌 플랫폼을 제공하는 것이 목표이다.
```

**✔ [IfUwanna IT 블로그를 통해 보는 카프카](https://ifuwanna.tistory.com/487)**


## 2. kafka 탄생배경

링크드인에서 링크드인 내부에서 발생하고 있는 이슈들을 해결하기 위해 만듬.

**✔ [춤추는 개발자 블로그를 통해 보는 링크드인과 카프카 탄생 배경](https://log-laboratory.tistory.com/143)**

## 3. 카프카 이용 현황 사례

**✔ 국내 카프카 이용 현황 사례**

```
2018년 카카오는 총 7개의 클러스터를 보유하고 있고, 하루 2600억 개의 메시지를 처리하며, 하루 약 240TB의 데이터가 카프카로 유입된다고 밝힌바 있음.
```

**✔ 해외 카프카 이용 사례**

1. [넷플릭스 사례](https://netflixtechblog.com/evolution-of-the-netflix-data-pipeline-da246ca36905)

<img src="https://miro.medium.com/max/720/0*twzMM1i4zLCilScl.">

2. [머신러닝 분야 활용 사례](https://www.confluent.io/blog/build-deploy-scalable-machine-learning-production-apache-kafka/)

<img src="https://cdn.confluent.io/wp-content/uploads/Kafka-Producer-Consumer.png">

<img src="https://cdn.confluent.io/wp-content/uploads/ML-architecture.png">


## 4. 카프카의 주요 특징

4-1. 높은 처리량과 낮은 지연시간

![image](https://user-images.githubusercontent.com/81727895/199721289-ab2f8cfc-a684-403d-9dda-661487391587.png)

4-2. 높은 확장성

- 손쉽게 확장이 가능하다.

4-3. 고가용성

- 고가용성을 갖추면서도 지연 없는 빠른 메시지 처리 기능

4-4. 내구성

카프카로 전송되는 모든 메시지는 안전한 저장소인 카프카의 로컬 디스크에 저장(과거의 메시지를 볼 수 있다.)

- 장애 대처가 유용하다

4-5. 개발 편의성

메시지를 보내는 프로듀서와 메시지를 가져오는 역할을 하는 컨슈머의 완벽한 분리

4-6. 운영 및 관리 편의성

## 5. Kafka 실습

### 5-1. 가상환경 setting(VMware)

**✔ [Kafka 실습 (1) - 환경설정](https://jeffrey-oh.tistory.com/358)**

**✔ [Kafka 과제 참고](https://github.com/yunyoseob/RedWoodK/tree/master/assignment/Staff/Kafka_%EA%B3%BC%EC%A0%9C)**

### 5-2. Zookeper & Kafka 설치

**✔ [youtube 빅공쟁 Kaka 클러스터 환경 구축 Zookeeper 설치 및 환경 설정](https://www.youtube.com/watch?v=2bNEKDx-5Rg&list=PLJlUnZ1kDbt6rN-pf_4jxPSWuP4BeK4pk&index=4)**

**✔ [youtube 빅공쟁 Kaka 클러스터 환경 구축 Kafka 설치 및 환경 설정](https://www.youtube.com/watch?v=dGCGV1wFrv0&list=PLJlUnZ1kDbt6rN-pf_4jxPSWuP4BeK4pk&index=5)**
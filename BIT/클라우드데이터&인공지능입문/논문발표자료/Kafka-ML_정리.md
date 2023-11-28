# Kafka-ML: connecting the data stream with ML/AI frameworks

작성일: 2023.11.28 
작성자: 비즈니스IT전공 윤요섭

# 키워드 정리

## ✔️ Contents


✨ Section1: 
``````
- The presentation of Kafka-ML, an open-source, acces-sible and user-friendly framework to manage ML/AI pielines through data streams

- A novel approach to manage the data streams of ML/AI pipelines with (no) need for data storage or file systems.
``````

✨ Section2:
``````
A background of Kafka-ML 
``````


✨ Section3:

``````
The motivation of this work
``````

✨ Section4:
``````
The ML/AI pipeline of Kafka-ML is introduced.
``````

✨ Section5:
``````
Kafka-ML architecture and its components are presented. 
``````

✨ Section6:
``````
The approach for data stream management in Apach Kafka is presented
``````

✨ Section7:
``````
A validation of Kafka-ML is analyzed
``````

✨ Section8:
```
related work is discussed
```

✨ Section9:
```
conclusions and future work
```

## Section 1: Introduction


추후 작성

## Section 2: Back Ground

Apache Kafka란?

대량의 메시지를 전달하고 소비할 수 있는 분산 메시지 시스템(pub/sub) 

high availability

low latency

Load balancing

추후 작성

## Section 3: Back Ground

ML 프레임워크의 대부분은 데이터 스트림과 함꼐 작동하도록 설계되지 않음

수신 데이터를 예측할 수 있는 추론 뿐 아니라 ML/AI 파이프라인의 교육 및 평가 단계를 위한 데이터 스트림 수집도 포함

Data Stream <-> ML Framework 격차를 줄이고, AutoML 기능을 채택하고, 고성능 및 고가용성 인프라에서 ML모델, 측정항목 및 결과를 공유할 수 있는 시스템 구상

##  Section4: Pipeline of an ML model in Kafka-ML

```
A) designing and defining the ML model

B) Creating a training configuration of ML model

C) deploying the configuration for training

D) ingesting the deployed configuration with training and optionally evaluation stream data through Apache Kafka

E) deploying the trained model for inference

F) feeding the deployed trained model for inference to make predictions with data streams

- 이전 단계의 대부분은 RESTful API를 사용하므로, 파이프라인은 자동화 될 수 있으며, 이와 관련된 모든 단계는 ML 모델 공급(훈련 및 추론)이 수행
```

✔️ 각 단계별 고려사항

**A. Designing and defining ML models**

ML 개발자가 ML 모델에 집중할 수 있도록 최대한 간단하게 만듬

- Example ML code for Kafka-ML

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, input_dim =100, activation=tf.nn.relu),
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)])

model.compile(optimitzer='adam', loss='sparse_categorical_crossentropy' , metrics=['accuracy'])
```

**B. Creating a configuration**

A configuration is a logical set of Kafka-ML models that can be grouped for training.

This can be useful when it is required to evalute and compare metrics of a set of Kafka-ML models or just to define a group of then can be trained with the same and unique data stream in parallel.

**C. Deploying the configuration for training**

training parameters 설정이 끝나면, Kafka-ML 모델별로 작업이 배포

Kafka-ML 아키텍처에서 해당 ML 모델을 가져와서 로드하여 훈련을 시작

**D. Ingesting the deployment with stream data**

스트림 데이터를 사용하여 배포 수집 모델이 배포되면 파이프라인을 계속하기 위해 훈련을 위해 데이터 스트림을 보내야 함.

```
2개의 Kafka Topic 사용

1.  data topic(s) which only contain training and evaluation data streams required for training and evaluation

2. informs deployed ML models
through control messages when and where the data streams are
available for training and evaluation
```
- Section 5에서 더 자세히 다룰 예정


**E. Deploying trained models for inference**

훈련 및 평가 직후, 훈련된 모델 자체와 정의된 측정 항목이 Kafka-ML 아키텍처에 제출됨.

사용자는 배포할 추론 replica를 선택할 수 있음.

Apache Kafka의 Consumer Group을 통해 추론을 위한 로드밸런싱 및 내결함성 활성화

**F. Ingesting the deployed trained models with stream data for inference**

사용자와 시스템은 입력 토픽에 정의된 데이터 형식으로 인코딩된 데이터 스트림을 전송하기만 하면 되며, 모델 예측이 구성된 출력 토픽에 대한 추론 결과가 즉시 전송된다.

##  Section5: Kafka-ML ARCHITECTURE

Kafka-ML 아키텍처는 MSA를 구성하는 SRP(단일책임원칙)을 기반으로 하는 구성 요소 집합으로 구성

모든 구성 요소는 Docker 컨테이너로 실행될 수 있도록 컨테이너화

Kubernetes와 같은 컨테이너 오케스트레이션 플랫폼을 통한 관리 및 모니터링도 가능

Kubernetes는 컨테이너와 해당 replica를 지속적으로 모니터링하여 정의된 상태와 지속적으로 일치하는지 확인하는 동시에 고가용성 및 로드 밸런싱과 같은 프로덕션 환경에 대한 기타 기능을 허용

Kubernetes는 Kafka-ML 및 해당 구성 요소의 수명 주기를 관리
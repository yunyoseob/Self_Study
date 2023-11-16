# Kafka 실습

## 가상환경 구성

### 1. Window에서 가상 머신인 VMWare를 설치하여 가상 환경을 구성합니다.

### 2. VMWare를 설치 한 뒤, 3대의 kafka 실습 서버 환경을 구축합니다.

![image](https://user-images.githubusercontent.com/81727895/201528485-0035b8de-8dbe-4bc3-95fe-5fd04df7ab4e.png)

### 3. 각 서버에 apache-zookeeper-3.6.3-bin.tar.gz와 kafka_2.13-3.31.tgz 파일을 다운 받은 뒤, 압축을 해제 하여 줍니다.

```
[root@kafka01 app]# ls
apache-zookeeper-3.6.3-bin.tar.gz  kafka_2.13-3.3.1.tgz
```

### 4. 압축을 푼 zookeeper에서 conf 디렉토리 안에 zoo.cfg 파일을 만든 뒤, 필요한 정보를 입력하여 줍니다.

```=2000
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/usr/local/zookeeper/data
dataLogDir=/usr/local/zookeeper/logs
maxClientCnxns=0
clientPort=2181
server.1=kafka01:2888:3888
server.2=kafka02:2888:3888
server.3=kafka03:2888:3888
```

- dataDir 경로에 myid 파일을 만들어 주고, 각 id를 부여합니다.

```
kafka01 : 1
kafka02 : 2
kafka03 : 3
```

### 5. config 디렉토리 안에 zookeeper.properties를 설정한 뒤, Zookeeper service를 시작합니다.

```
dataDir=/usr/local/zookeeper/data
clientPort=2181
maxClientCnxns=0
tickTime=2000
initLimit=10
syncLimit=5
server.1=192.168.112.130:2888:3888
server.2=192.168.112.131:2888:3888
server.3=192.168.112.129:2888:3888
```

- Zookeeper service 시작

```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

- Zookeeper service 시작 화면

![image](https://user-images.githubusercontent.com/81727895/201697183-4fbc4541-9baa-4990-84e5-e176a1c95178.png)



### 6. 압축을 푼 kafka에서 config 디렉토리 안에 server.properties를 설정합니다.

```
broker.id=1
listeners=PLAINTEXT://:9092
...
zookeeper.connect=192.168.112.130:2181,192.168.112.131:2181,192.168.112.129:2181
...
delete.topic.enable=true
auto.create.topics.enable=false
```

- 각 서버 마다 broker.id는 다르게 설정합니다.

```
kafka01 : 1
kafka02 : 2
kafka03 : 3
```

### 7. 다른 터미널을 열어 Kafka Broker service를 시작합니다.

```
bin/kafka-server-start.sh config/server.properties
```

**💻 Terminal log**

- kafka01

```
[2022-11-14 23:47:21,375] INFO [KafkaServer id=1] started (kafka.server.KafkaServer)

[2022-11-14 23:47:21,528] INFO [BrokerToControllerChannelManager broker=1 name=alterPartition]: Recorded new controller, from now on will use broker 192.168.112.130:9092 (id: 1 rack: null) (kafka.server.BrokerToControllerRequestThread)
```

- kafka02

```
[2022-11-14 23:47:22,113] INFO [KafkaServer id=2] started (kafka.server.KafkaServer)

[2022-11-14 23:47:22,361] INFO [BrokerToControllerChannelManager broker=2 name=forwarding]: Recorded new controller, from now on will use broker 192.168.112.130:9092 (id: 1 rack: null) (kafka.server.BrokerToControllerRequestThread)
```

- kafka03

```
[2022-11-14 23:47:24,870] INFO [KafkaServer id=3] started (kafka.server.KafkaServer)

[2022-11-14 23:47:25,053] INFO [BrokerToControllerChannelManager broker=3 name=alterPartition]: Recorded new controller, from now on will use broker 192.168.112.130:9092 (id: 1 rack: null) (kafka.server.BrokerToControllerRequestThread)
```


### 8. 토픽을 생성합니다.

```
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```

**💻 Terminal log**

```
Created topic test.
```

**✔ 토픽 리스트 확인하기**

```
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
- 출력 결과 : test

### 9. 메시지 주고 받기

- bin/kafkap-console-producer.sh 실행시키기

```
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test

> RedwoodK
```

- bin/kafka-console-consumer.sh 실행시키기

```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

- 출력 결과

```
RedWoodK
```

### 10. 다중 브로커 활용

```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 1 --topic my-replicated-topic
```

- 토픽 확인 해보기

```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 1 --topic my-replicated-topic
```

- 출력 결과

```
Topic: my-replicated-topic	TopicId: JYFby8CBS2eQ35Hph9l2pA	PartitionCount: 1	ReplicationFactor: 3	Configs: 
	Topic: my-replicated-topic	Partition: 0	Leader: 2	Replicas: 2,1,3	Isr: 2,1,3
```

- producer와 consumer로 여러 메시지 주고 받기

```
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic my-replicated-topic

> redwoodk1
> redwoodk2
> redwoodk3
> kafka test
```

```
bin/kafka-console-consumer.sh --bootstrap-server localh:9092 --from-beginning --topic my-replicated-topic
```

- 출력 결과

```
redwoodk1
redwoodk2
redwoodk3
kafka test
```

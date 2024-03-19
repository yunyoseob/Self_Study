# 도커

## 도커 엔진: 컨테이너 자원 할당 제한

**#1. 컨테이너 상세 정보 확인**

```
docker inspect 
```

**#2. 컨테이너 자원 제한 변경**

```
docker update (변경할 자원 제한) (컨테이너 이름)

docker update --cpuset-cpus=1 centos ubuntu
```

**#3. 컨테이너 메모리 제한**

--memory를 지정: 최소 메모리는 6MB

```
docker run -d --memory="1g" --name memory_1g nginx
# 메모리를 1GB로 제한
```

**#4. 컨테이너 CPU 제한**

--cpu-shares: 컨테이너에 가중치를 설정해 해당 컨테이너가 CPU를 상대적으로 얼마나 사용할 수 있는지를 나타냄. 즉, 시스템에 존재하는 CPU를 어느 비중만큼 나눠(share) 쓸 것인지를 명시하는 옵션

```
docker run -i -t --name cpu_share
--cpu-shares 1024
ubuntu:14.04
# 아무런 설정을 하지 않았을 때, 컨테이너가 가지는 값은 1024로, CPU 할당에서 1의 비중을 의미
```

--cpuset-cpus: 호스트에 CPU가 여러 개 있을 때, 컨테이너가 특정 CPU만 사용하도록 설정할 수 있음.

```
docker run -d --name cpuset_2 --cpuset-cpus=2 \
# 컨테이너가 3번째 CPU만 사용하도록 설정
```

--cpu-period, --cpu-quota: 컨테이너의 CFS(Completely Fair Scheduler) 주기 변경

```
docker run -d --name quota_1_4 \
--cpu-period=100000 \
--cpu-quota=25000 \ 
# 컨테이너의 CFS 주기는 기본적으로 100ms 설정
# --cpu-period=100000는 100ms를 뜻함
# --cpu-quota는 --cpu-period 중 설정값 만큼 할당할 것을 의미
# --cpu-quota=25000는 100000 중 25000만큼 할당해 CPU 주기가 1/4로 줄게 한 것
# 일반적인 컨테이너보다 CPU 성능이 1/4정도로 감소
```

--cpus: CPU의 개수를 직접 지정

```
docker run -d --name cpus_container \
--cpus=0.5

# CPU 개수를 0.5개 사용한다
# --cpu-period=100000 \ --cpu-quota=500000 과 동일함
```

**5. Block I/O 제한**

컨테이너 내부에서 파일을 읽고 쓰는 대역폭 제한 (하나의 컨테이너가 블록 입출력을 과도하게 사용하지 않게 설정하기 위함)

```
--device 옵션은 [디바이스 이름]:[값] 형태로 설정해야 함.
```

--device-write-bps /dev/xvda:1mb: 초당 쓰기 작업의 최대치가 1mb로 제한, /dev/xvda는 디바이스를 의미

```
docker run -it --device-write-bps /dev/xvda:1mb ubuntu:14.04
```

--device-write-iops, --device-read-iops: 수행시간의 상대적인 값을 의미

```
docker run -it --device-writer-iops /dev/xvda:5 ubuntu:14.04
# 2.02602s, 5.2 MB/s

docker run -it --device-writer-iops /dev/xvda:5 ubuntu:14.04
# 1.02254s, 10.3 MB/s
```
# Docker 실습

## Container 생성 실습

**✔️ 도커 버전 확인**

```bash
yun@test01:/var/run$ docker -v
Docker version 25.0.4, build 1a576c5
```

**✔️ 컨테이너 생성해보기**

- docker run :  컨테이너를 생성하고 실행하는 역할

```bash
yun@test01:~$ docker run -i -t ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
14.04: Pulling from library/ubuntu
2e6e20c8e2e6: Pull complete
0551a797c01d: Pull complete
512123a864da: Pull complete
Digest: sha256:******
Status: Downloaded newer image for ubuntu:14.04
root@163e37e1f7b8:/#
```
ubuntu:14.04: 컨테이너를 생성하기 위한 이미지

-i -t : 컨테이너와 상호(interactive) 입출력을 가능하게 함

**✔️ 컨테이너에서 빠져나오기**

1. exit 혹은 Ctrl + D: 컨테이너 내부에서 빠져나오면서 동시에 컨테이너 정지

2. Ctrl + P 혹은 Ctrl + Q: 컨테이너의 셸에서만 빠져나옴


**✔️ 이미지 받아오기**

```bash
yun@test01:~$ docker pull centos:7
7: Pulling from library/centos
2d473b07cdd5: Pull complete
Digest: sha256:******
Status: Downloaded newer image for centos:7
docker.io/library/centos:7
yun@test01:~$
yun@test01:~$
yun@test01:~$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
centos       7         eeb6ee3f44bd   2 years ago   204MB
ubuntu       14.04     13b66b487594   2 years ago   197MB
```

docker pull : 이미지를 내려받을 때 사용

docker images : 도커 엔진에 존재하는 이미지의 목록을 출력

**✔️ create 명령어로 컨테이너 생성하기**

```bash
yun@test01:~$ docker create -i -t --name mycentos centos:7
e165ec6d2eec....
```
e165ec6d2eec.... :  컨테이너의 고유 ID로 앞의 12자리만 사용 (docker inspect 명령어로 컨테이너 ID를 다시 확인 할 수 있음)

```bash
yun@test01:~$ docker start mycentos
mycentos
yun@test01:~$ docker attach mycentos
[root@e165ec6d2eec /]#
```

docker start : 컨테이너 시작

docker attach : 컨테이너 내부로 들어가는 명령어

**run 명령어, create 명령어 차이**

run 명령어는 pull, create, start 명령어를 일괄적으로 실행 후, attach가 가능한 컨테이너라면 컨테이너 내부로 들어감.

create 명령어는 도커 이미지를 pull한 뒤, 컨테이너 생성만 함. start, attach를 실행하지 않음

**✔️ Ctrl + P, Q를 입력해 컨테이너에서 나온 뒤, 목록 확인**

```bash
[root@e165ec6d2eec /]# read escape sequence
yun@test01:~$ 
yun@test01:~$ docker ps
CONTAINER ID   IMAGE      COMMAND       CREATED         STATUS         PORTS     NAMES
e165ec6d2eec   centos:7   "/bin/bash"   5 minutes ago   Up 3 minutes             mycentos
yun@test01:~$
yun@test01:~$ docker ps -a
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                     PORTS     NAMES
e165ec6d2eec   centos:7       "/bin/bash"   5 minutes ago    Up 3 minutes                         mycentos
163e37e1f7b8   ubuntu:14.04   "/bin/bash"   11 minutes ago   Exited (0) 9 minutes ago             boring_dijkstra
```

docker ps : 정지되지 않은 컨테이너만 출력

docker ps -a : 정지된 컨테이너를 포함한 모든 컨테이너 출력

**✔️ 컨테이너 삭제**

```bash
yun@test01:~$ docker ps -a
CONTAINER ID   IMAGE          COMMAND               CREATED          STATUS                      PORTS     NAMES
51d1486f399a   ubuntu:14.04   "echo hello world!"   25 seconds ago   Exited (0) 24 seconds ago             eager_lederberg
e165ec6d2eec   centos:7       "/bin/bash"           8 minutes ago    Up 6 minutes                          mycentos
163e37e1f7b8   ubuntu:14.04   "/bin/bash"           14 minutes ago   Exited (0) 12 minutes ago             boring_dijkstra
yun@test01:~$
yun@test01:~$ docker rm eager_lederberg
eager_lederberg
yun@test01:~$
yun@test01:~$ docker ps -a
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                      PORTS     NAMES
e165ec6d2eec   centos:7       "/bin/bash"   8 minutes ago    Up 7 minutes                          mycentos
163e37e1f7b8   ubuntu:14.04   "/bin/bash"   14 minutes ago   Exited (0) 12 minutes ago             boring_dijkstra
yun@test01:~$
yun@test01:~$ docker stop mycentos
mycentos
yun@test01:~$
yun@test01:~$ docker rm mycentos
mycentos
yun@test01:~$
yun@test01:~$ docker ps -a
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                      PORTS     NAMES
163e37e1f7b8   ubuntu:14.04   "/bin/bash"   16 minutes ago   Exited (0) 14 minutes ago             boring_dijkstra
```
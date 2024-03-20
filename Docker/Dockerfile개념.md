# 도커

## Dockerfile

**#1. Dockerfile 명령어**

1) FROM: 생성할 이미지의 베이스가 될 이미지를 뜻합니다. FROM 명령어는 Dockerfile을 작성할 때 반드시 한 번 이상 입력해야 하며, 
이미지 이름의 포맷은 docker run 명령어에서 이미지 이름을 사용했을 때와 같습니다. 사용하려는 이미지가 도커에 없다면 자동으로 pull합니다.

2) RUN: 이미지를 만들기 위해, 컨테이너 내부에서 명령어를 실행합니다. 이미지를 빌드할 때 별도의 입력을 받아야 하는 RUN이 있다면 build 명령어는 이를 오류로 간주하고 빌드를 종료합니다.

3) ADD: 파일을 이미지에 추가합니다. 추가하는 파일은 Dockerfile이 위치한 디렉터리인 컨텍스트(Context)에서 가져옵니다. Dockerfile이 위치한 디렉토리에서 파일을 가져옵니다.

4) WORKDIR: 명령어를 실행할 디렉터리를 나타냅니다. (리눅스에서 cd 명령어와 같음)

5) CMD: 컨테이너가 시작될 때마다 실행할 명령어(커맨드)를 설정하며, Dockerfile에서 한 번만 사용할 수 있습니다.

6) ENV: Dockerfuile에서 사용될 환경변수를 지정

7) COPY: 로컬 디렉토리에서 읽어들인 컨텍스트로부터 이미지에 파일을 복사하는 역할 (ADD와 달리 로컬 파일만 이미지에 추가할 수 있음)

8) VOLUME: 빌드된 이미지로 컨테이너를 생성했을 때 호스트와 공유할 컨테이너 내부의 디렉터리를 설정

9) ARG:build 명령어를 실행할 때 추가로 입력을 받아 Dockerfile 내에서 사용될 변수의 값을 설정

10) USER: 아래 명령어를 해당 사용자의 권한으로 실행


**#2. Dockerfile 빌드**

```
docker build -t mybuild:0.0 ./
# -t 옵션은 생성될 이미지의 이름을 설정함. 설정하지 않을 시, 16진수 형태의 이름으로 이미지 저장
# mybuild:0.0은 생성될 이미지의 이름
```

Dockerfile을 읽어 들인다면 해당 저장소(Repository)에 있는 파일과 서브 모듈을 포함합니다.

따라서, Dockerfile이 위치한 곳에는 이미지 빌드에 필요한 파일만 있는 것이 바람직합니다.

.dockerignore파일을 통해 빌드 시 파일에 명시된 이름의 파일을 컨텍스트에서 제외할 수 있습니다. (Dockerfile이 위치한 경로와 같은 곳에 위치해야 함. 컨텍스트의 최상위 경로)

**#3. Docker Cache**

한 번 이미지를 빌드를 마치고 난 뒤 다시 같은 빌드를 진행하면 이전의 이미지 빌드에서 사용했던 캐시를 사용

내용이 같은 경우, 별도의 빌드 과정이 진행되지 않고도 이미지를 빌드 할 수 있음.

그러나, cache를 사용하면, RUN git clone ~ 같은 명령어 실행시 소스 코드의 변경부분을 반영할 수 없음

이런 경우를 대비하여, 캐시를 사용하지 않는 옵션이 있다.

```
docker build --no-cache -t mybuild:0.0 .
```

또는 캐시로 사용할 이미지를 직접 지정하는 방법도 있다.

```
docker build --cache-from nginx -t my_extend_nginx:0.0 .
# 도커 허브의 nginx 공식 저장소에서 nginx:latest 이미지를 빌드하는 Dockerfile에 일부 내용을 추가해 사용한다면 로컬의 nginx:latest 이미지를 캐시로 사용할 수 있음.
```

**#3. ENTRYPOINT**

ENTRYPOINT는 컨테이너가 시작될 때 수행할 명령을 지정 (CMD와는 다르게 커맨드를 인자로 받아 사용할 수 있는 스크립트의 역할을 할 수 있다.)

```
# ENTRYPOINT를 사용하는 Dockerfile
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
```

```
# entrypoint.sh
echo $1 $2
apachetl -DFOREGROUND
# 아파치 웹 서버 실행하는 내용
```
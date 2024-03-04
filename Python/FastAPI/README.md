# Fast API

## FastAPI를 사용한 파이썬 웹 개발 

<img src="https://www.hanbit.co.kr/data/books/B9703548802_l.jpg">

해당 도서를 참고하여 환경 구성 및 실습을 진행하였음.

## Configuration

**1. 가상환경 접속 스크립트** 

```
.\venv\Scripts\activate
```

**2. 애플리케이션 시작**

```
uvicorn main:app --port 8000 --reload
```

**3. REST API Test** 

```
# httpie 설치
 http -v GET http://127.0.0.1:8000/
```

- [httpie docs](https://httpie.io/docs/cli/url-shortcuts-for-localhost)



## Event Planner Application(Fast API Application)



**Project Structure**

```
planner/
    main.py
    database/
        __init__.py
        connection.py
    routes/
        __init__.py
        events.py
        users.py
    models/
        __init__.py
        events.py
        users.py
```

**File description**

```
    routes/
        events.py: 이벤트 생성, 변경, 삭제 등의 처리를 위한 라우팅
        users.py : 사용자 등록 및 로그인 처리를 위한 라우팅
    models/
        events.py: 이벤트 처리용 모델을 정의
        users.py : 사용자 처리용 모델을 정의
```

**Route Description**

```
사용자: /user
          ㄴ /signup
          ㄴ /signin
          ㄴ /siginout
        
이벤트: /event
        ㄴ /new
        ㄴ / , /{id}
        ㄴ /{id} 
        ㄴ /{id}
```

|router|하위 router|Description|
|--|--|--|
|/user|/signup|사용자 등록|
|/user|/signin|사용자 로그인|
|/user|/||
|/event|/new|이벤트 생성|
|/event|/, /{id}|이벤트 조회|
|/event|/{id}|이벤트 변경|
|/event|/{id}|이벤트 삭제|
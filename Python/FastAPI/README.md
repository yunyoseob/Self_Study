# Fast API

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




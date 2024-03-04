from fastapi import FastAPI 
from routes.users import user_router
from routes.events import event_router
import uvicorn

app = FastAPI()

# 라우트 등록
# 사용자(users) router
app.include_router(user_router, prefix="/user")

# 이벤트(events) router
app.include_router(event_router, prefix="/event")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
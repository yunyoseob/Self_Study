from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 사용자 모델
# email: 사용자 이메일
# password: 사용자 패스워드
# events: 해당 사용자가 생성한 이벤트 (처음에는 비어 있다.)
class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]
    # 데이터를 어떻게 저장하고 설정하는지 보여주는 샘플 데이터 생성
    class Config:
        schema_extra={
            "example":{
                "email":"fastapi@packt.com",
                "username":"strong!!!",
                "events":[],
            }
        }

# 사용자 로그인 모델
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    class Config:
        schema_extra={
            "example":{
                "email":"fastapi@packt.com",
                "password":"strong!!!",
                "events":[],
            }
        }

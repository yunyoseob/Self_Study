from pydantic import BaseModel
from typing import List

# 이벤트 모델
# id: 자동 생성되는 고유 식별자
# title: 이벤트 타이틀
# image: 이벤트 이미지 배너의 링크
# description: 이벤트 설명
# tags: 그룹화를 위한 이벤트 태그
# location: 이벤트 위치
class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    # Event 클래스 안에 Config 서브 클래스 추가 : 문서화할 때 샘플 데이터를 보여주기 위한 용도
    class Config:
       schema_extra = {
           "example": {
               "title":"FastAPI Book Launch",
               "image":"https://linktomyimage.com/image.png",
               "description":"We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
               "tags":["python","fastapi","book","launch"],
               "location":"Google Meet"
           }
       }

from django.db import models
"""
CREATE TABLE 명령어 없이 ORM 방식으로 생성
Create your models here.
REQ-003. 테이블은 2개 필요
  - Question 테이블
  - Choice 테이블 
테이블을 만 든 뒤, Admin 사이트에 보이도록 등록 (admin.py 파일에 등록)
"""

# Question 테이블 컬럼과 클래스 변수 간의 매핑
# columns: id(integer), question_text(varchar(200)), pub_date(date_time)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 객체를 문자열로 표현할 때 사용하는 함수 (없으면 테이블 명이 제대로 표시되지 않음)
    def __str__(self):
        return self.question_text
    
# Choice 테이블 컬럼과 클래스 변수 간의 매핑
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
"""
models.py 모듈에 정의한 테이블을 migrate 명령으로 데이터베이스에 반영할 떄, 장고가 사용하는 SQL 문장 확인하기
$ python manage.py sqlmigrate polls 0001
BEGIN;
-- Create model Question
--
CREATE TABLE "polls_question" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "question_text" varchar(200) NOT NULL, 
  "pub_date" datetime NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "choice_text" varchar(200) NOT NULL, 
  "votes" integer NOT NULL, 
  "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
"""
from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
# models.py에서 작성한 클래스를 admin.py에서 admin.site.register() 함수를 통해 Admin 사이트에 등록
admin.site.register(Question)
admin.site.register(Choice)

"""
# models.py에서 테이블 생성 후, admin.py에서 register 한 뒤, 변경사항을 데이터베이스에 반영
$ python manage.py makemigrations
Migrations for 'polls':
  polls\migrations\0001_initial.py
    - Create model Question       
    - Create model Choice
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
"""
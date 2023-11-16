from django.urls import path
from polls import views

"""
REQ-002. index.html, detail.html, results.html 3페이지 제작 필요
  - index.html은 질문이 담겨있어야 함
  - detail.html은 답변 항목이 있어야 함
  - result.html은 투표 결과를 보여줘야 함
"""
# vote의 경우 리다이렉션 처리를 위한 로직
# path() parameters 
#  필수: route(URL String), view(URL String 매칭시 call function)
#  선택: , kwrags(URL스트링에서 추출된 항목 외의 추가적인 인자를 뷰 함수에 전달 시 정의<여기선 사용 X>), name(URL 패턴별 이름)
app_name='polls'
urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:question_id>/', views.detail, name='detail'), 
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
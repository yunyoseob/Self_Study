## MVT 코딩 순서

View: Controller의 역할

Template: 사용자에게 보여주는 화면

```
1.  프로젝트 뼈대 만들기: 프로젝트 및 앱 개발에 필요한 디렉토리와 파일 생성

2. 모델 코딩하기: 테이블 관련 사항을 개발(models.py, admin.py)

3. URLconf 코딩하기: URL 및 뷰 매핑 관계를 정의 (urls.py)

4. 템플릿 코딩하기: 화면 UI 개발 (templates/ 디렉토리 하위의 *.html 파일들)

5. 뷰 코딩하기: 애플리케이션 로직 개발 (views.py)
```

## 요구사항

```
REQ-001. 설문에 해당하는 질문을 보여준 후 질문에 포함되어 있는 답변 항목에 투표하면 그 결과를 알려주는 프로그램

REQ-002. index.html, detail.html, results.html 3페이지 제작 필요
  - index.html은 질문이 담겨있어야 함
  - detail.html은 답변 항목이 있어야 함
  - result.html은 투표 결과를 보여줘야 함

REQ-003. 테이블은 2개 필요
  - Question 테이블
  - Choice 테이블
```
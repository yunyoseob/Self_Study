# Maven Study

<hr>

### 1. Maven이란?

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 1강 - 메이븐(Maven)이란? ](https://www.youtube.com/watch?v=VAp0n9DmeEA&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=3)

빌드 툴(빌드할 때 사용할 수 있는 도구)

**✔ 프로젝트 빌드 과정**

1. 프로젝트 생성
2. 라이브러리 설정
3. 코드 작업
4. 컴파일
5. 테스트
6. 패키지 만들기
7. 배포
8. 레포팅

이 과정을 Maven이 효율적으로 할 수 있도록 도와준다.

빌드 도구는 IDE의 부분 집합니다.

**✔ 형상 관리 : Git, CVS**

**✔ 프로젝트 빌드 도구 : Maven, Gradle, Ant**

**✔ 테스트를 위한 도구 : JUnit**

**✔ 이클립스가 제공하지 않는 Maven만의 기능**

1. 프로젝트 생성 : **사용자 정의 프로젝트**
2. 라이브러리 설정 : **라이브러리 관리와 의존성 체크**
3. 코드 작업
4. 컴파일
5. 테스트
6. 패키지 만들기
7. 인스톨
8. 배포 : **라이브러리 저장소 활용**
9. 레포팅

### 2. Maven 설치하기

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 2강 - 메이븐 설치하기 ](https://www.youtube.com/watch?v=hDp__2KmjVg&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=2)

**✔ [Apache Maven Project](https://maven.apache.org/)**

**✔ [Apache Maven Project : Download & Install](https://maven.apache.org/download.cgi)**

- apace-maven-3.8.6-bin.zip 다운로드

Maven을 실행하려면 설치 되어 있는 파일로 가서 실행해야 한다.

**✔ 환경 변수 세팅**

설치 후에 환경변수에서 환경 변수를 세팅해야 한다.

1. 사용자 변수

Path ➡ 편집 ➡ %M2_HOME%\bin 변수 있는지 확인하고 없으면 세팅

2. 시스템 변수 편집

Path ➡ 환경 변수 편집 ➡ %M2_HOME%\bin 변수 있는지 확인하고 없으면 세팅

시스템 변수에 새로 만들기(W)로 변수는 M2_HOME으로 이름을 설정하고 값은 

apach-maven-3.8.6 폴더의 디렉토리로 설정

환경 변수 세팅이 끝났으면, cmd에서 mvn -version을 입력하여 잘 나오는지 확인

### 3. Maven으로 자바 프로젝트 생성하기

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 3강 - 자바 프로젝트 생성하기 ](https://www.youtube.com/watch?v=oPEY7xawQlg&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=3)

1. 먼저, Maven 프로젝트를 만들 폴더를 생성한다.

2. cmd에서 만든 폴더로 이동 후, 다음 명령어를 입력

```
$ mvn archetype:generate
```

- 템플릿, 그룹ID, 아티팩트ID, 버전 설정 후 패키지를 지정하고 입력을 확인하면 메이븐 프로젝트가 생성된다.

### 4. Maven : 컴파일과 실행하기

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 4강 - 컴파일과 실행하기 ](https://www.youtube.com/watch?v=3gJIbifmll4&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=4)

**✔ maven compile 하기**

메이븐 프로젝트가 생성 되었으면, 해당 디렉토리에서 다음 명령어를 입력한다.

```
mvn compile
```

**✔ jar 파일 만들기**

```
mvn package
```

**✔ day5_jdbc_coding-1.0-SNAPSHOT.jar**

day5_jdbc_coding-1.0-SNAPSHOT.jar파일에서 java 파일 실행시키기

```java
java -cp target\day5_jdbc_coding-1.0-SNAPSHOT.jar com.day5_jdbc_coding.App

// Hello World! 출력
```


### 5. Build LifeCycle과 Phase들

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 5강 : Build LifeCycle과 Phase들 ](https://www.youtube.com/watch?v=fQsTKKkZ6d8&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=5)

**✔ Build LifeCycle**

```
1. validate
2. initialize
3. generate-sources
4. process-sources
5. generate-resousrces
6. process-resources
7. compile
=============================
8. process-classes
9. geenerate-test-sources
10. process-test-sources
11. generate-test-resources
12. process-test-resources
13. test-compile
14. process-test-clasess
15. test
=============================
16. prepare-package
17. package
=============================
18. pre-integration-test
19. integration-test
20. post-integration-test
21. verify
22. install
23. deploy
```

- mvn 명령어들

```
mvn compile
mvn test
mvn package
```

명령어는 ~단계까지 해달라는 의미

POM.xml에서의 POM :  Project Object Model

**✔ 단계별 실행을 담당하는 플러그인들 보기**

```java
mvn help:describe -Dcmd=compile
```

### 6. 메이븐 프로젝트 이클립스에 로드하기

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 6강 - 메이븐 프로젝트 이클립스에 로드하기 ](https://www.youtube.com/watch?v=xq_EM-l_A5o&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=6)

이클립스에서 File ➡ import ➡ Maven ➡ Existing Maven Projects

생성한 Maven Project가 있는 경로 입력하여, import하기

### 7. 메이븐(Maven) 강의 7강 - 컴파일 플러그인으로 JDK 버전 변경하기

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 7강 - 컴파일 플러그인으로 JDK 버전 변경하기 ](https://www.youtube.com/watch?v=_6H0E49UGoM&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=7)

**이클립스 porm.xml에서 수정하기**

해당 내용을 본인의 java version에 맞게 지우고 저장하기

```xml
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>
  ```

1.7 ➡ 1.8로 수정

프로젝트 우클릭 후, Maven클릭 후, Update Project 누르기

### 8. 메이븐(Maven) 강의 8강 - 웹 프로젝트로 변경하기

<hr>

[참고 자료(Youtube-뉴렉처): 메이븐(Maven) 강의 8강 - 웹 프로젝트로 변경하기](https://www.youtube.com/watch?v=VPVMqA8tFRw&list=PLq8wAnVUcTFWRRi_JWLArMND_PnZM6Yja&index=8)

pom.xml 수정

```xml
<modelVersion>4.0.0</modelVersion>
  <groupId>com.ToDoList</groupId>
  <artifactId>ToDoList</artifactId>
  <packaging>war</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>ToDoList</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.ToDoList.com</url>
```

pom.xml을 수정하고 나면 webapp 폴더가 생긴다. 하위 폴더로 WEB-INF를 만든다.

이후, C:\Downloads\apache-tomcat-8.5.81\webapps\ROOT\WEB-INF 디렉토리에 있는web.xml을 복사하여 WEB-INF 폴더 아래 붙여넣기

### 9. 메이븐(Maven) 강의 8강 - 서블릿/JSP 라이브러리 설정하기

<hr>

index.jsp를 webapp 폴더 안에 생성하면 에러가 발생한다.

프로젝트 우클릭 Build Path에서 Add Library해서 Tomcat8.5를 추가하면 해결된다.

[Tomcat버전으로 Library 확인하기](https://mvnrepository.com/artifact/org.apache.tomcat/tomcat-jsp-api)


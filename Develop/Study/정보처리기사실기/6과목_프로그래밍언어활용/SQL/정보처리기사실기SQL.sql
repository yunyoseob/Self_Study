-- 테이블 리스트
-- $$$$$$$$$$$$$$$$
-- DROP TABLE 학생;
CREATE TABLE 학생(
    학번      VARCHAR2(100),
    이름      VARCHAR2(100),
    학년      NUMBER,
    수강과목 VARCHAR2(100),
    점수      NUMBER,
    연락처    VARCHAR(100)
);

INSERT INTO 학생
VALUES ('1000', '김정미', 1,'알고리즘',90,'010-1111-2222'); 
INSERT INTO 학생
VALUES ('2000', '강은미', 2,'데이터베이스',95,'010-2222-2222');
INSERT INTO 학생
VALUES ('3000', '홍길동', 3,'전산수학',90,'010-3333-3333');
INSERT INTO 학생
VALUES ('4000', '장길산', 4,'운영체제',95,'010-4444-4444');

-- $$$$$$$$$$$$$$$$
-- DROP TABLE STUDENT;
CREATE TABLE STUDENT(
    STID VARCHAR2(100),
    NAME VARCHAR2(100),
    SCORE VARCHAR2(100),
    DEPTID VARCHAR2(100)
);
INSERT INTO STUDENT
VALUES ('1000', '김정미', 90,1);
INSERT INTO STUDENT
VALUES ('2000', '강은미', '95','2');
INSERT INTO STUDENT
VALUES ('3000', '홍길동','90','3');
INSERT INTO STUDENT
VALUES ('4000', '장길산', '95','4');
-- $$$$$$$$$$$$$$$$
-- DROP TABLE SOO;
CREATE TABLE SOO(
    NAME VARCHAR2(100)
);
INSERT INTO SOO
VALUES ('SOPHIA');
INSERT INTO SOO
VALUES ('OLIVIA');
INSERT INTO SOO
VALUES ('SEMA');

-- DROP TABLE JEBI;
CREATE TABLE JEBI(
    RULE VARCHAR2(100)
);
INSERT INTO JEBI
VALUES ('S%');
INSERT INTO JEBI
VALUES ('%A%');
-- $$$$$$$$$$$$$$$$

-- DROP TABLE 성적;
CREATE TABLE 성적(
    과목코드 VARCHAR2(100),
    과목이름 VARCHAR2(100),
    학점 VARCHAR2(100),
    점수 NUMBER
);

INSERT INTO 성적
VALUES ('1000', '컴퓨터과학',' A+',95);
INSERT INTO 성적
VALUES ('2000', '운영체제',' B+',85);
INSERT INTO 성적
VALUES ('1000', '컴퓨터과학',' B+',85);
INSERT INTO 성적
VALUES ('2000', '운영체제',' B',80);
-- $$$$$$$$$$$$$$$$

-- DROP TABLE 학생;
CREATE TABLE 학생(
    학과 VARCHAR2(100),
    학생 VARCHAR2(100)
);

INSERT INTO 학생
VALUES ('전기', '이순신');
INSERT INTO 학생
VALUES ('전자', '이봉창');
INSERT INTO 학생
VALUES ('전자', '강우규');
INSERT INTO 학생
VALUES ('컴퓨터', '안중근');
INSERT INTO 학생
VALUES ('컴퓨터', '윤봉길');
-- $$$$$$$$$$$$$$$$
-- DROP TABLE 급여;
CREATE TABLE 급여(
    이름 VARCHAR2(100),
    부서 VARCHAR2(100),
    급여 NUMBER
);

INSERT INTO 급여
VALUES('김철수','마케팅',5000);
INSERT INTO 급여
VALUES('장길산','마케팅',4000);
INSERT INTO 급여
VALUES('홍길동','전산',3000);
INSERT INTO 급여
VALUES('한유리','전산',2000);;
-- $$$$$$$$$$$$$$$$
-- DROP TABLE 도서;
CREATE TABLE 도서(
    책번호 VARCHAR2(100),
    책명 VARCHAR2(100)
);

INSERT INTO 도서
VALUES ('111','운영체제');
INSERT INTO 도서
VALUES ('222','자료구조');
INSERT INTO 도서
VALUES ('555','컴퓨터구조');

-- DROP TABLE 도서가격;
CREATE TABLE 도서가격(
    책번호 VARCHAR2(100),
    가격 NUMBER
);

INSERT INTO 도서가격
VALUES ('111','20000');
INSERT INTO 도서가격
VALUES ('222','25000');
INSERT INTO 도서가격
VALUES ('333','10000');
INSERT INTO 도서가격
VALUES ('444','15000');
-- $$$$$$$$$$$$$$$$

-- DROP TABLE 사원;
CREATE TABLE 사원(
    이름 VARCHAR2(100),
    연봉 VARCHAR2(100)
);

INSERT INTO 사원
VALUES ('장길산','3000');
INSERT INTO 사원
VALUES ('임꺽정','2500');
INSERT INTO 사원
VALUES ('홍길동','2200');
INSERT INTO 사원
VALUES ('김철수','2000');
INSERT INTO 사원
VALUES ('나','30000');
-- ###################################################

-- 정보처리기사 문제 2020년 2회
-- 학생 테이블에서 3,4학년인 학번, 이름을 조회한다.
-- IN 연산자를 사용해야 한다.
SELECT 학번, 이름
  FROM  학생
 WHERE 학년 IN (3,4);

-- 테이블 칼럼 삭제 하기
ALTER TABLE 학생 DROP COLUMN 연락처;

-- 정보처리기사 문제 2020년 2회
-- STUDENT 테이블의 NAME 속성에 IDX_NAME 이름으로 인덱스를 생성하는 SQL 문을 작성하시오.
CREATE INDEX IDX_NAME ON STUDENT(NAME);

-- 정보처리기사 21년 3회 : 다음 쿼리를 수행시에 결과값을 작성하시오.
-- SELECT COUNT(*) CNT FROM SOO CROSS JOIN JEBI
-- WHERE SOO.NAME LIKE JEBI.RULE;
SELECT*FROM SOO;
SELECT*FROM JEBI;

SELECT COUNT(NAME) CNT FROM SOO;
-- 3
SELECT COUNT(RULE) RULE FROM JEBI;
-- 2

SELECT COUNT(*) CNT 
  FROM SOO CROSS JOIN JEBI
 WHERE SOO.NAME LIKE JEBI.RULE;
-- 5

SELECT COUNT(*) FROM SOO CROSS JOIN JEBI;
-- 6
-- 2 * 3

-- 정보처리기사 20년 3회
-- 과목별 점수의 평균이 90이상인 과목이름, 최소점수, 최대점수를 구하는 SQL 문을 작성하시오.
-- 대소문자 구분 x, WHERE 사용 금지, GROUP BY, HAVING 구문 꼭 쓰기, 별칭 사용, 세미클론 생략가능
SELECT*FROM 성적;

SELECT 과목이름,
          MIN(점수) AS 최소점수, 
          MAX(점수) AS 최대점수
  FROM 성적
GROUP BY 과목이름
HAVING AVG(점수)>=90; 

-- 정보처리기사 20년 4회 문제
-- 학과별로 튜플 수가 얼마인지를 구하는 SQL 문을 작성하시오.
-- 대소문자 구분 X, WHERE 구문 사용금지, GROUP BY 사용, 세미클론 생략 가능, 별칭(AS) 사용, 집계 함수 사용

SELECT 학과, COUNT(학생) AS 학과별튜플수
  FROM 학생
GROUP BY 학과
ORDER BY 학과별튜플수 ASC, 학과 DESC;

-- 단원 종합문제
-- 급여 테이블에서 부서의 급여 합계가 6000이상인 부서, 급여합계를 출력하는 SQL문을 작성하세요
-- 급여 합계는 급여 칼럼의 값들의 합이며 AS를 사용하여 급여합계로 출력

SELECT*FROM 급여;

SELECT 부서, SUM(급여) AS 급여합계
  FROM 급여
 GROUP BY 부서
HAVING SUM(급여) > 6000;


-- 도서 테이블과 도서 가격 테이블을 완전 외부 조인(Full Outer Join)하는 SQL문을 작성하시오.
-- FROM 절에서 도서는 A, 도서가격은 B로 별칭을 줌
-- 도서 테이블의 책번호와 도서가격 테이블의 책번호는 ON 절에서 조인 조건으로 사용

SELECT A.책번호, A.책명, B.책번호, B.가격
  FROM 도서 A FULL OUTER JOIN 도서가격 B
    ON A.책번호=B.책번호;

-- 도서 테이블과 도서가격 테이블에서 아래를 만족하는 SQL 문을 작성하시오.
-- WHERE 절에서 IN 연산자를 사용하여 IN 연산자의 조건에 서브쿼리를 사용
-- 책명이 자료구조인 가격 중에 가장 비싼 값을 도서가격 테이블에서 서브쿼리함

SELECT 가격
  FROM   도서가격
 WHERE 책번호=(SELECT 책번호 FROM 도서 WHERE 책명 IN ('자료구조'));

-- 순위함수를 사용하는 SQL 문을 작성하시오
-- RANK 함수를 이용하여 연봉이 높은 순에서 낮은 순으로 정렬함

SELECT*FROM 사원;

SELECT 이름
        ,  연봉
        ,  RANK() OVER(ORDER BY 연봉 DESC) AS 순위
  FROM 사원 ;







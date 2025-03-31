# 230902 텍스트데이터분석 Basic Python
# Part01_Python Basic
# 기본 자료형 (숫자 및 문자열)
def flowControl(a:int):
    type_a2=a**2
    type_2a=2*a
    if(a>10):
        type_m = 10%3
        type_o = 10//3
    print("a의 제곱은", type_a2)
    print(f"2*a는 {type_2a}")
    print("a를 3으로 나눴을 때 나머지 : {}".format(type_m))
    print("a를 3으로 나눴을 때 몫 : ", type_o)
flowControl(153)

print("="*20)
sqlQuery = """
    SELECT EMPNO, ENAME
      FROM EMP
     WHERE DEPTNO = 40;
"""
print("부서번호가 40인 부서의 사원의 사번과 이름 조회",end="")
print(" sql : {}".format(sqlQuery), end="")
print("="*20)
resultEmpno = 1234
resultEname = "Sam Smith"
print("결과 > EMPNO : %d , ENAME : %s"%(resultEmpno, resultEname))

# 문자열 관련 주요 함수
str = " Python is the best choice "
print(str.count("b"))
print(str.count(" "))
print(len(str))
print(len(str.strip()))
str2 =".".join(str.strip()) 
print("str2 >> : {}".format(str2))
strList = str.split(".")
print(strList)


score = {'kim':90,'lee':80}
for k in score:
    print("key : {}".format(k), end="")
    print(", value : {}".format(score.get(k)))


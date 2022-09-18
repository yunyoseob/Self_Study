# 210808 파이썬 연습

# 파이썬 심화
# pop quiz 사람들에게 먼저 온 순서대로
# 번호표를 나누어주려고 한다. 번호표를 나누어주는
# 함수를 작성해보자

people=['펭수','뽀로로','뚝딱이','텔레토비']

def func1(line):
    new_lines=[]
    i=1
    for x in line:
        print(f'대기번호 {i}번: {x}')
        new_lines.append((i,x))
        i+=1
    return new_lines
    
lines=func1(people)

# enumerate
people=['펭수','뽀로로','뚝딱이','텔레토비']

def func2(line):
    new_lines=[]
    for idx, val in enumerate(line):
        print(f"대기번호 {idx+1}번: {val}")
        new_lines.append((idx+1, val))
    return new_lines

lines=func2(people)

# lines=func2(people)
#대기번호 1번: 펭수
#대기번호 2번: 뽀로로
#대기번호 3번: 뚝딱이
#대기번호 4번: 텔레토비

#zip
str_list=['one','two','three','four']
num_list=[1,2,3,4]

for i in zip(num_list, str_list):
    print(i)

#(1, 'one')
#(2, 'two')
#(3, 'three')
#(4, 'four')

#lambda
lam1=lambda x:x+2
lam1(3)

#map
items=[1,2,3,4,5]

squared_map=list(map(lambda x: x**2, items))
squared_map

#lambda와 map을 이용하여 items의 요소들을
# string(문자)로 바꾸는 것을 짜봅시다. 

items=[1,24,3,6,7]
str_items=list(map(lambda x:str(x), items))
print(str_items)

# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서
#  map함수와 람다식을 이용해
# 항목의 제곱 값을 갖는 리스트를 변환하는 프로그램을 작성하십시오.
int_list=[1,2,3,4,5,6,7,8,9,10]
double_list=list(map(lambda x: x**2, int_list))
double_list

# list comprehension
# 0부터 9까지를 순서대로 가지고 있는 리스트를 만드세요. (한줄로)
lc_1=[x for x in range(10)]
print(lc_1)

# Quiz 1)
ququ_2=[2*x for x in range(1,10)]
print(ququ_2)

# Quiz 2)
str_1="코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 마스크를 끼고 손씻기를 생활화합시다."

def split_list(str_1):
    split_list=[]
    str_2=str_1.split()
    split_list.append([x for x in str_2])
    return split_list

split_list(str_1)

# for문 + if문
# 10부터 20 사이의 숫자들 중에서 짝수만을 담은 리스트를 만들어 보자.
# 1st method

list_1=[]

for i in range(10,21,2):
    list_1.append(i)
    
list_1

# 2nd method

list_2=[]

for i in range(10,21):
    if i%2==0:
        list_2.append(i)
    else:
        pass

list_2

# 3rd method
list_3=[x for x in range(10,21) if x%2==0]
list_3


# for문 + if문
# QUIZ 1부터 10의 제곱수 중, 50 이하인 수만 리스트에 저장하라.
# 1st method
list_4=[]

for i in range(1,11):
    if pow(i, 2)<=50:
        list_4.append(i)
    else:
        pass

list_4

# 2nd method
list_4=[x for x in range(1,11) if x**2<=50]
list_4

# Class
# 객체 (Object)
# 클래스(Class): 객체를 만드는 구조/틀
# 인스턴스(Instance): 클래스가 실질적으로 객체를 만들었을 때, 그 객체를 부르는 용어

class Account():
    def make_account(self):
        self.balance=0
    def deposit(self, money):
        self.balance += money
    def draw(self, money):
        self.balance -= money

a1=Account()
a1.make_account()
a1.deposit(1000)
print(a1.balance)
# 1000


# __init__ 사용

class Account():
    def __init__(self, money):
        self.money=money
    def make_account(self):
        self.balance=0
    def deposit(self, money):
        self.balance += money
    def draw(self, money):
        self.balance -= money

a1=Account(1000)
a1.make_account()
a1.deposit(1000)
print(a1.balance)

# 통장에 입금하기
# 인스턴스(instance)
class Acount():
    def moke_account(self):
        self.balance=0

    def deposit(self, money):
        self.balance += money

    def draw(self, money):
        self.balance -= money

a1=Account()  # 전의 Account 클래스 때문에 접속이 되지 않는다.

class Account():
    def __del__(self, money):
        self.money=money

a1=Account() # 이제 접속이 된다.

class Acount():
    def moke_account(self):
        self.balance=0

    def deposit(self, money):
        self.balance += money

    def draw(self, money):
        self.balance -= money

# 1000원 입금
a1.make_account()
a1.deposit(1000)
print(a1.balance)

# 5000원 입금
a2=Account()
a2.make_account()
a2.deposit(5000)
print(a2.balance)

class test():
    name='아무나'
    age=0
    def __init__(self,name,age):
        print("생성자 호출")
        self.name=name
        self.age=age
    def __del__(self):
        print("소멸자 호출")
    def info(self):
        print(f"나의 이름은 {self.name}입니다.")
        print(f"나이는 {self.age}입니다!")

r=test("윤요섭",26)
# 생성자 호출

r.info()
#나의 이름은 윤요섭입니다.
#나이는 26입니다!

# Class Variable과 Class Method
class Account2():
    bank="모두은행"
    total=0

    @classmethod #데코레이터(decorator): wrappping을 통해 특정 코드를 재사용할 수 있게 해주는 역할
    def merge(cls, acc1, acc2): #cls: 클래스를 위한 placeholder(self와 유사한 역할), 파이썬은 클래스 또한 자동으로 넘겨줌
        cls.total=acc1.balance+acc2.balance
        print(f"당신의 재산은 {cls.total}")
        ## 여기까지가 클래스 메소드 ##
    def __init__(self):
        self.balance=0
    def deposit(self, money):
        self.balance += money
    def draw(self, money):
        self.balance -= money

b1=Account2()
b1.deposit(4000)
print(b1.balance)
# 4000
print(b1.bank)
# 모두은행

b2=Account2()
b2.deposit(7000)
print(b2.balance)
# 7000
print(b2.bank)
# 모두은행

Account2.merge(b1, b2)
# 당신의 재산은 11000

Account2.total
# 11000


# Class Variable과 Class Method 2
class GuestHouse():
    guest=[]

    def __init__(self):
        self.room=[]

    @classmethod
    def check_in(cls, name):
        cls.guest.append(name)

    def add_person(self, name):
        self.check_in(name)
        self.room.append(name)

r1=GuestHouse()
r2=GuestHouse()

r1.check_in("뚝딱이")
r2.check_in("뿡뿡이")

GuestHouse.guest
# ['뚝딱이', '뿡뿡이']

r1.room
# []

r2.room
# []

r1.add_person('홍길동')
r2.add_person('텔레토비')

r1.room
# ['홍길동']

r2.room
# ['텔레토비']

GuestHouse.guest
# ['뚝딱이', '뿡뿡이', '홍길동', '텔레토비']


# 클래스 상속(inheritance)
# 상속: 부모의 클래스를 물려받음
# -> 부모 클래스가 가지고 있는 함수/변수를 그대로 사용할 수 있음
# 상속의 장점: 기존 클래스를 변형하지 않고 추가/변경이 가능함.

class Myphone():
    def __init__(self, model, color):
        self.model=model
        self.color=color

    def set_name(self, name):
        self.user=name
        print(f"사용자 이름은 {self.user}")
    def set_number(self, number):
        self.number=number

class Myphone2(Myphone):
    def has_case(self, val=False):
        self.case= val

p2=Myphone2('iphone','red')
p2.set_name('YS')
# 사용자 이름은 YS

p2.has_case(True)
p2.case
# True
# 자식 클래스의 새로운 매소드도 사용 가능

# 메소드 오버라이딩(overriding)
# 상속을 받은 자식 클래스가 상속해 준 부모 클래스의
# 메소드를 변형하는 방법

# 원본(부모 클래스)의 소스코드는 그대로 유지한채 소스코드를 확장,
# 개인화 할 수 있다는 장점이 있음.

class Calculate:
    type='low'
    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2
    def sum(self):
        print(self.n1+self.n2)

c=Calculate(4,2)
print(c.type)
# low
c.sum()
# 6

class Calculate_1(Calculate):
    type='high'
    def sub(self):
        print(self.n1-self.n2)
    def mul(self):
        print(self.n1*self.n2)

c1=Calculate_1(4,2)
print(c1.type)
# high
c1.sum()
# 6
c1.sub()
# 2
c1.mul()
# 8

class Myphone():
    def __init__(self, model, color):
        self.model=model
        self.color=color
    def set_name(self, name):
        self.user=name
        print(f"사용자 이름은 {self.user}")
    def set_number(self, number):
        self.number=number

p1=Myphone('iphone','red')
p1.set_number("010-****-****")

class Myphone3(Myphone):
    def set_number(self, num):
        self.number=num
        print("이 핸드폰의 번호는: %s"%self.number)

p3=Myphone3('iphone','red')
p3.set_number("010-****-****")
# 이 핸드폰의 번호는: 010-****-****

# 연습문제 1
# Human이라는 클래스를 만들어보자
# Human 클래스는 아래와 같은 특징이 있다.
# Human 클래스는 인스턴스 생성시 birth_date, sex, nation을 변수로 가지고 있다.
# give_name은 인스턴스 메소드로 이름을 input으로 받아서 name이라는 인스턴스 변수로
# 저장하고 화면에 이름을 출력하는 역할을 함수이다.
# can_sing이라는 함수는 True/False 값을 input으로 받으며, 참이면 "Sing a song"
# 을 화면에 출력하는 함수이다.

class Human():
    def __init__(self, birth_date, sex, nation):
        self.birth_date=birth_date
        self.sex=sex
        self.nation=nation
    def give_name(self, name):
        self.name=name
        print(f"이름은 {self.name}")
    def can_sing(self, TF):
        self.TF=TF
        if TF=="True":
            print("Sing a song")
        else:
            pass

h1=Human("0323","man","korea")
h1.give_name('YS')
# 이름은 YS
h1.can_sing("True")
# Sing a song

# 연습문제 2번
# Human이라는 클래스를 상속하는 Child라는 클래스를 만들어보자
# Child 클래스에는 아래와 같은 변수와 함수들이 추가된다.
# 눈동자 색깔을 나타내는 변수 eye를 인스턴스 선언시 사용할 수 있게 추가해보자.
# Child의 클래스는 노래하는 능력이 없다. 따라서 can_sing이라는 메소드가
# 호출되면 무조건 "Can't Sing"이라고 출력하도록 바꿔보자.
# Child는 노래 대신 춤을 출 수 있다. can_dance라는 메소드가 호출되면
# "Dance Time!"을 출력하도록 메소드를 작성해보자.

class Human():
    def __init__(self, birth_date, sex, nation):
        self.birth_date=birth_date
        self.sex=sex
        self.nation=nation
    def give_name(self, name):
        self.name=name
        print(f"이름은 {self.name}")
    def can_sing(self):
        print("Can't Sing")

class child(Human):
    def eye_color(self, eye):
        self.eye=eye
        print(f"눈동자의 색깔은 {self.eye}입니다.")
    def can_dance(self):
        print("Dance Time!")
  
c1=child("0323","man","korea")
c1.can_sing()
# Can't Sing
c1.can_dance()
# Dance Time!
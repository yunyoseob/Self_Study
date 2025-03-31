"""
파이썬은 모든 것이 객체

객체
  - 불변 객체 (Immutable Object)
  - 가변 객체 (Mutable Object)

파이썬 자료형 불변 객체 여부

| 클래스 | 불변 객체 |
|--|--|
|bool|O|
|int|O|
|float|O|
|list|O|
|tuple|O|
|str|O|
|set|X|
|dict|X| 
"""

# 불변 객체 테스트
print(id(10)) #140256109527568
a = 10
b = a
print(id(a)) #140256109527568
print(id(b)) #140256109527568

# 가변 객체 테스트 1
a = [1,2,3,4,5]
b = a
print(b) # [1, 2, 3, 4, 5]

a[2] = 4
print(a) # [1, 2, 4, 4, 5]
print(b) # [1, 2, 4, 4, 5]

# 가변 객체 테스트 2
a = [1,2,3]
b = a
b[2] = 5
print(a) # [1,2,5]
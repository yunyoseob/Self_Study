# 파이썬의 비교 연산자 is와 ==
# is 는 id() 값 비교 함수

a = [1,2,3] 

print(id(a)) # 139841906138880
print(id(list(a))) # 139841906139456

print(a == a) # True 

print(a == list(a)) # True

print(a is a) # True

print(a is list(a)) # False
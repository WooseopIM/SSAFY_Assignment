# 05_Workshop Python

## 01. 2개의 숫자를 인자로 받아 더하기, 빼기, 곱하기, 나누기 연산의 결과를 반환하는 4개의 함수를 calc.py에 작성하시오. 단, 나누기 연산에서는 try except 구문을 사용하여 '0'으로 나누려고 하는 경우에는 문자열 '0으로는 나눌 수 없습니다.'를 반환하시오

```python
'''
/mymath
	-  __init__.py	#아무 내용 없어도 됨
	-  calc.py		#여기서 이제 4개의 함수를 만들어 주면 됨.
'''

#calc.py내에서

def mysum(x,y):
    a = x+y
    return a

def mysub(x,y):
    b = x-y
    return b

def mymul(x,y):
    c = x*y
    return c

def mydiv(x,y):
    if y == 0:
        return '0으로는 나눌 수 없습니다.'
    else:
        d = x/y
    return d
```







## 02. 1번에서 작성한 calc.py 모듈을 import하여, 각 연산을 수행하는 함수들을 실행하는 코드를 작성하시오.

```python
import calc

print(calc.mysum(12,3)) #결과 확인 하기 위한 print()
print(calc.mysub(12,3)) #결과 확인 하기 위한 print()
print(calc.mymul(12,3)) #결과 확인 하기 위한 print()
print(calc.mydiv(12,3)) #결과 확인 하기 위한 print()
print(calc.mydiv(12,0)) #결과 확인 하기 위한 print()
```


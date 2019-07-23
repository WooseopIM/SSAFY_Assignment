# 05_Homework Python

## 01 아래와 같은 코드가 fibo.py 파일에 작성되어 있을 때, 아래와 같이 함수를 실행할 수 있도록 하는 import 구문을 (A), (B), (C)를 채워 넣어 완성하시오.

```python
def fibo_recursion(n):
    if n<2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
```

```python
from(	(A)   ) import(   (B)   ) as (   (C)   )
```

- (A): fibo(파일명이 기준이 되어야 하므로)
- (B): fibo_recursion(안에 있는 속성(attribute)을 가리키므로)
- (C): recursion(아무렇게나 내가 원하는대로 이름 지정할 수 있음)



## 02 다음 에러들이 어떠한 경우에 발생하는지 작성

- ZeroDivisionError:
  - 0으로 나누는 계산식은 불가능
- NameError: 
  - 이름이 지정되지 않은 변수를 호출할 때 
- TypeError: 
  - 서로 다른 자료형은 연산 불가능 (예) 정수형 + 문자열 연산은 불가능, 함수 호출 과정에서도 인자가 자신을 활용하지 못하는 함수 안에 있으면 타입에러가 뜬다.
- IndexError: 
  - 인덱스를 활용할 수 있는 객체에서 범위 내에 없는 인덱스를 호출할 때 발생
- KeyError: 
  - 딕셔너리 자료 안에 없는 '키'를 호출할 때 발생. 
- ModuleNotFoundError: 
  - 모듈이 아닌 것을 import하려고 할 때 발생한다. 한 프로그램을 import 하기 위해서는 from으로 어디에 속해 있는 모듈인지 말해줘야한다.
- ImportError: 
  - 모듈을 호출할 때 오타를 냈거나, 없는 모듈을 호출할 때 발생하는 에러.


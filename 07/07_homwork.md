# 07_Homework OOP_Advanced

```python
class Calculator:
    count = 0
    
    def info(self):
        print('나는 계산기입니다.')
    
    @staticmethod
    def add(a,b):
        calculator.count +=1
        print(f'{a} + {b} 는 {a + b}입니다.')
        
    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')
```



## 01. 인스턴스 메서드, 스태틱 메서드, 클래스 메서드에 해당하는 함수가 무엇인지 작성

- `인스터드 메서드`: 	.info()
- `스태틱 메서드`:         .add(a, b)
- `클래스 메서드`:         .history(cls)



## 02. 각각의 함수(메서드)를 실행하는 코드를 작성

```python
class Calculator:
    count = 0
    
    def info(self):
        print('나는 계산기입니다.')
    
    @staticmethod
    def add(a,b):
        Calculator.count +=1
        print(f'{a} + {b} 는 {a + b}입니다.')
        
    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')



calc = Calculator()

calc.info()
calc.add(2, 5)
calc.history()

calc.add(5457.2302, 123940)
calc.history()

[출력]
나는 계산기입니다.
2 + 5 는 7입니다.
총 1번 계산 했습니다.
5457.2302 + 123940 는 129397.2302입니다.
총 2번 계산 했습니다.

```





## 03. 파라미터 self와 cls에는 어떤 값이 할당 되는가?

```python
class Calculator:
    count = 0
    
    def info(self):
        print('나는 계산기입니다.')
    
    @staticmethod
    def add(a,b):
        Calculator.count +=1
        print(f'{a} + {b} 는 {a + b}입니다.')
        
    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')

        
        
calc = Calculator()

calc.info()
calc.add(2, 5)
calc.history()
```

- 이 소스코드의 경우, info(self)에 들어가는 self는 <class Calculator>의 instance인 calc이다. 
- history(cls)에 들어가는 cls는 <class Calculator>를 참조한다.
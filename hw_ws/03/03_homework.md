# 03_Homework

## 01 Python에서 기본적으로 사용할 수 있는 Builtin function 5개를 찾아서 작성하세요

- `print()`: 출력함수
- `abs()`: 절댓값 변환 함수
- `dict()`: 딕셔너리 생성 함수
- `round()`: 반올림 함수
- `sorted()`: 숫자를 정렬해주는 함수



## 02 다음 함수에서 오류가 발생하는 것(답: 3번)

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
    
1. ssafy(location='대전', name='철수')	#정상실행. 매개변수에 넣어줄 인자 순서가 바뀌어도 된다.
2. ssafy('길동', location='광주')		#정상실행. 매개변수를 적어주지 않아도 된다.
3. ssafy(name = '허준', '구미')			#오류. positional argument follows keyword argument

#키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없다.
#positional argument의 순서는 keyword argument의 앞에 있어야 하기 때문.
```



## 03 다음 코드에서 변수 result에 저장된 값(답: 11)

```python
def my_func(a,b):
    c = a+b
    print(c)
result = my_func(4,7)
```



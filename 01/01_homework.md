# 01_Homework

## 01 Python에서 사용할 수 없는 식별자(예약어)

```python
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```



## 02 아래의 값을 비교하기 위해 작성해야 하는 코드를 작성

```python
a = 0.1*3
b = 0.3

#1번 코드
abs(a-b) <= 1e-10

#2번 코드
import sys
abs(a-b) <= sys.float_info.epsilon

#3번 코드
import math
math.isclose(a,b)
```



## 03 이스케이프 문자열 중 1) 줄바꿈, 2) 탭, 3) \ 을 작성하세요.

```python
# 1. 줄바꿈
'\n'

# 2. 탭
'\t'

# 3. 백슬래시(\)
'\\'
```



## 04 "안녕, 철수야"를 String Interpolation을 사용하여 출력

```python
name = "철수"

# 1. %-formatting
print('안녕, %s야' % name)

# 2. str.format()
print('안녕, {}야'.format(name))

# 3. f-strings
print(f'안녕, {name}야')
```



## 05 형 변환시 오류가 발생하는 것

```python
# 1) str(1)
정수 1을 문자 1로 변환
# 2) int('30')
문자 30을 정수 30으로 변환
# 3) int(5)
정수 5 그대로 출력
# 4) bool('50')
문자 50은 True로 반환


# 5) int('3.5')
int는 정수형만 가능.
```


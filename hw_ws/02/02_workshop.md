# 02_Workshop

## 01 반복문을 사용하여 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

```python
n = 5
m = 9

i=0
while i < m:
    print('*'*n, end='\n')
    i+=1
```



## 02. 과목명(key)과 점수(value)가 담긴 student dictionary에서 평균 점수를 출력

```python
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
score_sum = sum(student.values())
num = len(student.values())
print(sum(student.values())/num)
```



## 03. 혈액형 문제 딕셔너리(반복문을 사용하여 key는 혈액형 종류, value는 인원 수)

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

import collections
blood_types_str = "A B A O AB AB O A B O B AB"
print(collections.Counter(blood_types))
```

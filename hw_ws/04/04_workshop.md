# 04_Workshop 함수 II

## 01 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수

##### `sqrt()사용 금지`

```python
def my_sqrt(n):
    x, y = 1, n
    result = 1

    while abs(result ** 2 -n) > 0.0000001:
        result = (x+y) / 2
        if result **2 < n:
            x = result
        else:
            y = result
            
    return result

print(my_sqrt(8))
```

kahnacademy square roots

프로그래머스 이분탐색 문제 찾아서 연습해보기. 중요한 파트.
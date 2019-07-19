#양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수 만들기
#sqrt() 사용금지

import math
print(math.sqrt(8))
#이렇게 하면 단순하게 나오는데, 이것을 어떻게 구현할 것인가?


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
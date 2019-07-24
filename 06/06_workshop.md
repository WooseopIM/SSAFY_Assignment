# 06_Workshop OOP_Basic

## 01. class Circle: 이 있을 때, 반지름이 3이고 x,y 좌표가 (2,4)인 원을 만들어 넓이와 둘레 출력

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return f'넓이는 {self.pi*self.r*self.r}입니다.'
    
    def circumference(self):
        return f'둘레의 길이는 {2*self.pi*self.r}입니다.'
    
    def center(self):
        return f'중심의 좌표는{(self.x, self.y)}입니다.'

myCircle = Circle(3, 2, 4)
print(myCircle.area())
print(myCircle.circumference())
print(myCircle.center())
```


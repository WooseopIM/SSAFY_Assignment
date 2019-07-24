# 07_Workshop OOP_Advanced

## 01. Animal 클래스를 상속 받는 Dog 클래스와 Bird 클래스를 작성하기.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):

    def run(self):
        print('멍멍이! 달린다!')
    def walk(self):
        print('멍멍이! 달린다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('바둑이')
dog.walk()
dog.run()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```


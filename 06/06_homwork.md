# 06_Homework OOP_Basic

## 01. Python은 객체 지향 프로그래밍 언어입니다. Python에서 기본적으로 정의되어 있는 class 5가지만 작성.

> `<class 'str'>`, `<class 'dict'>`, `<class 'list'>`,
>
> `<class 'int'>`, `<class 'complex'>`



## 02. 다음 매직 메서드의 역할을 간단하게 작성

> 양쪽에 언더스코어(_)가 있는 메서드를 매직 메서드 혹은 스페셜 메서드라고 부른다.

`__init__`: 새로운 인스턴스를 생성할 때 호출되어서 인자로 갖는 값들을 초기화.

`__del__`: 객체가 소멸되는 과정에서 호출되는 함수

`__str__`: 인스턴스 자체를 출력할 때의 형식을 지정해주는 문자열화 함수

`__repr__`: 인스턴스를 표현하는 문자열을 반환한다. str과 비슷.



## 03. 문자열, 리스트, 딕셔너리 등을 조작하는 메서드 3가지를 역할과 함께 작성

- String 메서드

  - `(문자).__add__(문자)`: 두 문자열을 더한다. 

    ```python
    'a'.__add__('b') => 'ab'
    ```

  - `(문자)__contains__(문자)`: 앞에 있는 문자열에 포함 여부를 bool값으로 반환

    ```python
    'abcdefg'.__contain__('b') => True
    ```

  - `(문자)__getitem__(정수)`: 앞에 있는 문자열의 (정수)번째 문자를 반환

    ```python
    'adgdebghj'.__getitem__(1) => 'd'
    ```

    

- List 메서드

  - `[1,2,3].__add__(['가','나'])`: 앞 리스트에 뒷 리스트를 합친다. 

    ```python
    [1,2,3].__add__(['가', '나', 'ssafy'])
    						 => [1, 2, 3, '가', '나', 'ssafy']
    ```

  - `[].__sizeof__()`: 앞 리스트의 메모리상 크기를 bytes로 나타낸다.

    ```python
    ['a', 'b', 'c'].__sizeof__() => 32
    ```

  - `[]__getitem__(정수)`: 앞 리스트의 (정수)번째 문자를 반환

    ```python
    ['a', 'b', 'c'].__getitem__(2) => 'c'
    ```

    

- Dict 메서드

  - `{}.__contains__(key)`: 앞 딕셔너리에 'key' 존재 여부를 bool값 반환 

    ```python
    {'a':1, 'b':3}.__contains__('a') => True
    ```

  - `{}__contains__(key, value)`: 앞 딕셔너리 해당 key의 value를 정해줌. key가 없으면 딕셔너리에 포함시킴포함 여부를 bool값으로 반환

    ```python
    {'a':1, 'b':3}.__setitem__('a', 3)
    {'a':1, 'b':3}.__setitem__('c', 3)
    
    [결과]
    {'a':3, 'b':3, 'c':3}
    ```

  - `{}__eq__({})`: 앞 뒤 딕셔너리가 같은지 bool값 반환

    ```python
    dictt = {'a':1, 'b':3}
    dictt.__eq__({'a':1, 'b':4})
    
    [결과]
    False
    ```

    
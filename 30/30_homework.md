# 30_Homework	`JavaScript 문법`

>자바스크립트(JS)의 기본 문법

## 01. 변수와 상수의 선언, let & const

> JavaScript는 ES6 이전과 이후로 많은 것이 바뀌었다. ES5까지는 `var` 키워드로 변수를 선언했다면, ES6 이후로는 `let`과 `const` 키워드가 등장했다. `let`과 `const`의 차이점과 언제 사용하는지에 대하여 간단하게 작성하라

```javascript
// let
1. 변수를 선언할 때 쓴다.
2. x라는 변수를 선언할 때 딱 한 번 쓸 수 있다.
	let x = 1; lex x = 2;
	처럼 동일 변수에 대해서 두 번의 선언은 불가능하다.
    만약 위처럼 쓰게된다면 'x' has already been declared라는 SyntaxError를 띄운다.
3. 하지만 일단 let x = 1 을 선언 했다면, 이후에 x에 무슨 짓을 하든지 가능하다.
	let x = 1; x += 2; console.log(x) >>>> 3
4. 만약 x를 let으로 선언하기 전에 값을 할당한다면, ReferenceError를 띄운다.

// const
1. 변하지 않는 상수를 선언할 때 쓴다.
2. 상수 선언한 값에 대해서는 등호(=)를 다시 쓰지 못한다.
3. 만약 다음과 같이 쓴다면 Assignment to constant variable이라는 TypeError를 띄운다.
	const x = 28; x = 30;
4. 상수를 선언할 때는 ALLCAP으로 쓰는 것이 JS의 관례
```

## 02. JS Object `vs` JSON 

> JavaScript에서는 Key-Value로 이루어진 자료 구조를 Object라고 한다. Object와 JSON의 차이를 간단하게 작성하자.

```javascript
// JavaScript Object
1. JS Engine 메모리 안에 있는 데이터의 구조. 모든 JS의 values들, data types 등은 JS Object임
2. JSON.stringify()를 통해 JS Obect 파일을 JSON으로 바꿀 수 있음
3. 파이썬의 dictionary에 대응된다. key 값에 꼭 String을 안 써도 가능
4. value 값에 함수 선언이 가능

// JSON
1. JavaScript Object Notation의 약자
2. 기본적으로 Client 및 Server 사이에 데이터를 쉽게 공유할 수 있는 텍스트 형식
3. JavaSript Object와 관련이 있지만 완전히 JavaScript 객체는 아님
4. JSON을 쉽게 JavaScript Object로 파싱할 수 있는 .parse() 메서드 존재
5. 데이터 구조로 변환하기 쉬움
6. 아래와 같은 형식으로 사람이 읽기 쉬운 구조로 써있음
	userinfo = {
        "name": 'John',
        "language": 'Python3',
        "hobby": 'programming',
    }
7. dot notation으로 접근할 수 있음. 만약 'John'이라는 값을 뽑고 싶으면 userinfo.name으로 접근
8. value에 함수 선언 불가능. 기본적으로 텍스트 형식이기 때문에.

```


## 03. Access 

> 아래의 코드가 있을 때, 'value'에 접근하는 두 가지 방법을 코드로 작성

```javascript
const myObject = {
	key: 'value'
}
```

```javascript
// 1. 점 표기법(dot notation)
myObject.key

// 2. 괄호 표기법(Bracket notation)
myObject['key']
```




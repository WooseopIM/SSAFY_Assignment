# 09_Homework	`HTML element, layout`

## 01. HTML의 약자

`Hyper Text Markup Language`



## 02. T/F

- 웹 표준을 만드는 곳은 Mozilla 재단이다 [F]
  - Mozilla가 속해 있는 `WHATWG`이다.
- 표(table) 를 만들 때에는 반드시 `<th>` 태그를 사용해야 한다 [F]
  - `<td></td>`로 쓸 수 있기 때문에 반드시 사용해야하는 것은 아니지만,
    사용하면 보기에 편한 table이 된다.
- 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. [F]
  - CSS 선언 혹은 외부 로딩 파일 지정 등도 작성할 수 있다.

- 인용문을 가리키는 태그는 `<blockquote>`이다. [T]
  - 인용문을 가리키는 태그는 `<q></q>`태그와 `<blockquote></blockquote>`태그가 있다. 

## 03. HTML5에서 추가된 Semantic 태그(맞는 것 고르기)

`div`, `header`, `h1`, `section`, `footer`, `a`, `form`, `span`

답: `header`,`section`,`footer`



## 04. 로그인 Form을 생성하는 HTML코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <form action="">
    <div>ID : <input type="text"></div>
    <div>PWD : <input type="text"> <button>로그인</button></div>
  </form>
</body>
</html>
```




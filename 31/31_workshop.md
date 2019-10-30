# 31_Workshop	`JavaScript DOM`

> JavaScript를 활용한 DOM 조작의 이해

## 01. JavaScript 코드 작성

> 아래의 주석 내용에 따라 JavaScript 코드를 작성하자

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Hello World!</title>
</head>
<body>
  <h1>Hello World!</h1>
  <script>
    // 1. h1 태그를 선택한 뒤, header라는 상수에 할당한다.
    const header = document.querySelector('h1')
    
    // 2. 브라우저 콘솔에 header 안의 내용을 출력한다.
    console.log(header.value) // 결과는 <h1>Hello World!</h1> 전체가 나옴
      
    // 3. header 안의 내용을 'Happy Hacking!'으로 변경한다.
    header.inneerText = 'Happy Hacking!'
    
  </script>
  
</body>
</html>
```


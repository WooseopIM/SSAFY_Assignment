# 32_Workshop	`JS Event Listener`

> JavaScript의 Event Listener에 대한 이해

## 01. JavaScript 코드 작성

> 아래의 주석 내용에 따라 JavaScript 코드를 작성하자

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>clicked</title>
</head>
<body>
  <h1>0</h1>
  <button id="change-btn">Click it</button>
  <script>
    // 1. #change-btn을 button 상수에 할당한다.
    const button = document.querySelector('#change-btn')
    
    // 2. h1 태그를 header 상수에 할당한다.
    const header = document.querySelector('h1')
    console.log(header.value) // 결과는 <h1>Click it</h1> 전체가 나옴
      
    // 3. button에 'click' eventListener를 추가한다. 클릭이 발생하면,
    // 4. clickCount가 1씩 증가한다.
    // 5. header 안의 내용을 clickCount로 변경한다.
    let clickCount = 0

    button.addEventListener('click', e => { // 3
      clickCount += 1                       // 4
      header.innerText = clickCount         // 5
    })   
  </script>
  
</body>
</html>
```


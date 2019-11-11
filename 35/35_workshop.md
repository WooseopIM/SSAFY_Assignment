# 35_Workshop	`Vue.js`

> v-on 디렉티브의 활용
>
> Computed와 Watch의 활용

## 01. Counter 앱

> v-on 디렉티브를 활용하여, `+1`버튼을 누르면 숫자가 하나씩 증가하는 Counter 앱을 만들어보자.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <title>Document</title>
</head>
<body>
  <div id="app">
    <button @click="counter += 1">+1</button>
    <p>Counter: {{ counter }} </p>
  </div>
  
  <script>
    var app = new Vue({
      el: '#app',
      data: {
        counter: 0,
      },
    })
  </script>
</body>
</html>
```




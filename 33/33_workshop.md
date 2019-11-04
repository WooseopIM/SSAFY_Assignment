# 33_Workshop	`Vue.js`

> Single Page Application에 대한 이해
>
> Vue 인스턴스에 대한 이해

## 01. 필요한 Vue 인스턴스

> 페이지에 Hello, World! 를 rendering 하기 위하여 필요한 `___(a)___`, `___(b)___`를 작성하여 Vue 인스턴스를 완성하자

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
    ____(a)____
  </div>
  
  <script>
    var app = new Vue({
      el: ____(b)____,
      data: {
        message: 'Hello, World!'
      },
    })
  </script>
</body>
</html>
```

```html
(a): {{ message }}
(b): '#app'
```


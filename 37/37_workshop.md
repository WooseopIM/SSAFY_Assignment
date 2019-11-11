# 37_Workshop	`Vue.js`

> 양방향 데이터 바인딩의 이해 및 활용

## 01. v-bind, v-model

> v-bind와 v-model 디렉티브를 활용하여, `Go!`링크를 누르면 입력 창에 작성한 URL로 이동하도록 하는 `주소가 변하는 링크`를 만들어보자.

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
  <div id="app">
    <input v-model="url" placeholder="링크를 입력하세요">
    <a :href="url">Go!</a>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue ({
      el: "#app",
      data: {
        url: ''
      },
    })
  </script>
</body>
</html>
```


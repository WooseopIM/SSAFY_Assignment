# 36_Workshop	`Vue.js`

> Vue.js
>
> v-bind 디렉티브의 class, style 전달인자

## 01. 만들어보자

> v-bind 디렉티브의 class 또는 style 전달인자를 사용하여 `Toggle`버튼을 클릭 할 때마다 작성된 문장이 빨강과 파랑으로 변경되도록 하는 앱을 만들어보자.

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
      <button @click="visible=!visible">Toggle</button>
      <div v-if="visible" v-bind:style="{ color: activeColor }">빨강과 파랑을 섞으면 보라색이 됩니다.</div>
      <div v-else style="color: blue;">빨강과 파랑을 섞으면 보라색이 됩니다.</div>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    var app = new Vue ({
      el:'#app',
      data: {
        activeColor: 'red',
        visible: true,
      }
    })
  </script>
</body>
</html>
```


# 34_Workshop	`Vue.js`

> Single Page Application에 대한 이해
>
> Vue 인스턴스에 대한 이해

## 01. Vue directive

> 다음과 같은 Vue 인스턴스가 있을 때, v-for와 v-if 디렉티브를 활용하여 짝수만 나타나도록 하는 리스트를 작성하면?

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
    <ul>
      <li v-for="number in numbers" v-if="number%2==0">{{ number }}</li>    
    </ul>
  </div>
  
  <script>
    var app = new Vue({
      el: '#app',
      data: {
        numbers: [0,1,2,3,4,5,6,7,8,9]
      },
    })
  </script>
</body>
</html>
```


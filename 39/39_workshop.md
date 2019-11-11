# 39_Workshop	`Vue.js`, `Axios`

> Axios를 활용한 HTTP 요청에 대한 이해

## 01. 임의의 Post 리스트

> Axios를 활용하여, `Get Posts`버튼을 클릭하면 특정 URL로 HTTP 요청을 보내어 임의의 Post의 리스트를 가져와 보여주는 앱을 만들어보자.
>
> 요청을 보낼 URL은 `https://jsonplaceholder.typicode.com/posts`이다. 어떠한 데이터들을 가져올 수 있는지 브라우저 주소창에 입력하여 확인해보자.

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
    <select @change="initialize" v-model="key">
      <option v-for="selected in selecteds">{{ selected }}</option>
    </select>
    <button @click="getPosts">Get Posts!</button>
    <li id="json" v-for="something in somethings">
      {{ something[key] }}
    </li>
  </div>

  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        selecteds: ['userId', 'id', 'title', 'body'],
        somethings: [],
        key: 'userId',
      },
      methods: {
        getPosts() {
          const URL = `https://jsonplaceholder.typicode.com/posts`
          axios.get(URL)
            .then(response => {
              this.somethings = response.data
              console.log(this.somethings)
            })
        },
        initialize() {
          this.somethings = []
        }

      },
    })
  </script>
</body>

</html>
```

- 문제에서 요구하는 것 이상으로 `38 Workshop`의 내용을 접목시켜서 가져올 수 있는 데이터들의 목록을 Select > option으로 구현해보았다.
- 한 가지 문제는 이벤트가 발생할 때마다 데이터를 계속 로드해야 한다는 점.


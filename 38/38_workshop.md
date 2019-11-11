# 38_Workshop	`Vue.js`, `Axios`

## 01. Axios를 활용한 앱 만들기

> Axios를 활용하여, `Get {N} Dogs!` 버튼을 클릭하면 Dog API URL로 HTTP 요청을 보내어 임의의 강아지 사진을 지정한 개수만큼 가져와 보여주는 앱을 만들어보자. 
>
> 요청을 보낼 API URL은 `https://dog.ceo/api/breeds/image/random/{N}`이다. 어떠한 형태로 데이터를 가져올 수 있는지 브라우저 주소창에 입력하여 확인해보자.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Dog & Cat API</title>
  <style>
    img {
      width: 300px;
      height: 300px;
    }
  </style>
</head>

<body>
  <div id="app">
    <select v-model="selected">
      <option v-for="number in numbers">{{ number }}</option>
    </select>
    <button id="Dog" @click="getDogAndPush">Get {{ selected }} Dogs!</button>
  </div>

  <div id="showIMG">

  </div>

  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const dogVue = new Vue({
      el: '#app',
      data: {
        selected: 1,
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      },
      methods: {
        getDogAndPush() {
          document.querySelector('#showIMG').innerHTML= ''
          const DogURL = `https://dog.ceo/api/breeds/image/random/${this.selected}`
          axios.get(DogURL)
            .then(response => {
              console.log(response.data)
              const imgURLs = response.data.message
              // console.log(imgURL) 3개의 URL이 배열로 들어옴
              for (let imgURL of imgURLs) {
                const imgTag = document.createElement('img')
                imgTag.src = imgURL
                document.querySelector('#showIMG').appendChild(imgTag)
              }
            })
        }
      }
    })
    
  </script>
</body>

</html>
```


# 38_Homework	`Vue.js` `Axios`
> Axios는 다양한 HTTP 요청들을 브라우저나 Nodejs 환경에서 보낼 수 있는 JavaScript HTTP 클라이언트 라이브러리이다. 

## 01. Axios
> CDN을 통하여 Axios를 사용하려 할 때, 어떠한 tag를 추가하여 해당 라이브러리를 불러와 사용할 수 있는지 작성하자.
```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```



## 02. NPM

> NPM(Node Package Manager)을 통하여 Axios를 사용하려 할 때, Axios를 설치하는 명령어는 무엇인지 작성하고, Vue 앱에서 어떻게 불러와 사용할 수 있는지 작성하자.

```bash
$ npm install axios
```

```javascript
const axios = require('axios')
또는
import axios from 'axios'
```


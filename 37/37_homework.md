# 37_Homework	`Vue.js`
## 01. v-model

> v-model 디렉티브는 input, textarea, select와 같은 엘리먼트들과 `___(a)___`을 생성합니다. 빈칸 (a)에 들어갈 말을 작성하자.

```html
(a): 양방향 데이터 바인딩
```

- 사용자 입력 이벤트에 대한 데이터를 업데이트 하는 `syntax sugar`



## 02. v-model 속성

> v-model 디렉티브는 엘리먼트의 종류에 따라 인스턴스의 속성을 업데이트하는 데이터의 타입이 다릅니다. 아래의 엘리먼트들이 기본적으로 어떠한 데이터 타입으로 인스턴스의 속성을 업데이트 하는지 https://kr.vuejs.org/v2/guide/forms.html를 참고하여 작성하자

- input

  ```html
  <input v-model="message" placeholder="여기를 수정해보세요">
  <p>메시지: {{ message }}</p>
  ```

  

- textarea

  ```html
  <span>여러 줄을 가지는 메시지:</span>
  <p style="white-space: pre-line">{{ message }}</p>
  <br>
  <textarea v-model="message" placeholder="여러줄을 입력해보세요"></textarea>
  ```

  ```html
  <textarea>{{ message }}</textarea> 는 작동하지 않음
  ```

  

- 단일 checkbox: 단일 boolean 값을 가진다.

  ```html
  <input type="checkbox" id="checkbox" v-model="checked">
  <label for="checkbox">{{ checked }}</label>
  ```

  - {{ checked }}에는 true와 false가 checkbox를 누를 때마다 바뀌어서 나오게 됨.

- 다중 checkbox: 같은 배열을 바인딩할 수 있음

  ```html
  <div id='example-3'>
    <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
    <label for="jack">Jack</label>
    <input type="checkbox" id="john" value="John" v-model="checkedNames">
    <label for="john">John</label>
    <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
    <label for="mike">Mike</label>
    <br>
    <span>체크한 이름: {{ checkedNames }}</span>
  </div>
  ```

  

- radio:

  ```html
  <input type="radio" id="one" value="One" v-model="picked">
  <label for="one">One</label>
  <br>
  <input type="radio" id="two" value="Two" v-model="picked">
  <label for="two">Two</label>
  <br>
  <span>선택: {{ picked }}</span>
  ```

  - 선택한 것에 따라 {{ picked }}안에 One 또는 Two가 출력됨.

  

- 단일 select:

  ```html
  <select v-model="selected">
    <option disabled value="">Please select one</option>
    <option>A</option>
    <option>B</option>
    <option>C</option>
  </select>
  <span>선택함: {{ selected }}</span>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
  new Vue({
    el: '...',
    data: {
      selected: ''
    }
  })
  </script>
  ```

  - 초기 값이 어떤 옵션에도 없으면 select 엘리먼트는 선택없음 상태로 렌더링 된다. 

  

- 다중 select: 배열을 마인딩한다.

  ```html
  <select v-model="selected" multiple>
    <option>A</option>
    <option>B</option>
    <option>C</option>
  </select>
  <br>
  <span>Selected: {{ selected }}</span>
  ```

  


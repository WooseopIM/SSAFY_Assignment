# 36_Homework	`Vue.js`
## 01. 무엇이 렌더링 될까

> 아래와 같은 템플릿 코드와 Vue 인스턴스의 data 속성이 있을 때, 어떠한 HTML 코드가 렌더링 되는지 작성하자.

```html
<div class="static" v-bind:class="{ active: isActive, error: hasError }"></div>
```

```javascript
var = new Vue ({
    el: '.static',
    data: {
        isActive: true,
        hasError: false,
    },
})
```

```html
<div class="static active"></div>
```



## 02. 무엇이 렌더링 될까 (2)

> 아래와 같은 템플릿 코드와 Vue 인스턴스의 data 속성이 있을 때, 어떠한 HTML 코드가 렌더링 되는지 작성하자.

```html
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

```javascript
var app = new Vue ({
    data: {
        activeColor: 'red',
        fontSize: 30
    }
})
```

```html
<div style="color: red; font-size: 30px;"></div>
```


# 31_Homework	`DOM 선택, 조작`

>DOM 요소 선택과 조작
>
>**`DOM`**: **D**ocument **O**bject **M**odel,
>
>*BOM: Browser Object Model

## 01. querySelector() `vs` querySelectorAll()

> DOM에서 특정 요소를 선택할 때, document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용할 수 있다. 이 둘의 차이를 간단하게 작성해라.

```javascript
// 1. document.querySelector(selectors)
1. 제공한 선택자 또는 선택자 덩어리와 일치하는 문서 내 첫 번째 element를 반환한다. 일치하는 요소가 없으면 null을 반환한다.
2. 탐색은 depth-first, pre-order 순회를 하며, 문서의 첫 번째 요소부터 시작해 자식 노드의 수를 기준으로 순회한다.
3. selectors는 하나 이상의 선택자를 포함한 DOMString. 유효한 CSS 선택자여야만 하며 아닐 경우 SYNTAX_ERR 예외가 발생한다. 


// 2. document.querySelectorAll(selectors)
1. 지정된 셀렉터 그루벵 일치하는 document의 element list를 나타내는 정적 NodeList를 반환한다. 일치하는 것이 없는 경우에는 비어 있는 NodeList(즉, NodeList.length === 0)를 반환한다.
2. 매칭할 하나 이상의 셀렉터를 포함하는 DOMString. 유효한 CSS 세렉터여야만 한다. 그렇지 않을 경우 SYNTAX_ERR 예외가 발생한다.
3. 대부분의 일반적인 자바스크립트 DOM 라이브러리와 다르게 동작하여 예상하지 못한 결과를 가져올 수 있음
```

```html
<div class="outer">
    <div class="select">
        <div class="inner">
        </div>
    </div>
</div>
```

```javascript
const select = document.querySelector('.select');
const inner = select.querySelectorAll('.outer .inner');
inner.length; // 1 입니다. 0 이 아닙니다!
```

- 클래스 `select`를 갖는 `div` 컨텍스트에서 `.outer .inner`를 셀렉팅할 때, `outer`가 탐색을 수행하는 기본 엘리먼트(`select`)의 자손이 아님에도 클래스 `.inner`가 탐색된다. 기본적으로 `querySelectorAll()`은 탐색 범위 내에서 셀렉터의 마지막 엘리먼츠만을 검증한다. 

## 02. innerHTML `vs` appendChild()

> DOM에 요소를 추가할 때, 'innerHTML += ... '의 방법과 'appendChild()' 함수를 사용하는 방법이 있다. 이 둘의 차이를 간단하게 작성해라.

```javascript
두 가지 방법은 모두 Script로 태그를 추가하는 방법이다.

// 1. innerHTML += ... (Property)
1. element 내에 포함 된 HTML 또는 XML 마크업을 가져오거나 설정한다.
2. 만약 <div>, <span>, <noembed> 노드가 (&), (<), (>) 문자를 포함하는 텍스트 노드를 자식으로 갖고 있으면, innerHTML은 이러한 문자들을 각각 ("&amp;"), ("&lt;"), ("&gt;")로 반환한다.
3. const content = element.innerHTML; 과 같이 선언
4. 교체; 전체 태그에 합쳐지는 것(전체데이터 += 추가데이터를 새로 쓰는 효과)

// 2. appendChild()	   (Method)
1. 추가; 현재 위치에만 추가(추가데이터만 필요할 때는 이것만 쓴다)
```

참고:  https://developer.mozilla.org/ko/docs/Web/API/Node/appendChild  (`Node.appendChild()`)

참고:  https://developer.mozilla.org/ko/docs/Web/API/Element/innerHTML  (`Element.innerHTML`)


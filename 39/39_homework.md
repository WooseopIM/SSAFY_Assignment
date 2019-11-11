# 39_Homework	`Axios`
## 01. Axios

> 새로운 글을 작성하기 위해 Axios를 사용하여 `/articles/create/`로 POST 요청을 보내려 할 때, 아래의 빈칸 (a), (b)에 들어갈 코드

```javascript
createArticle: function () {
    axios.(a)((b)), {
        title: '안녕하세요.',
        body: '반갑습니다.',
    }).then((response) => {
        // ...
    })
}
```

```
(a): post
(b): /articles/create/
```



## 02. CORS

> CORS가 무엇의 약자인지, 그리고 의미하는 바가 무엇인지 작성

```
Cross-Origin Resource Sharing
추가 HTTP 헤더를 사용하여 브라우저가 한 출처에서 실행중인 웹 애플리케이션에 선택된 액세스 권한을 부여하도록 하는 메커니즘
```


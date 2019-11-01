# 28_Workshop	`REST API`

## 01. 통합 자원 식별자(URI)

> 위키피디아에서 설명하고 있는 인터넷에 있는 자원을 나타내는 유일한 주소는 `___(a)___`이다.  `___(a)___`에는  `___(b)___`와 `___(c)___` 두 종류가 있다. `___(b)___`는 네트워크상에서 자원이 어디 있는지를 알려주기 위한 규약으로 웹 사이트 주소 뿐만 아니라 다양한 프로토콜(FTP/Telnet 등)에서도 활용된다. 빈칸 (a), (b), (c)에 들어갈 용어를 작성하자
>
>  https://en.wikipedia.org/wiki/Uniform_Resource_Identifier 

```
(a): URI (Uniform Resource Identifier)
(b): URL (Uniform Resource Locator)
(c): URN (Uniform Resource Name)
```



## 02. REST의 정의

> REST는 Representational State Transfer의 약자로 자원의 표현을 하기 위한 아키텍처 중 하나이다. 장점 중에 하나로 HTTP 프로토콜 인프라를 그대로 사용한다. 즉, `___(a)___`를 통해 자원을 명시하고 `___(b)___`를 통해 자원에 대한 동작을 나타낸다. 빈칸 (a), (b)에 들어갈 용어를 작성
>
> https://meetup.toast.com/posts/92 
>
> https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html 
>
> https://poiemaweb.com/js-rest-api 

```
(a): URI
(b): HTTP Method(GET, POST, PUT, DELETE)
```

- URI는 정보의 자원을 표현해야 한다



## 03.

> SSAFY 회원 정보가 있는 API를 구조화하였을 때, 1반(classes)의 3번 학생(members)을 나타내는 URL 예시를 작성

```
GET /classes/1/members/3
```


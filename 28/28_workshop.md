# 28_Workshop	`REST API`

> - REST API의 구조
> - HTTP Methods
> - REST API의 일반적인 설계에 대한 이해

## 01. 

> 일반적인 REST API에서 게시글(Article)에 대한 각각의 CRUD에 대응되는 HTTP Methods와 URL을 작성

|        CRUD         | HTTP Methods |             URL              |
| :-----------------: | :----------: | :--------------------------: |
|    리소스의 목록    |     GET      |          /articles/          |
|    리소스의 생성    |     POST     |          /articles/          |
| 리소스 중 하나 표시 |     GET      | /articles/`<int:article_pk>` |
|     리소스 수정     |     PUT      | /articles/`<int:article_pk>` |
|     리소스 삭제     |    DELETE    | /articles/`<int:article_pk>` |


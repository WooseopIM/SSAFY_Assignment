# 18_Workshop	`SQLite RDBMS`

## 01. DB 테이블 생성

> 아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 데이터를 입력해 보자
>
> Table Name: bands

| id(INTEGER) | name(TEXT) | debut(INTEGER) |
| :---------: | :--------: | :------------: |
|      1      |   Queen    |      1973      |
|      2      |  Coldplay  |      1998      |
|      3      |    MCR     |      2001      |

```sqlite
sqlite> CREATE TABLE bands (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL,
   ...> debut INTEGER
   ...> );

sqlite> INSERT INTO bands VALUES (1,'Queen',1973);
sqlite> INSERT INTO bands VALUES (2,'Coldplay',1998);
sqlite> INSERT INTO bands VALUES (3,'MCR',2001);

sqlite> .headers on
sqlite> .mode column

sqlite> SELECT * FROM bands;
id          name        debut
----------  ----------  ----------
1           Queen       1973
2           Coldplay    1998
3           MCR         2001

```



## 02. id와 name 조회

> bands 테이블에서 모든 데이터 레코드의 id와 name만 조회하는 SQL query문을 작성하고 실행

```sqlite
sqlite> SELECT id,name FROM bands;
id          name
----------  ----------
1           Queen
2           Coldplay
3           MCR
```



## 03. 데뷔년도가 2000년 이전인 밴드

> bands 테이블에서 debut가 2000보다 작은 밴드들의 이름만을 조회하는 SQL query문을 작성하고 실행

```sqlite
sqlite> SELECT name FROM bands WHERE debut < 2000;
name
----------
Queen
Coldplay
```

- 1973년에 데뷔한 Queen과 1998년에 데뷔한 Coldplay의 이름만 나오는 것을 알 수 있다.
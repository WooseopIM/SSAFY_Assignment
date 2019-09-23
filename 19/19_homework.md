# 19_Homework	`SQLite RDBMS`

## 01. friends table 생성

> id (INTEGER), name (TEXT), location (TEXT)

```sqlite
sqlite> CREATE TABLE friends (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL,
   ...> location TEXT NOT NULL
   ...> );
   
sqlite> .tables
friends

```


## 02. friends 테이블에 데이터 입력
```sqlite
sqlite> INSERT INTO friends VALUES (1,'Justin','Seoul');
sqlite> INSERT INTO friends VALUES (2,'Simon','New York');
sqlite> INSERT INTO friends VALUES (3, 'Chang','Las Vegas');
sqlite> INSERT INTO friends VALUES (4, 'John','Sydney');
sqlite> SELECT * FROM friends;
id          name        location
----------  ----------  ----------
1           Justin      Seoul
2           Simon       New York
3           Chang       Las Vegas
4           John        Sydney
```


## 03. 스키마 변경
> married (INTEGER) 컬럼 추가하기
>
> *컬럼을 추가하는 과정에서 married를 narried로 오타를 내서 컬럼의 이름을 바꾸는 방법을 찾아봤는데 Stackoverflow.com에서 컬럼의 이름을 바꾸거나 컬럼을 지우는 것은 불가능하다는 글을 보았다.
>
> SQLite에서는 ALTER TABLE 명령을 사용하여 테이블 이름을 바꾸기, 기존 테이블에 새 컬럼 추가하기 정도만 가능하다.

```sqlite
sqlite> ALTER TABLE friends ADD COLUMN married INTEGER;
sqlite> SELECT * FROM friends;
id          name        location    married
----------  ----------  ----------  ----------
1           Justin      Seoul       NULL
2           Simon       New York    NULL
3           Chang       Las Vegas   NULL
4           John        Sydney      NULL

```



## 04. 데이터 추가하기

> 추가한 컬럼에 각각 값을 넣어주기.

```sqlite
sqlite> UPDATE friends SET married=1 WHERE id=1;
sqlite> UPDATE friends SET married=0 WHERE id=2;
sqlite> UPDATE friends SET married=0 WHERE id=3;
sqlite> UPDATE friends SET married=1 WHERE id=4;
sqlite> SELECT * FROM friends;
id          name        location    married
----------  ----------  ----------  ----------
1           Justin      Seoul       1
2           Simon       New York    0
3           Chang       Las Vegas   0
4           John        Sydney      1

```


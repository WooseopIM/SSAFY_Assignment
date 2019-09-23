# 18_Homework	`SQLite RDBMS`

## 01. RDBMS

> 우리가 사용하는 SQLite 는 RDBMS에 속한다.
> RDBMS의 특징 2가지만 작성해라

```python
RDBMS(Relational DataBase Management System)은 데이터 항목들 간에 사전 정의된 관계가 있을 때 그러한 데이터 항목들의 모음을 가리킨다.

이들 항목은 열과 행으로 이루어진 테이블 집합으로 구성되고, 테이블은 DB에 표시할 해당 객체들에 관한 정보들을 수록하는데 사용된다.

테이블의 각 행은 기본 키(PRIMARY KEY)라고 부르는 고유 식별자로 표시할 수 있고, 여러 테이블에 있는 행들은 외래 키를 사용하여 상호 연결될 수 있다.

# RDBMS의 중요한 특징들
1. SQL(Structured Query Language)
- RDBMS의 기본 Interface이자 표준.
- 다양한 오픈소스 RDBMS가 있다.

2. 데이터 무결성
- 일련의 제약 조건을 사용하여 DB 내에서 데이터의 전체적인 완전성, 정확성, 일관성을 확보할 수 있다.
- 기본 키, 외래 키, NOT NULL 제약조건, Unique 제약 조건, Default 제약 조건 및 Check 제약 조건 등을 포함한다.
```


## 02. T/F
```python
1. RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [F]
2. SQL에서 명령어는 대문자로 써야만 동작한다. [F]
3. 일반적인 SQL 문에서 명령어는 세미콜론(;)으로 끝난다. [T]
4. SQLite에서 dot(.)으로 시작하는 명령어는 SQL이 아니다. [F]
5. 한 개의 DB에는 한 개의 테이블만 존재한다. [F]
```


## 03. 코드의 실행결과 (답: NULL)
```sqlite
sqlite> .nullvalue 'NULL'
sqlite> CREATE TABLE ssafy (
   ...> id INTEGER PRIMARY KEY,
   ...> location TEXT,
   ...> class INTEGER
   ...> );
sqlite> INSERT INTO ssafy (id, location)
   ...> VALUES (1, 'JEJU');
sqlite> SELECT class FROM ssafy WHERE id=1;
NULL

```


# 20_Workshop	`Database <1:N 관계>`

## 01. workshop_18에서 만든 테이블 갖고 오기

> workshop_18에서 만든 bands 테이블에 밴드 멤버 수 레코드를 갖는 members 컬럼을 추가하고, 데이터를 삽입해라

| id(INTEGER) | name(TEXT) | debut(INTEGER) | members(INTEGER) |
| :---------: | :--------: | :------------: | :--------------: |
|      1      |   Queen    |      1973      |        4         |
|      2      |  Coldplay  |      1998      |        5         |
|      3      |    MCR     |      2001      |        9         |

```sqlite
sqlite> ALTER TABLE bands ADD COLUMN members INTEGER;
sqlite> SELECT * FROM bands;
id          name        debut       members
----------  ----------  ----------  ----------
1           Queen       1973        NULL
2           Coldplay    1998        NULL
3           MCR         2001        NULL


sqlite> UPDATE bands SET members=4 WHERE id=1;
sqlite> UPDATE bands SET members=5 WHERE id=2;
sqlite> UPDATE bands SET members=9 WHERE id=3;
sqlite> SELECT * FROM bands;
id          name        debut       members
----------  ----------  ----------  ----------
1           Queen       1973        4
2           Coldplay    1998        5
3           MCR         2001        9

```



## 02. 레코드 수정( UPDATE ~ SET ~ WHERE ~)

> id가 3인 레코드의 members를 5로 수정하는 SQL query문을 작성하고 실행

```sqlite
sqlite> UPDATE bands SET members=5 WHERE id=3;
sqlite> SELECT * FROM bands;
id          name        debut       members
----------  ----------  ----------  ----------
1           Queen       1973        4
2           Coldplay    1998        5
3           MCR         2001        5
```



## 03. 레코드 삭제(DELETE FROM ~ WHERE ~)

> id가 2인 레코드를 삭제하는 SQL query를 작성하고 실행

```sqlite
sqlite> DELETE FROM bands WHERE id=2;
sqlite> SELECT * FROM bands;
id          name        debut       members
----------  ----------  ----------  ----------
1           Queen       1973        4
3           MCR         2001        5.ex
```


# 23_Homework	`Django Seeding, Fixture`

## 01. Fixture 파일형식

> Django에서 Database에 값을 일괄 삽입하기 위해야 Fixture 기능을 이용한다. Fixture 파일은 기본적으로 각각의 app 폴더 안의 fixtures 폴더에 위치해야 하며, 파일 형식은 `___(a)___` 또는 `___(b)___`를 사용한다.

```python
# (a)
.json

# (b)
.xml or .yaml
```


## 02. Fixture 
> 23_Workshop과 같이 Database에 데이터가 저장되어 있을 때, Django Fixture 기능을 이용하여 아래와 같은 yaml 형식의 파일을 만들기 위해 입력해야 할 명령어는? (단, 파일 이름은 person.yaml)
>
>  https://wkdtjsgur100.github.io/django-initial-data/ 
>
>  https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata 

- fixture란 django가 DB에서 import하는 방식을 알고 있는 데이터들의 집합

```python
- model: myapp.person
  pk: 1
  fields:
    first_name: John
    last_name: Lennon
- model: myapp.person
  pk: 2
  fields:
    first_name: Paul
    last_name: McCartney
```

- yaml 파일을 만들고 싶은 폴더 트리 만들기: `app/fixture`

```bash
$ python manage.py dumpdata > person.yaml
```


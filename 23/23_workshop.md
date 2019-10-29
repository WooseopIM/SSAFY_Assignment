# 23_Workshop	`Django Model Fixture`

## 01. Fixture 기능을 활용한 데이터 삽입

> Django의 Fixture 기능을 활용하여 myapp의 Musician 모델에 데이터를 일괄 삽입하려 할 때, 23_Workshop.pdf와 같이 데이터를 삽입하기 위하여 필요한 json 파일을 작성하시오

|  PK  | FIRST NAME | LAST NAME |
| :--: | :--------: | :-------: |
|  2   |    Paul    | McCartney |
|  1   |    John    |  Lennon   |

```json
[
  {
    "model": "myapp.person"
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapp.person"
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  },
]
```


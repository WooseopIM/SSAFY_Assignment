# 22_Workshop	`Database Validations`

## 01. 데이터베이스 검증

> 데이터베이스에 값을 추가할 때, 22workshop.pdf에서 보이는 것과 같이 검증하려면 빈칸 (a)와 (b)에 들어갈 알맞은 코드를 작성하기

```python
class Person(models.Model):
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100,
                            validators = _____(a)_____
                            )
    age = models.IntegerField(validators=[ _____(b)_____ ])
```

```python
# (a)
[validate_email]
# (b)
MinValueValidator(19)
```


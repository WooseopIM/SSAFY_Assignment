# 25_Homework	`Database M:N`

## 01. M:N 관계설정

> Article 모델과 User 모델을 M:N 관계로 설정하여 `좋아요` 기능을 구현하려고 할 때, `___(a)___`에 들어갈 클래스의 이름

```python
class Article(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models._____(a)_____(settings.AUTH_USER_MODEL, _____(b)_____='like_posts', blank = True)
```

```
(a): MaynToManyField
```



## 02. 이름 중복 

> 위의 Article 모델에서는 이미 user 필드에서 User 모델과 1:N 관계가 설정되어 있기 때문에 M:N 관계를 설정하려 하면 User 모델에서 Article을  참조하는 이름이 중복되어 오류가 발생한다. 이 때, 이를 방지하기 위하여 별도의 이름을 생성하도록 하는, 빈 칸 `___(b)___`에 들어갈 옵션은?

```python
(b): related_name
```


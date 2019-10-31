# 25_Workshop	`Database M:N`

## 01. M:N 구현

> Article의 Hashtag를 구현하기 위하여 25workshop.pdf의 그림과 같이 개체-관계 다이어그램을 작성하였을 때, 다이어그램을 바탕으로 models.py에 Article 모델과 Hashtag 모델을 작성하자
```python
from django.db import models
from django.conf import settings

class Hashtag(models.Model):
    content = modelsTextField(unique=True)
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, blank=True)
```

- `Article` 테이블과 `Hashtag` 테이블이 `articles_hastags`라는 테이블을 기준으로 연결됨
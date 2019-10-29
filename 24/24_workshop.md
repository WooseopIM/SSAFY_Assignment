# 24_Workshop	`ERD에 대한 이해`

## 01. 투표를 위한 설문app 만들기

> 아래의 Django 코드를 바탕으로 개체-관계 다이어그램(ERD)를 작성.

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

#### ERD

![](C:\Users\student\codes\hwws\24\24_workshop_ERD.PNG)
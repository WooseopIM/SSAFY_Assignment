# 26_Homework	`Django-Auth`

>사용자 인증(Authentication) 및 권한 관리(Authorization)

## 01. 사용자 권한 관리

> 로그인 한 사용자만 게시물을 작성할 수 있도록 해주는 코드

```python
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if requeset.method == "POST":
        article_form = ArticleForm(request.POST)
```

## 02. 1:N 관계 형성

> Aticle 모델에 사용자 정보가 담긴 모델과 1:N 관계를 형성하기 위한 칼럼을 추가하려 할 때 써야하는 코드

```python
from django.db import models
from django.conf import ___(a)___

class Article(models.Model):
    user = models.ForeignKey(___(b)___, on_delete=models.CASCADE)
```

```
(a): settings
(b): settings.AUTH_USER_MODEL
```

참고: https://blog.hannal.com/2015/06/start_with_django_webframework_09/
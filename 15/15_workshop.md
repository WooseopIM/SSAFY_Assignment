# 15_Workshop	`Django: Web Framword for Python` `Template, View` `Template Extending`

## 01. 템플릿 확장(Template Extending)

> 'Base is everywhere!'이라는 문자를 공유하는 서로 다른 2개의 view를 템플릿 확장(Template Extending)을 활용하여 3개의 html 파일을 만들어라.

#### STEP 1. 프로젝트 생성

```bash
$ venv	# 가상환경 시작하자! 꼭! 까먹지 말고!
$ mkdir WORKSHOP
$ django-admin startproject workshop WORKSHOP
$ python manage.py runserver	# 로켓 모습 보이면 완료된 것!
$ python manage.py startapp practice
```

#### STEP 2. workshop 프로젝트의 url.py 설정

- `pages/`라는 공통 url을 사용할 것이기 때문에
- `django.urls`에서 `include`를 import해주고, 
- `practice` 폴더 안에 있는 `urls.py`를 참조하도록
- `include('practice.urls')`를 해준다.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('practice.urls'))    
]
```

#### STEP 3. workshop 프로젝트 settings.py 설정

- 내가 만든 practice 앱을 `INSTALLED_APPS 리스트`에 추가해주자.

```python
INSTALLED_APPS = [
    'practice',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

#### STEP 4. practice 앱의 urls.py 설정

- `from . import views`로 현재 동일 패키지로 묶여있는 views.py를 호출한다.
- `one/`과 `two/` url을 만들어주고 `views.py`에서 `one`, `two`를 정의할 준비를 마친다.

``` python
from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one),
    path('two/', views.two),
]
```

#### STEP 5. practice 앱의 views.py 설정

```python
from django.shortcuts import render

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request, 'two.html')
```

#### STEP 6. 확장 템플릿(base.html)과 one.html, two.html 만들기

- `base.html`
- 내용이 들어갈 부분에   `{% block body %}  {% endblock %}`처리를 해준다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>Base is everywhere!</h1>
  {% block body %}

  {% endblock %}
</body>
</html>
```

- `one.html`
- `{% extends 'base.html' %}`로, base.html을 확장 템플릿으로 사용할 것이라고 지정.
-  `{% block body %}  {% endblock %}` 부분을 base.html의  `{% block body %}  {% endblock %}`에 가져다 넣는 느낌으로 만들면 된다.

```html
{% extends 'base.html' %}

{% block body %}
<h2>I am ONE!</h2>
{% endblock %}
```

- `two.html`
- 앞의 `one.html`과 같은 방식으로 해주면 된다.

```html
{% extends 'base.html' %}

{% block body %}
<h2>I am TWO!</h2>
{% endblock %}
```


# 14_Workshop	`Django: Web Framword for Python`

## 01. 요구에 맞는 프로젝트 생성하기

> 임의의 숫자를 입력할 수 있는 Form과, 해당 Form으로부터 넘어온 숫자를 받아 보여주는 2개의 View.
> 요구에 맞는 `urls.py`, `views.py`, `templates(html)`을 만들어보자

```bash
$ mkdir WORKSHOP_APP
$ django-admin startproject workshop_app WORKSHOP_APP
$ python manage.py startapp pages
```

```python
# urls.py 만들기

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('num/push/', views.push),
    path('num/pull/', views.pull)
]
```

```python
# views.py 만들기

def push(request):
    return render(request,'push.html')

def pull(request):
    result = request.GET.get('push')
    context = {
        'result': result,
    }
    return render(request, 'pull.html', context)
```

```html
<!--push templates 만들기-->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>14_Workshop</title>
</head>
<body>
  <form action="/num/pull/">
    <h1>Push Number</h1>
    <input type="text" name="push"> <button>Push!</button>
  </form>
</body>
</html>
```

```html
<!--pull templates 만들기-->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>Pull Number</h1>
  <h2>Pull 해보니 {{ result }} 입니다!</h2>
</body>
</html>
```


# 13_Workshop	`Django: Web Framword for Python`

## 01. 이름이 'classroom'인 프로젝트를 생성하시오.

Git Bash:

```bash
1. mkdir CLASSROOM
2. django-admin startproject classroom CLASSROOM
```



## 02. '/info'의 주소로 접속했을 때, 반의 정보를 보여주는 페이지를 만들기.

```bash
1. python manage.py startapp [앱 이름]
2. python manage.py startapp pages
```

```python
# settings.py의 INSTALLED_APPS에 pages 넣어주기.

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info),
]
```

```python
from django.shortcuts import render

def info(request):
    teacher = "킹갓갓갓동주"
    student = ['방대승', '김재현', '임우섭', '조동빈', '박진홍', '이수진']
    context = {
        'Teacher': teacher,
        'Student': student,
    }
    return render(request, 'info.html', context)
```

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
  <h1>우리반정보</h1>
  <h2>Teacher</h2>
  <ul>
    <li>{{ Teacher }}</li>
  </ul>
  <h2>Student</h2>
    <ul>
      {% for person in Student%}
      <li>{{ person }}</li>
      {% endfor %}
    </ul>
</body>
</html>
```

## 03. '/student/<학생이름>'의 주소로 접속했을 때, 학생의 이름과 나이를 보여주는 페이지 만들기

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<name>', views.student),
]
```

> 사용자로부터 입력값을 받을 때는 <> 안에 넣어준다.
> 그리고 함수에서도 request 말고 name이라는 인자를 넣어준다.

```python
def student(request,name):
    age = 28
    context = {
        'name': name,
        'ages': age,
    }
    return render(request, 'student.html', context)
```

> `'name'`은 html에서 쓰일 이름. `name`은 사용자가 넣어주고 함수의 인자로 쓰이게 될 것.
> `'ages'`는  html에서 쓰일 이름. `age`는 함수 안에서 정의된 변수

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
  <h1>이름: {{ name }}</h1>
  <h4>나이: {{ ages }} </h4>
</body>
</html>
```




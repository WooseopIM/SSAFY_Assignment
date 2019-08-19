# 16_Workshop	`Django Moel` `SQL`

## 01. Student Model

> 자신의 반에 있는 사람들의 데이터를 저장하는 Student Model을 model.py에 작성해라. Student Model이 가져야 할 필드는 다음과 같다.

|  필드명  |    타입     |
| :------: | :---------: |
|   name   |  CharField  |
|  email   |  CharField  |
| birthday |  DateField  |
|   age    | IntegeField |

```python
# Student Model 만들기. models.py에서 class를 만들어줘야 한다.
class Student(models.Model):
    name = models.CharField()
    email = models.CharField()
    birthday = models.DateField()
    age = models.IntegerField()
```



## 02. Model Migration
> 모델 마이그레이션 작업을 수행한 후, Admin 페이지에서 주변 학생 3명의 정보를 삽입해라.

```bash
$ python manage.py makemigrations
Migrations for 'practice':
  practice\migrations\0001_initial.py
    - Create model Student
    
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, practice, sessions
Running migrations:
  Applying practice.0001_initial... OK
  
$ python manage.py createsuperuser
Username (leave blank to use 'student'): admin
Email address:
Password:	# 타이핑을 해도 커서가 움직이지 않음.
Password (again): # 타이핑을 해도 커서가 움직이지 않음.
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

```python
# admin.py에서
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

위 과정을 수행하면 localhost:8000/admin에 로그인해서 보이는 창에 Students라는 것이 보임. 여기 들어가서 ADD STUDENT를 누르면 된다.



## 03. `__str__`메소드

> 정보 삽입 후, Admin 페이지에서 학생들의 목록을 보기 쉽게 만들기 위하여 `__str__` 메소드를 작성하여 name이 출력되도록 하라.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f'{self.id} : {self.name}'
```


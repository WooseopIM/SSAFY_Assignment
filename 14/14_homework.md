# 14_Homework	`Django: Web Framework for Python`, `MTV 아키텍처`

## 01. MTV의 약자

> Django는 MTV로 이루어진 Web Framework이다. MTV는 무엇의 약자인가?

데이터 관리자: `M`odel

사용자에게 보여지는 화면: `T`emplate

중간 관리자: `V`iew



## 02. Django 프로젝트에서 pages 앱 생성할 때 입력해야 할 명령어.

```bash
$ python manage.py startapp pages
```



## 03. 생성한 앱 이름 추가하기

> pages 앱을 생성한 후, Django 프로젝트의 설정 파일인 settings.py에서 리스트로 된 변수 `___(a)___`에 생성된 앱의 이름을 추가해 주어야 한다. `___(a)___`에 들어갈 변수의 이름은?

```python
INSTALLED_APPS = [
    'pages',	# 여기에 pages를 추가해 줘야 한다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```


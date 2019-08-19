# 13_Homework	`Django: Web Framework for Python`

## 01. Django 서버 실행 명령어

> Git Bash 창에서 Django 서버를 실행하고 싶을 때 사용하는 명령어

`python manage.py runserver` 실행 후, `localhost:8000`에 들어갔을 때 `Django로켓`이 보이면 성공적!



## 02. Django Response 1

>Django는 요청에 대한 응답을 할 때, 기본적으로 허용된 도메인으로부터 온 요청에 한해서만 응답을 하도록 설정되어 있다. `settings.py` 파일에서 특정 도메인을 허용하기 위해 수정해야 하는 변수명을 찾아 작성해라

`ALLOWED_HOSTS = []`: 서버는 여러 개의 도메인을 가질 수 있는데, 그 중에 허용할 도메인을 리스트 [] 안에 입력할 수 있다. 리스트 안에 `*`을 넣어주면 모든 도메인에 대해서 허용한다는 의미를 갖는다. 우리는 local에서 학습 중이라 따로 도메인 설정은 해주지 않았음. `https://여러분의도메인` 이런 식으로 나중에 넣게될 것.



## 03. Django Response 2

> 주소 '/ssafy'로 요청이 들어왔을 때 실행되는 함수가 `views.py` 파일 안의 `ssafy 함수`일 때, 요청에 응답할 수 있도록 `urls.py`에 추가하여야 하는 코드를 작성해라.

```python
path('ssafy/', views.ssafy)
```


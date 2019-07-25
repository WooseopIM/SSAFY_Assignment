# 08_Homework	Web, Flask

## 01. 빈칸 채우기

Web에서의 커뮤니케이션 방식은 (`Request`)와 (`Response`)로 이루어져 있다. 브라우저의 주소창에 주소를 입력하는 것으로 (`Request`)를 보내며, 그에 대한 (`Response`)로 HTML, XML, JSON 등의 문서를 보내준다.



## 02. Flask 설치를 위한 bash 창 명령어

pip install Flask

(pip list에서 지금까지 설치된 모듈의 목록을 볼 수 있다.)



## 03. (a)에 들어갈 코드와 그 의미를 설명

```python
#_________(a)__________#

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

```

↓

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```


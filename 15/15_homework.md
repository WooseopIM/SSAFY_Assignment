# 15_Homework	`Django: Web Framework for Python`, `Template과 View`

## 01. render

> Django에서는 특정 html을 보여주기 위하여 views.py에서 render 함수를 사용한다. 빈칸에 들어갈 코드를 작성해라

```html
<h1>
    Hello, {{ name }} !
</h1>
```

```python
def hello(request, name):
    context = {
        'name': 'ssafy'
    }
    return render(request, 'hello.html', context)
```



## 02. Django 프로젝트의 template 탐색
> Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 앱 폴더 안의 `___(A)___` 폴더 내부를 탐색한다. (A)에 들어갈 폴더 이름은?

```python
templates
```


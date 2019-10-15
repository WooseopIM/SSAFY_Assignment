# 17_Homework	`Django`

> Django Form Class의 선언과 활용

## 01. 모듈 import

> Django Form Class를 만들 때, Django에 내장되어 있는 모듈을 import하고 해당 모듈에 정의된 Class를 상속받아야 한다. 해당 모듈을 import하는 코드를 작성하라.

```python
from django import forms
```

## 02. form 렌더링

>Form Class를 Template에서 활용하기 위해서 변수 form에 Form Class의 인스턴스를 할당하여 Template으로 전달하였다. Template에서 < p> Tag로 감싸진 form을 렌더링하기 위한 코드를 작성하라.

```html
{% load bootstrap4 %}
<form>
  {% bootstrap_form form이름 %}
</form>
```

## 03. 유효성 검사

> Form Class를 활용할 때, Form에 담긴 데이터가 유효한지 체크하기 위해서 is_valid() 메소드를 활용하였다. 유효성 검사를 통과한 후, 유효한 데이터를 가져오기 위하여 빈칸 (a)에 들어가야하는 코드를 작성하시오. (단, StudentForm Class는 forms.Form을 상속받았다고 가정한다)

```python
def create(request):
if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
        name = form.__(a)__.get('name')
        age = form.__(a)__.get('age')
```

```
답: cleaned_data
```


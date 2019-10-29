# 21_Homework	`Database <1:N 관계>`

## 01. html 파일에서 for문 작성

> Question 모델과 Comment 모델이 1:N 관계를 형성하고 있을 때, 하나의 
> Question을 보여주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html 파일이 있을 때, 모든 Comment의 content를 h3 태그를 이용하여 출력하는 for문을 작성하자.(단, related_name은 설정하지 않았다고 가정한다.

```html
{% extends 'base.html' %}
{% block body %}
<h1>{{ question.title }}</h1>

<!-- 여기에 들어갈 코드를 작성하시오 -->
{% for comment in comments %}
  <h3>{{ comment.content }}</h3>
{% endfor %}

{% endblock %}
```


## 02. Form 태그의 action 속성값
> 다음과 같은 urls.py 파일이 있을 때, comment를 작성하는 form을 만들기 위하여 form 태그 안에 action 속성 값으로 넣어야 하는 경로를 작성하라.

```python
app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name-'detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/create/', views.comments_create, name='comments_create'),
]
```

```html
<form action="{% url 'questions:comments_create' %}" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  여기에 내용이 들어가지요
</form>
```


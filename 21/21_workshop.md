# 21_Workshop	`Database <1:N 관계>`

## 01. 투표를 위한 설문app 만들기

> 질문에 대한 답변을 투표하여 각각의 항목이 몇 표를 받았는지 기록하는 기능을 가진 설문 app을 만들려고 한다. 설문 app은 Question 모델과 Choice 모델로 구성되어 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 형성하고 있다.
>

| Model name |                        Columns                         |
| :--------: | :----------------------------------------------------: |
|  Question  |                 title(제목): CharField                 |
|   Choice   | content(내용): CharField / votes(투표수): IntegerField |

> HTML 파일에 아래와 같은 코드가 작성되어 있다고 할 때, Choice의 내용과 투표수를 출력하는 코드를 작성하자

```html
<h1>{{ question.title }}</h1>
<ul>
  {% for choice in choices %}
  <p>
    <li>{{ choice.content }} : {{ choice.votes }}표</li>
  </p>
  {% endfor %}
</ul>
```


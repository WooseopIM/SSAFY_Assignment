# 20_Workshop	`Database <1:N 관계>`

## 01. 투표를 위한 설문app 만들기

> 질문에 대한 답변을 투표하여 각각의 항목이 몇 표를 받았는지 기록하는 기능을 가진 설문 app을 만들려고 한다. 설문 app은 Question 모델과 Choice 모델로 구성되어 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 형성하고 있다.
>
> 아래와 같은 컬럼을 가지고 있는 Question 모델과 Choice 모델을 정의하는 models.py 코드를 작성하자.

| Model name |                         Columns                         |
| :--------: | :-----------------------------------------------------: |
|  Question  |                 title(제목): CharField                  |
|   Choice   | content(내용): CharField<br>votes(투표수): IntegerField |

```python
class Question(models.Model):
    title = models.CharField(max_length=300)
    
class Choice(models.Model):
    content = models.CharField(max_length=300)
    votes = models.IntegerField
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
```


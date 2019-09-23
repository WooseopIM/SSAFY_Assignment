# 20_Homework	`Database <1:N 관계>`

## 01. 1:N 관계 모델 설정에 필요한 코드

> School 모델과 Student 모델을 1:N 관계로 설정하려고 한다. models.py의 Student 모델에서 필요한 코드를 작성해라

```python
# 정답: ForeighKey
class Student(models.Model):
    name = model.CharField(max_length=100)
    student_id = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

```


## 02. 1:N 관계의 Question 모델과 Comment 모델
> ```python
> question = Questions.objects.get(id=id)
> ```
>
> 위와 같은 코드가 있을 때, views.py에서 해당 Question의 모든 Comment를 가져오기 위한 코드를 작성해라. (단, related_name은 설정하지 않았다고 가정한다.)

```python
# 정답: 
def detail(request, pk):
    # pk라는 id를 가진 글을 찾아와 보여준다
    question = Questions.objects.get(pk=pk)
    # 해당 pk를 갖는 글의 모든 댓글을 보여준다
    comments = post.comment.all()
    context = {
        'question': question,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)
    
```


## 03. ForeignKey
> 기본적으로 1:N 관계를 설정할 때, ForeignKey를 이용해서 1에 해당하는 클래스를 지정한다. 지정한 클래스가 Movie일 때, ForeignKey로 지정된 컬럼의 이름은 무엇인가?

```python
# 정답:movie
class 어쩌구(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
```


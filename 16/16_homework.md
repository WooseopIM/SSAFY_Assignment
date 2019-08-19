# 16_Homework	`Django Model`

## 01. Model

> Django에서 선언한 Model을 실제 Database에 반영하는 과정을 무엇이라고 하는가?

```python
# 정답: Migration
```


## 02. Model 필드 정의
> Model 필드를 정의할 때, CharField에는 필수로 넘겨주어야 하는 인자가 존재한다. 무엇인지 작성해라.

```python
# 정답: max_length

def _check_max_length_attribute(self, **kwargs):
    if self.max_length is None:
        return [
            checks.Error(
                "CharFields must define a 'max_length' attribute.",
                obj=self,
                id='fields.E120',
            )
        ]
    elif (not isinstance(self.max_length, int) or isinstance(self.max_length, bool) or self.max_length <= 0):
        return [
            checks.Error(
                "'max_length' must be a positive integer.",
                obj=self,
                id='fields.E121',
            )
        ]
    else:
        return []
```


## 03. Python Shell
> Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어떠한 명령어를 통해 해당 Shell을 실행할 수 있는가?

```bash
# 정답: 
$ python manage.py shell
```


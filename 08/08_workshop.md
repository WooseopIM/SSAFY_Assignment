# 08_Workshop	Flask 기본 구조

## 01. Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 나만의 영어 단어장 페이지를 만들어보자.

|     주소(route)      | /dictionary/<string:word> |
| :------------------: | :-----------------------: |
| 페이지에 표시할 내용 |     예) apple은 사과      |

```python
from flask import Flask

app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def words(word):
    #word를 찾아서 뜻을 보여준다.
    my_dict = {'apple':'사과', 'banana':'바나나', 'melon':'멜론'}
    if word in my_dict.keys():
        return f'{word}은(는) {my_dict[word]}!'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'
```


# 30_Workshop	`JavaScript 문법`

> JavaScript 기본 문법에 대한 이해

## 01. Python to JavaScript

> 아래의 Python 코드를 JavaScript 코드로 다시 작성하자.
>
> 변수 및 함수 이름은 JavaScript naming convention(lowerCamelCase)을 따른다.
>
> Python의 F String은 JavaScript의 Template Literal을 사용한다.

```python
def concat(str1, str2):
    return f'{str1} - {str2}'

def check_long_str(string):
    if len(string) > 10:
        return True
    else:
        return False
    
if check_long_str(concat('Happy', 'Hacking')):
    print('LONG STRING')
else:
    print('SHORT STRING')
```

```javascript
const concat = function (str1, str2) {
    return `${str1} - ${str2}`
}

const checkLongStr = function (string) {
    if (string.length > 10) {
        return true
    }
    
    else {
        return false
    }
    
}

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING')
}
else {
    console.log('SHORT STRING')
}
```

```base
>>> LONG STRING
```


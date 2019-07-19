# 03_Workshop

## 01 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요

```python
# 1. 조건표현식(Conditional Expression) 사용
def palindrome():
    word = input('단어를 입력해주세요: ')
    
    result=True if word == word[::-1] else False
    return result

print(palindrome())



# 2. 일반 조건문 사용
def palindrome():
    word = input('단어를 입력해주세요: ')
    
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome())
```


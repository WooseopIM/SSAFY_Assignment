# 26_Workshop	`Django-Auth`

> Django Auth 모듈에 관한 이해

## 01. 로그인 form 만들기

> 아래의 회원가입 페이지는 Django.contrib.auth.forms 모듈의 UserCreationForm 클래스를 활용한 것이다. 아래와 같은 페이지를 만들기 위하여 views.py와 template(signup.html)에 작성하여야 하는 코드는?

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == "POST"
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        context ={
            'form': userCreationForm(),
        }
    return render(request, 'accounts/sighup.html',context)
```

```html
<!-- signup.html -->
<!-- form의 action Default는 signup -->
<form>
  {{ form.as_p }}
  <input type="submit" value="제출">
</form>
```


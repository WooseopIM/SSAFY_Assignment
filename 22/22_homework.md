# 22_Homework	`Database Validations`

## 01. Django Model Validator

> Django Model Validator는 Database에 저장될 값이 정해진 조건에 맞지 않으면 `특정 오류`를 발생시켜 값이 저장되지 않도록 한다. 이 때 발생하는 오류가 어떤 오류인가?

```python
# ValidationError
```
```python
# 공식문서
The ValidationError exception is raised when data fails form or model field validation

ValidationError는 데이터가 형식 또는 model field 유효성 검사에 실패하면 발생한다. 공식문서에서는 ValidationError에 대한 다음 source code를 확인할 수 있다.
```

```python
class ValidationError(Exception):
    """An error while validating data."""
    def __init__(self, message, code=None, params=None):
        """
        The `message` argument can be a single error, a list of errors, or a
        dictionary that maps field names to lists of errors. What we define as
        an "error" can be either a simple string or an instance of
        ValidationError with its message attribute set, and what we define as
        list or dictionary can be an actual `list` or `dict` or an instance
        of ValidationError with its `error_list` or `error_dict` attribute set.
        """
        super().__init__(message, code, params)

        if isinstance(message, ValidationError):
            if hasattr(message, 'error_dict'):
                message = message.error_dict
            elif not hasattr(message, 'message'):
                message = message.error_list
            else:
                message, code, params = message.message, message.code, message.params

        if isinstance(message, dict):
            self.error_dict = {}
            for field, messages in message.items():
                if not isinstance(messages, ValidationError):
                    messages = ValidationError(messages)
                self.error_dict[field] = messages.error_list

        elif isinstance(message, list):
            self.error_list = []
            for message in message:
                # Normalize plain strings to instances of ValidationError.
                if not isinstance(message, ValidationError):
                    message = ValidationError(message)
                if hasattr(message, 'error_dict'):
                    self.error_list.extend(sum(message.error_dict.values(), []))
                else:
                    self.error_list.extend(message.error_list)

        else:
            self.message = message
            self.code = code
            self.params = params
            self.error_list = [self]

    @property
    def message_dict(self):
        # Trigger an AttributeError if this ValidationError
        # doesn't have an error_dict.
        getattr(self, 'error_dict')

        return dict(self)

    @property
    def messages(self):
        if hasattr(self, 'error_dict'):
            return sum(dict(self).values(), [])
        return list(self)

    def update_error_dict(self, error_dict):
        if hasattr(self, 'error_dict'):
            for field, error_list in self.error_dict.items():
                error_dict.setdefault(field, []).extend(error_list)
        else:
            error_dict.setdefault(NON_FIELD_ERRORS, []).extend(self.error_list)
        return error_dict

    def __iter__(self):
        if hasattr(self, 'error_dict'):
            for field, errors in self.error_dict.items():
                yield field, list(ValidationError(errors))
        else:
            for error in self.error_list:
                message = error.message
                if error.params:
                    message %= error.params
                yield str(message)

    def __str__(self):
        if hasattr(self, 'error_dict'):
            return repr(dict(self))
        return repr(list(self))

    def __repr__(self):
        return 'ValidationError(%s)' % self
```



## 02. Django Bulit-in Validator

> 공식 문서를 통해 Django의 Bulit-in Validator에는 어떤 것들이 있는지 찾아 3가지 이상 작성
>
>  https://docs.djangoproject.com/en/2.2/ref/validators/ 

```python
# 1. RegexValidator
class RegexValidator(regex=None, message=None, code=None, inverse_match-None, flags=0):
    pass
==> The regular expression pattern to search for within the provied value, or a pre-compiled regular expression. By default, raises a ValidationError with message and code if a match is not found


# 2. EmailValidator
class EmailValidator(message=None, code=None, whitelist=None):
    pass


# 3. URLValidator
class URLValidator(schemes=None, regex=None, message=None, code=None):
    pass
```




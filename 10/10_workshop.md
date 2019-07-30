# 10_Workshop	`HTML, CSS`

## 01. 

#### 몇 번째 단락이 빨간색으로 변하는가? 

##### `첫번째 단락이 선택됨`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <style>
    #ssafy > p:nth-child(2) {
        color: red;          
    }      
  </style>
  <div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
</body>
</html>
```



#### nty-child 대신 nth-of-type을 사용하면 몇 번째 단락이 파란색으로 되는가?

##### `두번째 단락이 파란색으로 변함`

```html
<style>
  #ssafy > p:nth-of-type(2) {
      color: blue;          
  }      
</style>
```


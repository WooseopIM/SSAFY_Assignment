# 09_Workshop	Semantic Web

## 01. 클릭하면 싸피닷컴으로 이동하는 버튼 만들기

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
  <a href="https://www.ssafy.com/"><button>누르면 SSAFY.com으로 이동합니다.</button></a>
</body>
</html>
```



## 02. 태그에서 잘못된 부분을 찾아 올바르게 수정

수정 전

```html
<img href="https://picsum.photos/200" alt="">
```

수정 후

```html
<img src="https://picsum.photos/200", alt="설명도 넣어주면 좋지">
```



## 03. Resume.html 로컬 이미지 보여주기.

```html
<img src="file:///C:/TIL/SSAFY/Image/my_photo.png" width="300" height="200">
```

> 파일 크기는 그냥 임의로 넣어봄
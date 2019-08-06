# 12_Homework	`Responsive Web`

## 01. 반응형 웹디자인의 의미

> 반응형 웹디자인이란 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 `Device`에 따라 가로폭이나 배치를 변경하여 가독성을 높이도록 하는 웹페이지 접근기법이다.



## 02. 모바일 디바이스에서 반응형 웹의 정상 동작 조건

>반응형 웹이 정상적으로 동작하기 위해서는 head tag 내부에 특정 meta tag를 정의하여야 한다.

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
```

html에서 `!+tab`을 하면, 자동으로 태그들이 완성되는데 그 중 `<head></head>` 안에는 여러 meta tag들이 생성된다. 그 중 아래에 있는,

```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
```

meta tag는 반응형 웹의 정상 동작에 필요한 특정 meta tag이다.



## 03. Bootstrap의 5개 반응형 그룹

> 부트스트랩에서는 총 5개의 반응형 그룹으로 나누어 화면 크기별로 다른 Layout이 표시된다.
>
> 5개의 그룹을 구분 짓는 화면 크기의 가로 해상도 4가지 px단위.

```html
Extra small: No media query for 'xs' since this is the default in Bootstrap
Small: >= 576px
Medium: >= 768px
Large: >= 992px
Extra large: >= 1200px
```


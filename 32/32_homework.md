# 32_Homework	`JS Event Listener`
## 01. querySelector() `vs` querySelectorAll()
>JavaScript에서 자주 사용하는 다음 Event Listener들에 대해서 각각 어떤 Trigger를 의미하는지 조사하여 간단하게 작성하자.

- click(`MouseEvent`)
  - The event occurs when the user clicks on an element
  - 사용자가 특정 엘레먼트를 클릭했을 때 보여줄 동작을 Event Listener 안에 정의해줄 수 있다.
- mouseover(`MouseEvent`)
  - The event occurs when the pointer is moved onto an element, or onto one of its children
  - 화면상에 보이는 마우스포인터가 어떤 엘레먼트나 그 자손 엘레먼트 위로 올라 갔을 때.
- mouseout(`MouseEvent`)
  - The evnet occurs when a user moves the mouse pointer out of an element, or out of one of its children
  - 사용자가 마우스포인터를 어떤 엘레먼트나 그 자손 엘레먼트 밖으로 움직였을 때.
- mousemove(`MouseEvent`)
  - The event occurs when the pointer is moving while it is over an element
  - 마우스포인터가 어떤 엘레먼트 위에서 움직이고 있을 때
- keypress(`keyboardEvent`)
  - The event occurs when the user presses a key
  - 사용자가 어떤 키(KeyboardEvent)를 눌렀을 때
- keydown(`keyboardEvent`)
  - The event occurs when the user is pressing a key
  - 사용자가 어떤 키를 계속 누르고 있을 때
- keyup(`keyboardEvent`)
  - The event occurs when the user releases a key
  - 사용자가 누르고 있던 키를 뗐을 때
- load(`UIEvent`)
  - The event occurs when an object has loaded
  - 어떤 객체가 로드될 때.(수업 중 Giphy 실습의 경우, `GiphyAPICall`에 대한 server의 response가 잘 도착했는지 확인할 때 load EventListener를 사용했다)
- scroll(`UIEvent`)
  - The event occurs when an element's scrollbar is being scrolled
  - document view나 element가 스크롤 될 때
- change
  - The event occurs when the content of a form element, the selection, or the checked state have changed (for `<input>`, `<select>`, `<textarea>`)
  - 사용자가 input, select, textarea 태그에 대해서 요소 값 변경을 커밋했을 때.
  - 입력 이벤트와는 달리 변경 이벤트는 요소 값이 변경 될 때마다 발생하진 않는다.
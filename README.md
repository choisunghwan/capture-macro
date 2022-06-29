# capture-macro

e-book 사용시 불편함을 해결하고자 개발하였음. (2022-06-29)

 대부분 e-book 은 캡처가 금지되어 있다. 
 
 하지만 불법적인 공유 목적이 아닌 개인적으로 태블릿에 있는 '삼성노트', '굿 노트' 에서 ebook을 불러와 필기하고 싶은경우도 있다.
 또한 2in1 노트북(?) 인 경우 필기자체가 안된다고 한다. 불법 공유 목적이 아닌 이외 여러 다양한 이유와 목적으로 사용되었으면 좋겠다.
 
 + yes24 인 경우 해당 매크로를 실행시키더라도 '우측 입력' 즉, 페이지 넘기기 가 안된다. yes24 측에서 막아둔거 같다.
 
 ->해결법: 블루스택 or 녹스 프로그램을 pc에 설치하여 yes24 ebook을 열어서 해당 메크로를 그 위에 실행시키면 된다.
 
 실행방법
 
 0. 캡처 프로그램이 필요한데, scapture(에스캡처) 를 설치해야한다.
 ![image](https://user-images.githubusercontent.com/33335762/176366298-7d17f020-9781-4d3a-9c9f-cfd3649f3f84.png)
+ 에스 캡처 실행시, 작은 창이 뜰텐데 '상세'를 클릭한다.

![image](https://user-images.githubusercontent.com/33335762/176366507-a5fa47db-f152-44fe-979b-fafacd138473.png)
+ 그후, 위 사진에 '캡처하기 버튼' 을 자동으로 마우스가 클릭할 수 있도록  위치값 코드를 수정해주면 된다.

 1. 터미널 창(ctrl+shift+`(틸다)) 을 연후, 파이썬 파일(capture macro.py)을 실행시키면 자동 매크로 실행이 된다.
 2. 파이썬 파일(win_size_check) 은 매크로 파일을 실행시키기 위해 자동으로 클릭될 마우스 좌표 값이 필요한데(0번에 위치값이 필요하다
 언급했던것), win_size_check 파일을
 실행시키면 화면 사이즈와 마우스가 있는 좌표값을 출력한다. <*아래 사진 참고>
 
![image](https://user-images.githubusercontent.com/33335762/176366076-1f8b5d92-9a68-4e48-80a9-7333ae4a498d.png)






개발 참고 영상:https://www.youtube.com/watch?v=w2HchQQdQzA

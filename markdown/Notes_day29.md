# Day29_230105 목  

1. 어제 한 것 
소프트웨어 배포 했을 때 장고 개발용 시크릿 키는 올리면 안되고, 서버컴퓨터에 따로 깔아줌. 

   - 장고 설치
   - 프로젝트 파일 생성
   - 앱폴더 생성
   - settings.py 에 APP 등록, DIR설정

- 간단 복습 예제    
```sh
review/hello/ > view hello 함수 실행 > hello.html 을 응답 (렌더)
```
1. 오늘 한 것 

압축풀기  : 현재 위치에 내용물 압축풀기, 특정폴더에 압축풀기 

```sh
템플릿안 앱 단위 폴더 구분
Settings.py에 등록되어있는 APP순서를 따라서 templates 폴더 안의 html을 찾아주기 때문에 동일한 이름의 html파일을 구분해줄려면 각각의 html파일을 한 군데에다 모아두는 폴더를 만들어 준다. 
 - URL 변수화 app name, pattern name ( {% url 템플릿 폴더이름:키값 %})
```
   
    - 요청 프로세스의 URL과 views.py 의 function은 1:1 대응
    - form , action, name 
    - CSRF (Cross Site Request Forgery) 설정
    - form 에서 POST로 인자를 넘길려면 CSRF 토큰, input tag에는 name 이 정의되어 있어야 함. 
    - QueryDict 는 딕셔너리와는 다르지만 비슷한것 
    - 사용자가 제출한 데이터를 받을려면 요청 - 응답 사이클 2번 필요 

```sh
원리 정리 
- Request(URL) > SERVER.Django.Framework > Response
- urls.py > views.py 함수 작업 > return html 파일 
```
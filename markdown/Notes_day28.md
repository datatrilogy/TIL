# Day 28_230104
- Static Web
- Dynamic Web (Web App)
- 프레임워크와 라이브러리

```sh
git push를 잘못했다면 
Git add
Git commit —amend
Add html files & txt
Vi text 파일 수정 후 : x 엔터
```
- github.io : html & CSS로 관리 
- 구체적인 경로와 파일을 입력안하면 index.html을 찾아서 보여준다. 


- Django MTV(MVC) 모델 (Django roadmap)
![img](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction/basic-django.png)

|그 외 언어||파이썬|
|-|-|-|
|Model|DB|Model
|View|HTML|Template|
|Controller|관리자 Response|View|

```sh
- Framwork 요청이 들어오면
-  URL/ dir.A 먼저구분하고 / dir.a # 프로젝트 폴더 urls 
-  URL/ dir.A / dir.a 구분 # 하위 앱 폴더 urls
- views.py 의 함수 실행 
```

- : Framkework Design pattern
- 작업. 일의단위 : 함수
- path(url, func) : url이 들어오면 일을(함수를) 일을 한다. 
- Flask와 유사하다. 
- URL Pattern과 그에 대응하는 함수로 이루어져 있다.
- 혹은 python에서는 class-based views로 생성하기도 한다. 
- html에서 Emmet을 사용하고 싶다면 별도의 툴킷 설치필요
- 장고는 특수문법 인식
- 출력을 원한다면 중괄호 2개 
- 장고 html 주석 : 웹브라우저 JSconsole에서도 안보임
 
|Language|Frameworks|
|-|-|
|Ruby|Rails|
|JAVA|Spring|
|Javascript|Express|
|Python|Django|

```sh
pip install django==원하는 버전 
```
- (Python package index에 등록되어있기때문에Pip install 가능 )
- Dependency : 프레임 워크 하나를 깔아도 하나만 까는게 아니라, 의존하는 여러가치 툴들을 같이 설치한다. 
```sh
django-admin start project (프로젝트폴더 생성)
```
```sh
python manage.py startapp (앱폴더 생성)
```
```sh
python manage.py runserver (서버 시작)
```

```sh
Django 간단 실습 예제
1. '/hello/lunch/'로 요청이 들어오면
2. 'views.py'의 'lunch'함수를 실행함
3. 'lunch'함수는 'lunch.html'파일을 응답함
4. 'lunch.html'에는 
'<h1>LUNCH</h1>을 표시.
```

```sh
1. /hello/lotto > hello.lotto 함수 실행
2. Response > lotto.html
3. 브라우저에 랜덤 숫자 6개 출력 
```




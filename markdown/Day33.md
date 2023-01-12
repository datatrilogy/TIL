# Day33_230111수

1. 개요

1_1. 코드를 짜는 기본 두가지 방법
```sh
선언형 프로그래밍
명령형 프로그래밍
```
- 메타 클래스
- 클래스 메타 
- 클래스의 클래스 타입
- 비유 : 택시기사님한테 길 찾아달라고 할 때 
```sh 
명령형 프로그래밍
request.POST 접근 
어쩌고 저쩌고 이렇게 저렇게 하고 나서
렌더 하겠다. 동사위주느낌 
```
```sh
class Meta:
    model = 
    fields = (argument, argument, ) # 와우
```
- 글로벌 파이썬
- 독립개발환경

2. 터미널 코드 복기_ 실행 명령어

2_1. 장고 프로젝트 개발 환경 셋팅

- 프로젝트 생성

```sh
mkdir FORM
cd FORM
python -m venv venv
touch .gitignore README.md
source /FORM/venv/bin/activate
pip install django==3.2.16 django_extensions
pip list
pip freeze > requirements.txt
pip install django_extensions
```

- 필요한 파이썬 패키지 대략적 내용
```sh
asgiref 동기식 네트워크 응답 방식 / 비동기식 
sqlparse ORM이 해석할 때 쓰는 패키지 
pytz 타임존용 라이브러리 
```

- 앱폴더안에 urls.py와 forms.py 가 없어도 돌아간다. 
- urlpatterns 를 써두기 위해 따로 urls.py를 만들어준다. 

```sh
mkdir -p templates/classroom
장고 native apps
원래 이 타이밍에 git commit -m 'initproject'
```

2_2. 초기 골격 DB 구상 : DataBase Modeling

|Table name: Student|charfield|floatfield|charfield|integerfield|
|-|-|-|-|-|
|id|name|GPA|major|age|

- Entity Relationship Diagram : ER diagram
- 개체들 간의 관계를 나타낸 다이어그램 
  
|Student||
|-|-|
|id|int(pk)|
|name|varchar|
|GPA|float|
|age|int|

2_3. models.py에 구현 후 DB 생성 
- 현위치 확인필수, 최상단 디렉토리 manage.py 있는 곳에서 명령어 실행

```sh
python manage.py makemigrations
python manage.py migrate
```

2_4. 코드 구현
```sh
요청 프로세스 : URL > VIEW > MODEL 
코드 짤 때 순서 : MODEL > VIEW > URL
```

```sh
superuser admin 생성 해도 됨 
```

3. 수강생들 사이에서 자주 나왔던 에러 
```sh
ModuleNotFoundErro:No module named 
```

4. 정규표현식이란 ? 
   - forms.py를 통해 구현해준 ModelForm 조건 설정 대신 정규표현식으로 설정 가능 
   
```sh
django form regex
regular expression
regex tester
RegexValidator
example : 폰번호 정규표현식
```

5. 추가 공부 

5_1.오늘 언급한 응답 코드 

- HTTP Response 401 402 403 404 405

- [HTTP Response Status Code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [HTTP Request Method](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)

5_2. View Decorators

```sh
from django.views.decorators.http
```

```sh
import
```

```@require_http_methods(["GET", "POST"])``` 
```@require_GET()```
```require_POST()```
```@require_safe```

5_3. HTML 코드 개선 

ㄱ. ```html extends 와 include``` 

|html|extends|include|
|-|-|-|
||확장해서 다른 파일에서 끌어다 사용|부품처럼 만들어 놓고 비어있는 곳에 끼워넣어 사용|

ㄴ. Bootstrap으로 HTML 웹에서 보기 예쁘게 구현.

- 새로 프로젝트를 시작할 때는 새롭게 깔아줘야함
```sh
pip install bootstrap5 
```

- 마진 설정, index.html, base.html 수정 . 슬랙, 깃허브 참고
- 새로 글을 생성할 때, 글을 수정하고 저장할 때 각각 두개의 함수가 필요했지만, forms.py에서 ModelForm을 이용해서 하나의 함수로 만들어줌
- 두 경우의 출력 화면 HTML이 굉장히 유사함. Form action의 URL 주소가 다르다는 것만 제외하면 똑같음.
- 아무것도 입력하지 않았을 때 URL 요청시 자기자신, 현재 그 URL로 다시 가기 때문에, 두 가지 HTML 파일을 하나의 파일로 표현가능
- urlpatterns 경로 수정 후 불필요하게 많은 HTML 파일 줄여줌
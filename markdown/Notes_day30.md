# Day30_230106금 

## SQL : Structed Query Language
- 데이터 베이스 모델링 
- DB
- TITO Trash In, Trash Out  
- 데이터는 항상 존재해왔고, 떠다니고 휘발되는 데이터를 저장하지 않았을 뿐이다.
- 데이터 기반 의사결정에 도움
 
|RDBMS|NoSQL|
|-|-|
|Excel|메모장 |
|Relational DataBase Management System||

- 엑셀 스프레드 시트 <> 메모장
- Table <> Documnet 
- 메모장에는 내가 쓰고 싶은대로 쓸 수 있다. 


```sh
RDBMS, SQl 
행과 열로 구성되어 있고, 새로운 값이 들어왔을 때 처리하기가 힘들다. 
열이 추가되어야 하기 때문에, 깔끔하고 처리빠르고, 구조화가 되어있기 때문에 할 일이 밖으로 벗어나지 않는다. 
```


```sh
- 유료 DB 서비스 예 : 오라클  
- 무료로 제공되는 서비스는 문제가 생겼을 때, 책임을 질 누군가가 없다. 
- 사후처리를 해주기 때문에 사용한다. 
```
```sh
- MySQL, postgreSQL, SQLite ,Maria DB
- 각각의 SQL이 다르다 
```
### Django에서 DB구현해보기
1. 개요
- db.sqlite3
- 데이터 베이스의 데이터 타입은 기본적으로 파이썬과 다르다. 
- CRUD
- Create Retrieve(Read) Update Delete
- 테이블과 레코드, Entity(개체)
- M:N
  
- 활용분야
```sh
ERP (전사적 자원관리. 회계,인사,생산,물류)
대표적 기업 SAP / 사용언어 ABAP
```  

```sh
코드가 길어지는 구간
- 조회(Retrive)를 어떤 형태로 하느냐
- 테이블 간에 관계가 형성되었을 때 어떻게 구성되어 있는지에 따라 구현할 때 어려움이 있다.
```
```sh
ORM : Object, Realtional DB, MAPPER
```
2. 구현
2_0. 준비물
```sh
VSCODE, SQLlite 뷰어 설치
```
- 데이터베이스는 파일로 이루어져있지 않고, 프로그램으로 관리하는데, dbsqlite3의 경우 특이하게 파일이다. 
  
```sh
1. 장고 프로젝트 생성
2. 앱폴더 생성 후 , Settings.py에 APP 출생신고, DIR에 BASE_DIR / 'templates' 폴더 디폴트 값 설정. 
3. db.sqlite3생성
4. 최상위 폴더 crud.py에 생성 적어볼 코드 미리 작성 
5. models.py에 구현할 DB 클래스 생성
```
2_1. 클래스 구현 방법
```sh
엑셀에 구현되어 있는 표를 생각하며 DB를 만들어보자.
- 각각의 한줄을 아티클로 받아서 클래스를 정의해줌 (models.py)
- 타입(자료형)지정
- DB랑, 연계할 수 있게 models.Model 상속 받아주기 
- 자료형 지정, charfield max length 지정
```
2_2. 터미널 명령어 실행
```sh
- django-admin startproject board .
- python manage.py makemigrations board / 가안 만들어주기.
- primary key 확인
- python manage.py board migrate 
- python manage.py board 
- python manage.py shell
```
- Timestamp : updated, created 

```sh
# DB 생성 코드 복기 . 
from board.models import Article

# Create
# 1
article = Article()
article.title = '1번글'
article.content = '내용'
article.author = '작성자'
article.save()

 # 2. 
 article = Article(title='2번글', content='테스트', author='까마귀')
 article.save()

# 3. 
Article.objects.create(title='3번글', content='고양이', author='강아지')

# Read / Retrieve
# objects > 매니저
Article.objects

# 단일 조회
article = Article.objects.get(id=1)
article = Article.objects.get(pk=1)
article.id ; article.pk
article.title
article.content
article.author

# 전체조회
articles = Article.objects.all()
for article in article:
    print(article.title)

## Update ( 수정 )

article = Article.objects.get(id=3) # 먼저 수정할 게시글을 고르고,
article.title = '수정한 글'
article.content = '바뀌어라 얍'
article.save()

# Delete / Destroy (삭제)
# 조회로 불러와서, 삭제 
article = Article.objects.get(id=5)
article.delete()
# 삭제하고 새로 하나 만들어줘도 아이디는 그 다음 걸로 넘어간다. 
```
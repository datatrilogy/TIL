# Day34_230112
- 아직 정리안됨

agility
Agile Methodology
Waterfall 

Python -m venv env
Python manage.py shell
Source venv/bin/activate

Primary key - foreign key

Postgre	
관계형 데이터의 무결성 
의존 독립
 One To Man
Many to Many

Data를 채워본다

DB 엑셀표에 실제로 넣어보기 

Id 값을 들고 올때 model.py에 Foreign Key
_id 안붙여줘도 알아서 데이터베이스에 붙여줘서 컬럼 만들어 준다

 
Pip freeze > requirements.txt  지우고 새로 작성
Pip freeze >> requirements.txt append 있는거에 덮어씀

Viscose icons

Query : DB에 뭔가 요청하거나 명령하는 모든 작업 
Query를 날린다. 

Not NULL constraint failed : board_comment.article_id

아 . NULL >>DB 에서 에러가 났구나

Comment.article_id = 1
Comment.article = article
Comment.save 

모델 속성으로 할당하기 보다는 모델 자체를 불러주면 pk값을 알아서 들고온다 

존재하지 않는 pk 값을 할당 시켜줬을 때 숫자로 받는게 아니라, 필드 자체가 foreign key 이기 때문에 
Integrity error 

종속되어있는 상위 테이블 확인할때 테이블 모델명을 부르는게 아니라 하위 테이블 클래스에 정의 되어있는 ForeignKey Field 이름을 불러준다. 

ipython
CTRL + L

=====================
껐다 켜서 
Python manage.py shell plus —print-sql

a.save()
UPDATE

==========================
오후 
Model Form 
class Meta:
auto_now_add=True 
auto_now=True
필드가 이 두 가지 중 하나를 포함하면 Form에 포함하지도 않고 검사도 안한다. 

Authorization
authentication

```sh
Article = Article()
Article.title =
article.content
article.save()
Article

comment = Comment()
Comment.content

comment.save
<bound method Model.save of <Comment: Comment object (None)>>

comment.save()
NOT NULL constraint failed: board_comment.article_id
IntegrityError: NOT NULL constraint failed: board_comment.article_id

comment.article_id = 1
Comment.save()
comment = Comment()
Comment.content = ‘간헐적단식’

article 
<Article: Article object (1)>

comment.article = article
comment.save()

a = Article.objects.get(pk=1)
c1 = Comment.objects.get(pk=1)
c2 = Comment.objects.get(pk=2)

c1.article
<Article: Article object (1)>

Comment.objects.filter(article_id=1)
<QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>


Comment.objects.filter(article=a)
FieldError: Cannot resolve keyword 'article' into field. Choices are: article, article_id, content, created_at, id, updated_at

Comment.objects.filter(article=article)
FieldError: Cannot resolve keyword 'aritcle' into field. Choices are: article, article_id, content, created_at, id, updated_at

In [24]: a.comment_set
Out[24]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x1048db850>

In [25]: a.comment_set.all()
Out[25]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>

In [26]: Comment.objects.filter(aritcle=1)
FieldError: Cannot resolve keyword 'aritcle' into field. Choices are: article, article_id, content, created_at, id, updated_at

==================
터미널 껐다 켜서 

Python manage.py shell_plus —print-sql 

a = Article()
a.title = ‘배고프다’
a.save()
INSERT INTO "board_article" ("title", "content", "created_at", "updated_at")
VALUES ('배고프다', '', '02:28:05.377730', '02:28:05.378200')
Execution time: 0.001357s [Database: default]

In [4]: a
Out[4]: <Article: Article object (2)>

In [5]: a.save
Out[5]: <bound method Model.save of <Article: Article object (2)>>

In [6]: a1 = Article.objects.get(pk=1)
SELECT "board_article"."id",
       "board_article"."title",
       "board_article"."content",
       "board_article"."created_at",
       "board_article"."updated_at"
  FROM "board_article"
 WHERE "board_article"."id" = 1
 LIMIT 21

a2.content

In [8]: a1. content
Out[8]: '메뉴추천'

In [9]: c2 = Comment.objects.get(pk=2)
SELECT "board_comment"."id",
       "board_comment"."content",
       "board_comment"."article_id",
       "board_comment"."created_at",
       "board_comment"."updated_at"
  FROM "board_comment"
 WHERE "board_comment"."id" = 2
 LIMIT 21

In [11]: c1 = Comment.objects.get(pk=1)
SELECT "board_comment"."id",
       "board_comment"."content",
       "board_comment"."article_id",
       "board_comment"."created_at",
       "board_comment"."updated_at"
  FROM "board_comment"
 WHERE "board_comment"."id" = 1
 LIMIT 21

In [12]: c1 .article
SELECT "board_article"."id",
       "board_article"."title",
       "board_article"."content",
       "board_article"."created_at",
       "board_article"."updated_at"
  FROM "board_article"
 WHERE "board_article"."id" = 1
 LIMIT 21
Out[12]: <Article: Article object (1)>


In [13]: a1.comment_set.all()
Out[13]: SELECT "board_comment"."id",
       "board_comment"."content",
       "board_comment"."article_id",
       "board_comment"."created_at",
       "board_comment"."updated_at"
  FROM "board_comment"
 WHERE "board_comment"."article_id" = 1
 LIMIT 21



```
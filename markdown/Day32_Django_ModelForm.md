# Day32_230110월

1. Day28~Day31 Django 프로젝트 복기 겸 실습예제
   - 09:15 ~ 11:40 
   - 오전까지 끝내는 것 1차 목표

1_0. 던져주신 문제 명세 (Specification) 
```sh
기존 MTV 프로젝트 내부에
startapp => board
URL => board/
model => Posting
subject : CharField(max_length=100)
description: TextField()
CRUD 가능하도록 만들기
view 함수명
C => new, create
R => index, detail
U => edit, update
D => delete
```

1_1. 과제 수행여부
||비고|
|-|-|
|완성하였는가?| 11:40 넘기고 점심시간까지 조금 사용해서 어제 쳐놓은 코드 보면서 따라 쳐서 완성하기는 했음|
|느낀 점|이해는 하고 있지만, 솔직히 어제 내가 입력해놓은 코드를 봐가며 완성해서 내가 100퍼센트 다 완성했다고 느끼지 못함. 내것이 아닌 느낌|


1_2. 강사님 코드 해설,에서 얻어갈 것 
(파이썬 파일 내가 쓴 코드위에 선생님 해설 추가)

- board/detail.HTML
```sh 
ㄱ. javascript 코드로 삭제하기 전에 한번 더 확인하기 
input type="submit" onclick="return confirm(삭제하시겠습니까?)"
```
```sh
ㄴ. HTML 코드 구현 팁 '+'
div>label+input TAB 하면 바로 div태그안에 각각 태그 생성
```
- board/views.py 
```sh
- 작성한 게시글을 DB에서 불러와서 게시글 목록을 구현할 때 Class.objects.all을 사용했는데, 이렇게 하면 일반적으로 널리 사용하는 게시글 목록과는 다른 결과가 출력된다. 
최신글이 최상단에 오는 것이 아니라, 제일 먼저 작성한 게시글이 최상단에 오게 된다. 가장 마지막에 생성한 항목을 최상단에 오게 해주자.
```
    ㄷ. Python 언어를 사용해서 내림차순 구현
```sh
Class.objects.all[::-1]
```
    ㄹ. DB를 불러오는 방식을 달리해서 내림차순 구현
  - QuerySet Order_by
```sh
Class.objects.order_by('-pk')
Class.objects.order_by('-updated_at')
```

2. 오늘의 의문점
```sh
ㄱ. form 태그와 a href태그 정확한 차이 : 해소함
secure hash algorithms
password, SHA 256 암호화, http, https, GET, POST
RESTful API  
```
```sh
ㄴ. urls.py의 url 요청을 views.py에서 어떻게 받는지  
How django processes a request?
```
[docs.djangoproject en 4.1 topics http urls ](https://docs.djangoproject.com/en/4.1/topics/http/urls/)
```sh
ㄷ. 장고 forms 가 html text area를 구현하는 방식 
장고가이드 내부코드 참조
- models.py의 클래스 인스턴스 생성과 굉장히 유사하다.
- 클래스 안에 클래스 형성 > 
```
```sh
ㄹ. 언급된 것 중에 모르는 것 . 정규 표현식 ??
```
```sh
ㅁ. Is.valid의 return 값 article_form : 맞는 문장인가? 
ㅂ. Get object or 404 정확하게 무엇을 해준것?
ㅅ. Try except 파이썬 예외처리
```

3. Refactoring

3_0. Refactoring을 위한 문제점인식 
```sh
ㄱ. 사용자 입력값은 믿을 수 없다. 들어온 입력값에 대한 검증(유효성 검사) 필요하다. 
ㄴ. views.py에 반복되는 코드가 많다. 코드 개선이 필요하다.
ㄷ. edit.html에 반복되는 div,label,input, form TAG 코드 개선이 필요하다. 
ㄹ. 올바른 에러메세지 응답을 반환해야한다. 아직 작성하지 않은 항목에 대해서 /blog/100/ 과 같이 없는 걸 요청 했을 때 
500이라고 응답할게 아니라 404로 응답해서 에러원인에 맞는 적절한 응답 화면을 내보내야한다.
```
3_1. 문제점 해결 방안
   - MTV project/ app_name=blog(DAY31에 한 프로젝트) 코드개선
```sh
ㄱ~ㄷ. 
- forms.py를 통해 Model Form 클래스를 이용해서 Meta 클래스 생성 후 
- views.py의 새로운 게시글 생성 함수에 ModelForm Class instance 생성 
- 생성된 클래스 인스턴스를 context인자로 render해서 return 값 반환
- tml에서 이중 괄호 {{}} 를 통해서 넘어온 context값 구현
- {{ article_form.as_p }} 의 as_p를 통해 블럭으로 구별 
```
- 위와 같이 하면 new, create 두가지 함수를 하나로 축소 구현가능

```sh
ㄹ.
from django.shortcuts import get_object_or_404
views.py의 detail과 update함수의 레코드 단일 조회 부분
get_object_or_404(Model, pk=model_pk)로 새로 할당
context로 모델 render 후 return
```
3_2. 실제 코드 변화 
A. 수정 전 

```sh
def new(request):
   return render(request, 'blog/new.html')

def create(request):
   article = Article()
   article.title = request.POST['title']
   article.content = request.POST['content']
   article.save()
   return redirect('blog:detail', article.pk)
```

B. 수정 후 : 함수 하나로 끝남. 

```sh
def create(request):
    if request.method =='POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('blog:detail', article.pk)
    elif request.method == 'GET':
        article_form = ArticleForm()
    context = {'article_form': article_form},
    return render(request, 'blog/form_new.html', context)
```

3_3. 새롭게 만들어 준 파일
```sh
forms.py
수정된 부분
views.py의 new, create함수
new_html의 반복되는 TAG 부분
```
[참고 : HTTP response status codes ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

3_4. 개요도, 플로우차트를 머릿속으로 한번 그려볼 것 
```sh
ModelForm의 method 'is.valid'의 return 값 : article_form
Article Form() > HTML input > Article Form (request.POST)
> 검증 > ok 저장 가능 save
> 검증 > Not ok 다시 HTML input > Article Form(request.POST)
```
3_5. KeyPoint ?? > 오늘, 어제와 다르게, 새롭게 배우고 적용한 개념
```django Class ModelForm```
- [Creating Forms From Models](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)



4. 헷갈리는 용어 정리 필요. 
- SQL```entity, fields, attributes, record, tuple```
  
![img](https://t1.daumcdn.net/cfile/tistory/993845445A67253915)
- ```QuerySet, QueryDict```
- Django 에서만 적용되는 건지, 파이썬 언어에서 적용되는 건지 헷갈림 

5. 총정리 

5_1.프로젝트를 시작할 때 해야할 생각. 가장 먼저해야할 것 
```sh
뭘 하고 싶지 ?  이걸 하고 싶네, 이제 뭐하지 ? 
무엇을 하고 싶은지에 대한 명확함이 없다면 코드로 옮기는 것은 당연히 안된다. 무엇을 해야 하는지 모르는데 코드로 옮긴다는 것 자체가 말이 안됨.
```
```sh
Django Project의 경우
DB와 내가 볼 화면을 초기에 생각을 다 해놓고 코드로 옮기자.
초기 골격, 내가 원하는 웹페이지를 구체적으로 다 구상해놓고 생각한다.
뭘 해야되지? 뭐 저장하지 ? 
```
```sh
Database modeling이 가장 중요하다. models.py
세 번 만들어보면 손에 익는다. 
에러를 많이 봐야 실력이 는다. 
일부러 틀려가며 에러를 보면서 이것 저것 고쳐보자. 
```
5_2. 추가 공부
2번과 4번을 바탕으로 추가 공부 지속. 


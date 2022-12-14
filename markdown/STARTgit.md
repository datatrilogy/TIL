# Git 기초 _ 설치부터 허브활용까지 _221212월
1일 1커밋흔적을 남겨보자 
## 깃헙 Git HUB  / GIT
### Git VCS: version control system 
공동으로 작업했을 때 누구의 잘못인지 모른다. 무엇을 수정했는지 모른다. 수정했는데 잘못하면 큰일난다. 용량이 너무 많다. 파일 양식이 통일이 안되어있다 . 그래서 만들었다. 
- 버전관리 : 수정한 내용을 주석 설명파일을 따로 둔다. 수정할 부분의 용량만 따로 추가할 수 있게 한다. 
- [깃헙책링크](https://git-scm.com/book/ko/v2)
자기를 소개하는 것이 아닌 자기가 한 것을 소개하는 것 
- [MIT 에서도 깃 안가르쳐준다.](https://missing.csail.mit.edu)
### VSC에서 깃헙 버전관리 시작하기 
- 홈 디렉토리에 일단 작업할 폴더를 만들어주자. 
- % ~
- % mkdir git-basic
- % `git init` (master 버전관리 활성화 | 비어있는 dir .git/ 이라는 폴더를 만들어줌. 단순한 파일 있는 폴더가 아니라 기능이 생김. 폴더안에 있는 모든 파일들에 대해서 버전관리 해줌 REPO라고 불러준다.)
  
# 221213 수 부트캠프12일차
```sh
프로젝트 초기화 진행
#### 계정세팅 (강사님 노트 참고해서 작성함)
% (계정당1회) 서명이 등록되지 않았다면, 계정용 서명 등록 
% git config --global user.email "개발에쓸@이메일"
% git config -- global user.name "내이름"
  ##### 서명이 정상적으로 등록되었는지 확인
% cat ~/.gitconfig
  - 로그인이 잘 되어 있는지 확인하려면
% git config (--global) user.name (user.email)
```
#### 프로젝트 생성부터 push까지
```sh
#프로젝트 폴더 생성 
% mkdir new_project
#프로젝트 폴더로 이동
% cd new_project
# README파일 & .gitignore 생성 
% touch README.md .gitignore
# gitignore.io에 접속하여 필요한 내용 복-붙 
# 폴더를 리포로 초기화 
% git init 
# README & .gitignore 파일 add(tracking)
% git add .
# commit 
% 
```

    - touch , git add, commit -m, rm, git restore
- 무슨 일이 일어난 걸까?
|헤메코 | 촬영 | 사진첩|
|-|-|-|
|작업공간|스테이지|커밋툴|
||ADD : stage에 올림|Commit:커밋 사진찍음|
|파일명옆 U:Untracked|파일명옆 A:Added|파일명 옆 M:Modified|
- commit 에 메세지 옵션 '변경사항주석 제목'
- add . 현재 디렉토리에 있는 모든 파일 한번에 스테이징
- commit은 스테이지를 찍는 것이기 때문에 따로 지정해줄 필요가 없다. 
- 명령어는 손이 외운다. 무슨 일이 일어나고 있는지 그릴 줄 알아야 한다. 
- git status, git log

### 깃허브 활용하기
* 어제는 GIT을 이용해서, 내 컴퓨터 폴더에 .git 폴더를 깔고 REPO로 업그레이드 시켜줬다면 오늘은 GIT HUB 서버컴퓨터 에도 폴더를 만들고 동기화를 시켜주는 작업을 한다. 
* GIT HUB
* ![img](/Users/macdoong/Desktop/프로그래밍 /22.11.28 ~ 부트캠프/스크린샷/REPO원리개요.png)
- % git remote add origin(별명,네임) https://서버폴더URL주소
- % git push origin master 
- % cat ~/.gitconfig 
#### 교육생들 사이에서 주로 발생한 문제
- 커밋을 안해서 저장한 마크다운 파일이 안올라감
- 로컬호스트 거부 
- 기존 유저라 브랜치가 두 개임 
### 다른 컴퓨터 사용하기 
- 새로운 컴퓨터를 쓸 때 깃헙으로부터 clone을 깔아준다. 
- pull을 해서 허브에 있는 내 파일들을 받아준다. 
- clone 과 init이 하는 역할은 비슷하다. 
- % git bash에서 git status / % git push origin master
- % Git log --pretty=oneline
- % Git log --oneline
### ✶주의사항✶ 
    1. **현재위치 어딘지 항상 확인**
    2. **Repo 안에 Repo(master)를 만들지 않는다.**
       1. 이미 git init을 실행한 폴더안에 
       2. 또 다른 폴더를 만들고
       3. 그 폴더 (하위폴더)에서 `git init`을 하지 않는다. 
       4. Master 떠있으면 init 제발 X
    3. **Home에서 init 하지 않는다.**
    4. **지금은 Github에서 직접 수정하지 않는다.**
### ✓권장사항 
    1. 커밋 : 메시지는 짧지만, 내용은 담아서
    2. 모든 Repo(프로젝트)에는 아래와 같은 파일을 꼭 만들어 포함한다. 
       1. ReadME.md
       2. .gitigonre 
          1. gitignore.io 에서 태그 포함해서 소스코드 긁어오기
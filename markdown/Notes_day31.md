# Day31_230109 월 

소프트 웨어를 새로 배포할 때 : 필요한 패키지와 패키지 버전 명시해줘야 함

```가상환경 독립개발환경``` 

오늘 쓴 명령어 정리 

```sh
% pip list
% python -m venv venv
% source venv/scripts(맥은 bin)/activate
% deactivate
% pip freeze
% pip freeze > requirements.txt
```
git .ignore

models.py 에 모델링을 할 때는 실제로 무슨 값을 채울지 생각해보고 만들면 쉽다.

RESTful API
GET : 변경이 없을 때 
POST : DB에 변경이 일어날때 
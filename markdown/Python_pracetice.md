# 예제 문제 풀이
- 221219월 부트캠프 Day 16
```sh
1. 모음 제거 하기 
    다음 문장의 모음을 제거한 새로운 문자열을 출력하세요
``` 
**[입력예시]**
```sh
'Life is too short, you need python'
```
**[출력예시]**
```sh
'Lf s t shrt, y nd pythn'
```
**문제 접근 방향** 
```sh
문제 접근 
- 스트링안에서 L에서 n까지 for문으로 순회한다.
- 자음이냐 모음이냐? 모음이면 제외하고 출력한다. 
``` 
```sh 
# 아래에 코드를 작성하세요
my_strs = 'Life is too short, you nee python'
new_str = ''
for char in my_strs:
    if char not in 'aeiou':
        new_str += char
print(new_str)
```
```sh
2. 과일 개수 골라내기 
    내 장바구니에 과일이 몇 개인지, 과일이 아닌 것은 몇 개인지 출력하세요. 장바구니에 담긴 과일과, 과일 판별 리스트는 제시됩니다. 
```
**[출력 예시]**
```sh 
과일은 23개이고, 11개는 과일이 아닙니다. 
```
```sh
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# 과일 개수 저장할 변수 / 비과일 개수 저장할 변수 
fruit_count = 0
non_fruit_count = 0 # xy 좌표 초기화 x = y = 0
# basket_items 안에 key_value 들을 돌면서 
for key in basket_items:
    #만약 key가 fruits 중에 하나라면, 
    if key in fruits:
        #fruits_count += basket_items[key]
    # 그게 아니라면
    else:
     # non_fruit_count를 value(*비과일개수*)를 더해나간다. 
        non_fuirt_count += basket_items[key]
print(f'과일은 {fruit_count}개이고, {non_fruit_count}개는 과일이 아닙니다.' )
```
```sh 
3. 영어이름 출력하기 
    영어이름은 가운데 이름을 가지고 있는 경우가 있습니다. 가운데 이름은 대문자로 축약해서 나타내는 코드를 작성하세요. 
```
**[입력예시]**
```sh
Alice Betty Catherine Davis
```
**[출력 예시]**
```sh
Alice B. C. Davis 
```
```sh
new _ name = ''
# names 에서 각 요소를 순회하며
for idx, name in enumerate(names):
    #idx가 0과 마지막일 때는 그대로
    if idx == 0 or idx == len(names) - 1:
        new_name += f'{name} '
    #그게아니면 
    else:
        new_name += f'{name[0]}. '
print(new_name)
```
```sh
for idx in range(1,len(names) - 1):
    names[idx] = f'{names[idx][0]}.'
print(' '.join(names))
```






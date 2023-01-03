# Day 27_230102 화
HTML과 CSS

[CSS레이아웃 FLEXBOX 게임](https://flexboxfroggy.com/#ko)

```sh
Main Axis(주축), Cross Axis(교차축)
Reverse : 축의 방향이 바뀜 
```
```sh
Justify-content: 주축을 기준으로 움직임
* flex-start: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
* flex-end: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
* center: 요소들을 컨테이너의 가운데로 정렬합니다.
* space-between: 요소들 사이에 동일한 간격을 둡니다.
* space-around: 요소들 주위에 동일한 간격을 둡니다.
* space-evenly
```
```sh
Align-items : 교차축을 기준으로 정렬
flex-start: 요소들을 컨테이너의 꼭대기로 정렬합니다.
flex-end: 요소들을 컨테이너의 바닥으로 정렬합니다.
center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
baseline: 요소들을 컨테이너의 시작 위치에 정렬합니다.
stretch: 요소들을 컨테이너에 맞도록 늘립니다.
```
Align-self 
개별 요소에 적용할 수 있는 또 다른 속성입니다. 이 속성은 align-items가 사용하는 값들을 인자로 받으며, 그 값들은 지정한 요소에만 적용됩니다.
```sh
flex-direction
* row: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
* row-reverse: 요소들을 텍스트의 반대 방향으로 정렬합니다. 
* column: 요소들을 위에서 아래로 정렬합니다.
* column-reverse: 요소들을 아래에서 위로 정렬합니다.
```
```sh
flex-wrap
* nowrap: 모든 요소들을 한 줄에 정렬합니다.
* wrap: 요소들을 여러 줄에 걸쳐 정렬합니다.
* wrap-reverse: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.
```
```sh
* flex-flow
Direction 과 wrap을 블락으로 구분해서 한 줄로 처리 
```
```sh
Align-content
* flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
* flex-end: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
* center: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
* space-between: 여러 줄들 사이에 동일한 간격을 둡니다.
* space-around: 여러 줄들 주위에 동일한 간격을 둡니다.
* stretch: 여러 줄들을 컨테이너에 맞도록 늘립니다.
```

```sh
CSS Bootstrap
p m
x y e s t b
- 1 2 3 4 5 

```
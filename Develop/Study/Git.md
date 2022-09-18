![image](https://user-images.githubusercontent.com/81727895/157488416-37c84284-2d46-4d7e-802a-674db96f0340.png)

# git 기초

```git
$git config --global user.name "내 이름"

$git config --global user.email "내 메일주소"

$git status: git 상태 확인

vim 파일명: 파일 열기
```

![image](https://user-images.githubusercontent.com/81727895/157488670-e773bc02-9e0e-4021-9457-27c1a84ade5d.png)

```git
깃에서 스테이징 할때

$git add ~~~

깃 상태확인

$git status

스테이지에 올라온 파일 커밋 하기

$git commit -m "메모하고 싶은 내용"

다시 한 번 깃 상태 확인

$git status

저장소에 저장된 버전 확인

$git log

> $git log --stat
: 커밋과 관련된 파일까지 함께 살펴보기
```

방금 수정한 파일이 최신 버전과 어떻게 다른지 확인해보기

```git
$git diff
```

방금 커밋한 메시지 수정하기

```git
$git commit --amend
```

커밋 메시지가 나타나면, 제일 위에 줄을 수정하고 ex 모드로 돌아가 내용을 저장하고 빔을 종료. 

커밋 메시지가 수정되면서 이전 커밋에 더해짐.


**.gitignore 파일로 버전관리에서 제외하기**

버전 관리 중인 디렉터리 안에 버전 관리를 하지 않을 특성 파일 또는 디렉터리가 있다면 .gitignore 파일을 만들어 목록을 지정할 수 있습니다. 빔을 사용해서 .gitignore 파일을 만들어 그 안에 버전 관리하지 않을 파일 또는 디렉터리 이름이나 파일 확장자를 입력하면 됩니다. 주로 개인적으로 메모해 놓은 파일이나 프로그램 사용 중에 자동으로 생성된 swp파일, 백업 파일 등이 이 목록에 포함됩니다. 

> 예를 들어 다음과 같이 .gitignore 파일의 내용을 작성하면 mynote.txt 파일과 temp 디렉터리, 확장자가 .swp인 파일을 버전 관리에서 제외 시킬 수 있습니다.

```
my note.txt
temp/
.swp
```

>**스테이징 되돌리기**

```git
$git reset HEAD 파일 이름
```

- 스테이지에서 내릴 때 사용

>**최신 커밋 되돌리기**

```git
$git reset HEAD^
```
- 스테이징 후, 커밋까지 했을 때, 가장 마지막에 한 커밋을 취소하는 방법


> **git rest 명령의 옵션 살펴보기**

|명령|설명|
|------|---|
|--soft HEAD^|최근 커밋을 하기 전 상태로 작업 트리를 되돌립니다.|
|--mixed HEAD^|최근 커밋과 스테이징을 하기 전 상태로 작업 트리를 되돌립니다. 옵션 없이 git rest 명령을 사용할 경우 이 옵션을 기본으로 작동합니다.|
|--hard HEAD^|최근 커밋과 스테이징, 파일 수정을 하기전 상태로 작업 트리를 되돌립니다. 이 옵션으로 되돌린 내용은 복구할 수 없습니다.|

> **특정 커밋으로 되돌리기** 

```git
$git reset 복사한 커밋 해시
```

- git log 명령을 사용해서 로그 목록을 보고 커밋 해시를 복사하면 됨.

> **커밋 삭제하지 않고 되돌리기**

```git
$git revert 복사한 커밋 해시
```

# 깃과 브랜치 (Git and Branch)

> **새 브랜치 만들기**

```git
$git branch 브랜치이름
```

>**현재 저장소의 브랜치 확인**

```git
$git branch
```

> **브랜치 사이 이동하기**

```git
$git checkout 브랜치이름
```

> **--online  옵션으로 한 줄에 한 커밋씩 확인하기**

```git
$git log --online
```

> **브랜치와 커밋의 관계를 좀 더 보기 쉽게 그래프 형태로 표시하기**

```git
$git log --oneline --branches --graph
```

> **브랜치 사이의 차이점 알아보기**

```git
$git log 브랜치1..브랜치2
```

- 이렇게 하면 브랜치1에는 없고 브랜치2에만 있는 커밋만 보여줍니다.

- 브랜치1과 브랜치2 순서를 바꾸면 브랜치2에는 없고 브랜치1에만 있는 커밋을 보여줍니다.

> **브랜치 병합하기**

브랜치를 master 브랜치로 병합하는 방법

```git
$git check out master
```

- master 브랜치로 체크아웃 한 뒤,

```
$git merge 병합할브랜치
```

> **같은 문서의 다른 위치를 수정했을 때 병합하기**

ex) master 브랜치와 다른 브랜치에 똑같이 work.txt 파일이 있다면?

```git
$git check out master
```

```git
$git merge 다른브랜치
```

```git
$git log --online --branches --graph
``` 

- 지금 까지 만든 브랜치와 커밋의 관계 한 눈에 확인 가능

> **병합이 끝난 브랜치 삭제하기**

```git
$git branch

$git branch -d 다른 브랜치
```

- master 브랜치에 병합하지 않은 브랜치를 삭제하려면 오류 메시지가 나타남. 이럴 경우 옵션 -d 대신에 -D를 사용하면 강제로 브랜치를 삭제할 수 있음.

> **수정 중인 파일 감추기 및 되돌리기**

```git
$git stash
```

or

```git
$git stash save
```

- 커밋하지 않은 수정 내용을 어딘가에 보관하기

```git
$git stash pop
```

- stash 목록에서 가장 최근 항목을 되돌리기


>> stash 목록에 저장된 수정 내용을 나중에 또 사용할 것 같다?

```git
$git stash apply
```

>> stash 목록에서 가장 최근 항목을 삭제하고 싶다?

```git
$git stash drop
```

# 원격 저장소와 깃허브

> **원격 저장소에 연결하기**

```git
$git remote add origin 복사한주소붙여넣기
```

```git
$git remote -v
```

- 원격 저장소에 제대로 연결됐는지 확인

> **원격 저장소에 파일 올리기**

```git
$git push -u origin master
```

- 지역 저장소의 브랜치를 origin, 즉 원경 저장소의 master 브랜치로 푸시하라는 명령입니다. 여기에서 '-u' 옵션은 지역 저장소의 브랜치를 원격 저장소의 master 브랜치에 연결하기 위한 것으로 처음에 한 번만 사용하면 됩니다.

```git
$git commit -am "설명"
```

- -a는 스테이징 옵션, -m은 메시지 옵션
- 한 번 이상 커밋해야 가능


```git
$git push
```

- 연결 후, 다시 파일을 푸시할 때

>**원격 저장소에서 파일 내려받기**

```
$git pull
```


```
$git pull origin master
```

- origin(원격 저장소)의 내용을 master 브랜치로 가져온다는 뜻인데, git pull로만 쳐도 상관없음. 기본 우너격 저장소가 origin이고, 기본 브랜치가 master이기 때문

# 깃허브로 협업하기

> **원격 저장소 복제하기**

```git
$git clone 복제한주소 복제할디렉터리이름
```

- 복제할디렉터리이름을 쓰지않으면 자동으로 디렉터리가 만들어짐.

```git
$git remote -v
```

- 복제한디렉터리에서 위의 명령을 사용하면 연결이 되어 있는지 확인할 수 있습니다.

> **개인 컴퓨터에서 작업하고 올리기**

```git
$git commit -am "설명글"
```

```git
$git push
```

- 커밋을 원격저장소에 올리기

> **내려받아 작업하기**

```git
$git pull
```

- 원격저장소에 새로올라온 커밋을 가져옵니다.

> **수정 후 다시 올리기**

```git
$git commit -am "수정사항"
```

```git
$git push
```

> **원격 브랜치 정보 가져오기**

```git
$git fetch
```

> **다른 브랜치를 패치한 후, 최신 커밋을 현재 브랜치에 합치기**

```git
$git checkout 다른 브랜치

$git checkout master

$git merge 다른 브랜치
```

> **패치로 가져온 브랜치 한 번에 병합하기**

```git
$git merge origin/master
```

- 패치한 뒤, 병합할 때 원격 master 브랜치에 있는 커밋일 때, 위의 명령어 사용

```git
$git merge/origin/브랜치이름
```

- 다른 브랜치에 있는 커밋일 때, 위의 명령어 사용

```git
$git merge 다른브랜치
```

- 패치한 뒤, 지역 저장소에 반영하지 않은 최신 커밋을 병합

# 협업에서 브랜치 사용하기

```git
$git pull
```

- 원격 저장소에 다른 팀원들의 커밋이 추가되어 있는지 확인하기 위해 최신 커밋 정보를 가져옵니다.

```git
$git checkout -b 새로운브랜치이름
```

- 새로운 기능을 구현하기 위해 지역 저장소에 브랜치 를 만들고 만든 브랜치로 체크하웃합니다. -b 옵션을 사용하면 브랜치를 만들고 체크아웃 하는 것을 한꺼번에 할 수 있습니다.

```git
$git push origin 만든브랜치이름
```

- 원격 저장소에 새로만든 브랜치까지 함께 푸시하기. git push 뒤에 origin 새로만든브랜치를 추가하면 원격저장소에 새로만든 브랜치를 푸시한다는 의미




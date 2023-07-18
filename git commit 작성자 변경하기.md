# git commit 작성자 변경하기

### 상황

TIL를 작성하고 push를 하였는데 잔디가 심어지지 않았습니다

### 원인

로컬의 깃 계정과 깃허브의 계정이 달라 commit을 하여도 잔디가 심어지지 않았습니다

### 해결

1. git log --pretty=format:"%h = %an , %ar : %s" --graph
   - 깃 로그를 출력하여 commit을 변경할 최초 시점을 정합니다


2. git rebase -i --rebase-merges "해시코드"

   - 인터랙티브한 방식으로 merge commit을 다시 적용하는 명령어


   - 해쉬코드 이후의 커밋들 중 변경할 커밋들 앞에 pick대신 edit을 붙입니다


3. git commit --amend --author="et2468 <csm66865407@gmail.com>" 
   - 이전에 commit한 내용을 수정하고, commit 작성자 정보를 변경하는 명령어


4. git rebase --continue 

   - rebase 작업을 이어서 진행하는 명령어

   - 2, 3을 반복해서 하나하나 커밋들을 변경합니다


5. git push -f
   - 변경사항을 강제푸시하여 커밋기록을 완전히 덮어씁니다


### 해결도중 발생한 문제들

문제

merge commit을 다시 적용하는 명령어로 처음엔 `git rebase -i -p "해시코드"`를 사용하였습니다.

Git 2.18 버전에서 `git rebase` 명령의 옵션 변경으로`--preserve-merges` 옵션은 이제 더 이상 사용되지 않았습니다.

해결

`git rebase -i -p "해시코드"` 명령어를 `git rebase -i --rebase-merges "해시코드"`로 대체하여 햐결하였습니다.


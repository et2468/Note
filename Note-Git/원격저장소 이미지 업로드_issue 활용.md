# 원격저장소 이미지 업로드_issue 활용

### 0️⃣ 원격저장소 이미지 업로드_상대경로방법

- 이전에 img폴더를 만들어 상대경로로 img를 출력하며 원격저장소에 올리는 방법을 알아봤다
- 하지만 이 방법은 로컬PC에도 이미지를 첨부해야하므로 용량을 많이 사용한다



### 1️⃣ Github Issue로 이미지 업로드하기

![image-20230706160221364](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20230706160221364.png)



![image-20230706160301855](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20230706160301855.png)

![image-20230706160333342](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20230706160333342.png)

![image-20230706160431652](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20230706160431652.png)

1. Issue에 새 이슈를 생성한다
2. 이미지를 붙여넣는다 
3. 해당 이슈의 이미지 절대경로(웹주소)를 md파일에 넣는다
4. 잘 업로드 된 것을 확인한다



### 2️⃣ 피드백

로컬에 이미지를 저장하지 않아도 되서 로컬부담이 줄어든다

사진을 하나하나 다 이렇게 작업하기 힘들 것 같다

사진의 개수가 많이 없을 때 이렇게 하면 좋을듯



**이슈를 꼭 생성하지 않아도 된다

- 이슈에 이미지를 올리면 바로 github 서버에 이미지가 업로드 되기 때문에 이미지의 고유 링크가 생성된다

- 이미지를 이슈 본문에 붙여넣기 하는 순간 이미지 고유 링크가 생성되는 것이기 때문에 굳이 이슈를 발행하지 않아도 된다
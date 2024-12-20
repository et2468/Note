# 인텔리제이 JDK 연결

### 제작배경

2024.10월. 글로컬 청년취업사관학교에서 진행하는 웹 개발 준전문가 양성교육에 멘토로 참여하며, 코칭을 하게 되었습니다.

이에 프로그램을 실행해보며 효과적인 코칭을 할 수 있도록,

초대받은 github repository에서 Spring 기반의 프로젝트를 pull받아 로컬환경에서 웹 프로그램을 실행시켜보기로 하였습니다.

아래는 이를 위한 자바 웹 프로그램 실행환경 제작과정을 정리하였습니다.




### 개념정리

**인텔리제이**

-  JetBrains에서 개발한 통합 개발 환경(IDE)
- 자바(Java) 언어를 위한 강력한 기능을 제공
- 코드 작성, 디버깅, 테스트 등 개발 과정에서 생산성을 높이는 다양한 도구와 기능을 제공
- 자동 완성, 코드 분석, 리팩토링 같은 강력한 코드 편집 기능이 특징



**JDK**

- 자바 애플리케이션 개발을 위해 필요한 다양한 도구를 포함하는 패키지
- 자바 소스 코드를 작성하고, 컴파일하며, 디버깅하고, 실행할 수 있도록 필요한 모든 도구를 포함
- 컴파일러(`javac`), 디버거(`jdb`), 애플리케이션 패키징 도구(`jar`) 등이 포함

  - 이러한 도구들은 자바 프로그램의 개발, 디버깅, 배포 등에 사용
- **자바 컴파일러 (javac)**
- 자바소스코드(.java 파일)를 바이트코드(.class 파일)로 변환하여 자바가상머신(JVM)이 실행할 수 있도록 한다.
- **자바 가상머신 (JVM)**
  - 컴파일된 바이트코드를 실제 실행
  - 운영체제와 독립적으로 바이트코드를 실행하는 환경 제공
- **자바 런타임 환경 (JRE)**

  - JVM과 함께 자바 애플리케이션을 실행하는 데 필요한 라이브러리와 클래스들을 포함한 환경
  - 자바 애플리케이션을 실행할 수 있게 해 주지만, 컴파일 기능은 포함하지 않음




### 인텔리제이에서 JDK설치

인텔리제이를 사용하면 복잡하게 JDK를 다운받고, 환경변수를 설정하는 과정을 거치지 않아도 됩니다.

1. Project Structure 설정

- **[File] -> [Project Structure] -> [Project]** 선택합니다.

  - 맥 단축키: Command + ;
  - 윈도우 단축키: Shift + Ctrl + Alt + S

- ![image-20241002094812223](C:\Users\oceanlightai\AppData\Roaming\Typora\typora-user-images\image-20241002094812223.png)

  - 다운받으려는 JDK버전을 선택하고 JDK 제공 벤더를 선택합니다.

  - [Amazon Corretto](https://aws.amazon.com/ko/corretto/)는 OpenJDK의 프로덕션용 무료 멀티 플랫폼 배포입니다. Corretto는 오픈 소스 라이선스를 통해 Amazon에서 배포합니다.
  - 애플 실리콘칩(M1 칩)을 사용하고 있다면 aarch64로 다운받아줍니다.
  - 인텔리제이 21.2월 버전 이후부터 JDK 17을 지원합니다. 만약 JDK 17 이상의 버전이 보이지 않는다면 인텔리제이 업데이트가 필요합니다.
  - 언어수준은 JDK버전과 동일한 수준으로 설정하는게 좋습니다.

2. Project Setting 설정

- **앱 최상단의 [Intelij IDEA] -> [Preferences]** 선택합니다.
  - 맥 단축키: Command + ,(콤마)
  
  - 윈도우 단축키: Ctrl + Alt + S
  
- ![image-20241002095429825](C:\Users\oceanlightai\AppData\Roaming\Typora\typora-user-images\image-20241002095429825.png)

  - **[Build, Execution, Deployment] -> [Compiler] -> [Java Compiler]** 에서 Project bytecode version을 앞서 설정한 JDK과 일치시킵니다.

- Gradle JVM 변경

  - 스프링부트 그래들을 사용한다면 추가로 설정을 해야합니다.
  - ![image-20241002095643343](C:\Users\oceanlightai\AppData\Roaming\Typora\typora-user-images\image-20241002095643343.png)

  - **[Build, Execution, Deployment] -> [Build Tools] -> [Gradle]** 에서 Gradle JVM 버전을 앞서 설정한 JDK와 일치시킵니다.



### 마무리 정리

현재까지 Spring프로젝트를 git pull받아

인텔리제이 IDE 환경에서 자바소스코드를 컴파일 할 수 있도록 JDK를 설치, 프로젝트에 연결하였습니다.

이후에는 인텔리제이 IDE환경에서 Mysql DB에 연결하는 법을 정리하겠습니다.



### 참고자료

https://covenant.tistory.com/276
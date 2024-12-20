# 인텔리제이 DB 연결

### 제작배경

2024.10월. 글로컬 청년취업사관학교에서 진행하는 웹 개발 준전문가 양성교육에 멘토로 참여하며, 코칭을 하게 되었습니다.

이전 글에서 인텔리제이로 JDK 설치 및 프로젝트에 연결하는 법까지 정리해보았습니다. 



이번에는, 인텔리제이 환경에서 Mysql DB에 연결하는 방법을 정리해보겠습니다.




### 개념정리

**인텔리제이**

-  JetBrains에서 개발한 통합 개발 환경(IDE)
- 자바(Java) 언어를 위한 강력한 기능을 제공
- 코드 작성, 디버깅, 테스트 등 개발 과정에서 생산성을 높이는 다양한 도구와 기능을 제공
- 자동 완성, 코드 분석, 리팩토링 같은 강력한 코드 편집 기능이 특징



**Mysql**

- 오픈 소스 관계형 데이터베이스 관리 시스템(RDBMS)으로, 데이터를 효율적으로 저장하고 관리하며 다양한 응용 프로그램에서 데이터를 쉽게 조회하고 조작할 수 있도록 설계된 시스템입니다.
- 현재 Oracle Corporation에서 소유하고 있으며, 전 세계적으로 널리 사용되고 있는 데이터베이스 중 하나입니다.



**Jdbc**

- 데이터베이스와 자바 애플리케이션 간의 연결을 관리합니다.

- SQL 쿼리를 실행하며, 결과를 처리하는 역할

- 구성요소

  - JDBC API
    - 데이터베이스 연결, SQL 문 실행, 결과 처리 등의 기능을 제공합니다.

  - JDBC Driver
    - 자바 애플리케이션과 특정 데이터베이스 간의 연결을 가능하게 해주는 소프트웨어입니다.
    - 각 데이터베이스는 JDBC 드라이버를 통해 표준화된 인터페이스로 접근할 수 있습니다.



**Jdbc 주요 클래스 및 인터페이스**

- Deep한 내용이라 설명을 생략하겠습니다.
- Jdbc의 아키텍처?라고 이해하면 될 것 같습니다.



**build.gradle**

- gradle 빌드 시스템을 사용하는 프로젝트에서 빌드 스크립트로 사용되는 파일입니다.

- 대표 구성요소

  - plugins
    - 프로젝트에 사용될 플러그인들을 정의
  - dependency
    - 프로젝트에서 필요한 외부 라이브러리나 모듈을 지정

  - repositories
    - gradle이 의존성을 찾을 위치를 정의
    - 보통 Maven Central, JCenter, 혹은 특정 회사의 사설 리포지토리를 사용

- 예시

  - ```gradle
    # build.gradle
    
    plugins {
        id 'org.springframework.boot' version '2.7.0'
        id 'io.spring.dependency-management' version '1.0.11.RELEASE'
        id 'java'
    }
    
    group = 'com.example'
    version = '0.0.1-SNAPSHOT'
    sourceCompatibility = '11'
    
    repositories {
        mavenCentral()
    }
    
    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-web'
        implementation 'mysql:mysql-connector-java:8.0.32'
    }
    ```






### Mysql 다운로드

https://code-angie.tistory.com/158 참조



### 인텔리제이에서 스프링부트 프로젝트를 Mysql에 연결하기

1. `bulid.gradle dependencies`에 프로젝트가 mysql에 접근할 수 있도록 드라이버 추가

```gradle
dependencies {
    implementation 'mysql:mysql-connector-java'
}
```



2. 데이터베이스 설정 추가

MySQL에 연결할 수 있도록 애플리케이션의 설정 파일에 연결 정보를 추가해야 합니다.

`application.properties`에 다음의 내용을 추가합니다.

```properties
spring.datasource.url=jdbc:mysql://[HOST]:[PORT]/[DATABASE_NAME]?serverTimezone=Asia/Seoul
spring.datasource.username=[USERNAME]
spring.datasource.password=[PASSWORD]
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# JPA 설정 (필요에 따라 설정)
spring.jpa.hibernate.ddl-auto=update
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect
```





### 마무리 정리





### 참고자료

https://covenant.tistory.com/276

https://code-angie.tistory.com/158 
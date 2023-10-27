# 인텔리제이 Lombok 설정

1. build.gradle에 라이브러리 및 환경 추가

```
plugins {
    id 'org.springframework.boot' version '2.3.2.RELEASE'
    id 'io.spring.dependency-management' version '1.0.9.RELEASE'
    id 'java'
}

// lombok 설정    
configurations {
compileOnly {
    extendsFrom annotationProcessor
    }
}

dependencies {
    //...
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    testCompileOnly 'org.projectlombok:lombok'
    testAnnotationProcessor 'org.projectlombok:lombok'
    //...

}

```

2. Preferences(윈도우 File Settings) plugin lombok 검색 설치 실행 (재시작)

3. Preferences Annotation Processors 검색 Enable annotation processing 체크 (재시작)

4. 임의의 테스트 클래스를 만들고 @Getter, @Setter 확인
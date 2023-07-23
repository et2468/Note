# JPA를 쓰며 얻게 되는 이점

### 1️⃣ 생산성 - JPA로 CRUD

C: `jpa.persist(member)`

R: `Member member = jpa.find(memberId)`

U: `member.setName("")`

D: `jpa.remove(member)`

코드가 아주 간결해진다.



### 2️⃣ 유지보수

```java
public class Member {
    private String memberId;
    private String name;
    private String tel;	//추가 필드
 ...
}

INSERT INTO MEMBER(MEMBER_ID, NAME, TEL) VALUES
SELECT MEMBER_ID, NAME, TEL FROM MEMBER M
UPDATE MEMBER SET … TEL = ?
```

SQL중심 개발에서는 tel 필드가 추가된다면 관련된 모든 SQL문에 TEL필드를 추가해주어야 한다.

JPA는 이 과정을 하지 않아도 된다.



### 3️⃣ JPA와 페러다임 불일치

상속, 연관관계, 객체그래프탐색, 객체비교시 와 같은 자바 컬렉션과 RDB의 차이를 해결해주어 RDB를 컬렉션처럼 다룰 수 있게 해준다.



### 4️⃣ 성능

1. 1차 캐시와 동일성 보장

```sql
String memberId = "100";
Member m1 = jpa.find(Member.class, memberId); //SQL
Member m2 = jpa.find(Member.class, memberId); //캐시

println(m1 == m2) //true
```

첫 조회시 SQL문을 날려 데이터를 가져오고, 두번째 조회시 캐시에서 데이터를 가져와 성능을 최적화할 수 있고, 같은 인스턴스를 반환할 수 있다.



2. 쓰기지연

```java
// INSERT
transaction.begin();

em.persist(memberA);
em.persist(memberB);
em.persist(memberC);

transaction.commit();

//UPDATE
transaction.begin();

changeMember(memberA); 
deleteMember(memberB); 
...

transaction.commit(); 
```

트랜잭션을 커밋할 때까지 SQL문을 모아서 보낸다.

- 여러번 DB에 API를 날리지 않아 비용 최적화
- UPDATE, DELETE로 인한 로우락이 생기지 않는다. (아직 잘 이해가 안됨)



3. 지연로딩과 즉시로딩

```java
 Member member = memberDAO.find(memberId);
 Team team = member.getTeam();
 String teamName = team.getName();

//지연로딩
SELECT * FROM MEMBER
SELECT * FROM TEAM
    
//즉시로딩
SELECT M.*, T.* 
FROM MEMBER
JOIN TEAM …
```

지연로딩: 객체가 실제 사용될 때 로딩

즉시로딩: JOIN SQL로 한번에 연관된 객체까지 미리 조회



JPA는 지연로딩과 즉시로딩을 지원하여 JOIN을 적적하게 조절할 수 있다.




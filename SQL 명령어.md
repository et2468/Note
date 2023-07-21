# SQL 명령어

### 1. DDL (Data Definition Language) - 데이터 정의 언어

- CREATE: 객체 생성
- ALTER: DB 객체 변경
- DROP: DB 객체 삭제
- TRUNCATE: 테이블의 모든 데이터 삭제

*객체: DB에서 테이블, 뷰, 인덱스 등을 의미



### 2. DML (Data Manipulation Language) - 데이터 조작 언어

- SELECT: 데이터 조회
- INSERT: 새로운 레코드 삽입
- UPDATE: 기존 레코드 수정
- DELETE: 레코드 삭제





### 3. DCL (Data Control Language) - 데이터 제어 언어

- GRANT: DB에 사용자 권한 부여
- REVOKE: DB에 사용자 권한 취소





### 4. TCL (Transaction control Language) - 트랜잭션 제어 언어

- COMMIT: 트랜젝션을 완료하고 변경 내용을 DB에 반영
- ROLLBACK: 트랜젝션을 취소하고 이전 상태로 되돌림
- SAVEPOINT: 트랜젝션 내에 중간 저장점을 지정





### 5. 조건 및 그룹함수

- WHERE: SELECT문에서 데이터를 필터링
- GROUP BY: 데이터를 그룹화하고 그룹별로 함수를 적용

- HAVING: GROUP BY와 함께 사용하여 그룹화된 결과에 대한 조건 지정



### 6. JOIM

따로 정리



### 7. 서브쿼리

- SELECT문 안에서 사용되는 중첩된 쿼리, 다른쿼리의 결과를 사용하여 데이터를 추출하거나 조작









이외에도 다양한 SQL문이 있으며 DB마다 기능과 문법이 다르다.

SQL문은 ISO/IEC기관에 의해 관리되며 지속적으로 업데이트 된다.
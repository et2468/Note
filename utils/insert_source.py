import os

def insert_source():
    source = """\n
    ### 참고자료\n
    해당 내용은 다음 강의를 참고하여 정리하였습니다. \n
    [실전! 스프링 부트와 JPA 활용1 - 웹 애플리케이션 개발](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8-JPA-%ED%99%9C%EC%9A%A9-1/dashboard)
"""

    for file in os.listdir():
        print(os.path.isfile(file))

        if os.path.isfile(file) and not is_source_in_file(file, source):
            print(file)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(source)
        break

def is_source_in_file(file, source):
    # 파일에 source가 이미 있는지 확인
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        return source in content

if __name__ == "__main__":
    insert_source()
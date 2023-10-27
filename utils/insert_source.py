import os

def insert_source(explain, source_title, source_url, img_url):
    # 참고 자료 정보 설정

    source = generate_source(explain, source_title, source_url, img_url)

    for file in os.listdir():
        # 파일이면서 source가 이미 없는 경우에만 작업 수행
        if os.path.isfile(file) and not is_source_in_file(file, source):
            print(f"{file}에 source 추가")
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 2번째 줄에 source를 추가
            lines.insert(1, source)

            with open(file, 'w', encoding='utf-8') as f:
                f.writelines(lines)

def is_source_in_file(file, source):
    # 파일에 source가 이미 있는지 확인
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        return source in content

def generate_source(explain, source_title, source_url, img_url):
    source = f"""
**참고자료**\n
{explain}\n
![이미지]({img_url})\n
[{source_title}]({source_url})\n
\n
"""
    return source

def check_directory(USER_DIRECTORY):
    
    current_directory = os.getcwd()
    directory_name = os.path.basename(current_directory).strip()

    if USER_DIRECTORY != directory_name:
        raise Exception(f"현재 디렉토리({directory_name})와 파일 이름({USER_DIRECTORY})이 일치하지 않습니다.")
 
if __name__ == "__main__":

    # 해당 디렉토리의 파일들에 출처 정보 삽입
    PLZ_INSERT_EXPLAIN = "해당 내용은 다음 강의를 참고하여 정리하였습니다."
    PLZ_INSERT_SOURCE_TITLE = "자바 ORM 표준 JPA 프로그래밍 - 기본편"
    PLZ_INSERT_SOURCE_URL = "https://www.inflearn.com/course/ORM-JPA-Basic/dashboard"
    PLZ_INSERT_SOURCE_IMG_URL = "https://cdn.inflearn.com/public/courses/324109/course_cover/161476f8-f0b7-4b04-b293-ce648c2ea445/kyh_jsp.png"



    # 현재 디렉토리가 맞는지 확인 (파일이 잘못 입력될 수도 있으니 꼭 확인)
    PLZ_INSERT_DIRECTORY_NAME = "JPA 기본"
    check_directory(PLZ_INSERT_DIRECTORY_NAME)

    
    insert_source(PLZ_INSERT_EXPLAIN, PLZ_INSERT_SOURCE_TITLE, PLZ_INSERT_SOURCE_URL, PLZ_INSERT_SOURCE_IMG_URL)
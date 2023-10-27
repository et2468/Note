import os
import difflib

def delete_source(explain, source_title, source_url, img_url):
    # 참고 자료 정보 설정

    wrong_source = generate_source(explain, source_title, source_url, img_url)

    for file in os.listdir():
        if os.path.isfile(file):
            if is_source_in_file(file, wrong_source):
                print(f"{file}에 wrong_source 삭제")
                with open(file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
            
                new_lines = [line for line in lines if line not in wrong_source]
                with open(file, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
            else:
                with open(file, 'r', encoding='utf-8') as f:
                    whole_text = f.read()
                    check_the_wrong_source(file, wrong_source, whole_text)


def is_source_in_file(file, source):
    # 파일에 wrong_source가  있는지 확인
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        return source in content

def generate_source(explain, source_title, source_url, img_url):
    source = f"""
**참고자료**\n
{explain}\n
![]({img_url})\n
[{source_title}]({source_url})\n
\n
"""
    return source

def check_the_wrong_source(file, wrong_source, whole_text):
    wrong_source = wrong_source.splitlines()
    whole_text = whole_text.splitlines()
    for i in range(len(whole_text)):
        if whole_text[i] == wrong_source[0]:
            start = i
            break
    else:
        print(f"{file}에 잘못된 source의 첫 문장이 없습니다. 문장을 확인하거나 띄어쓰기가 있는지 확인하십시오.")
        return
    # 두 문자열의 첫 번째 라인을 비교한 이후의 라인을 비교
    for i in range(len(wrong_source)):
        if whole_text[start+i] == wrong_source[i]:
            print(f"{i}line 문장은 일치합니다.")
        else:
            print("=======================")
            print(f"{i}line 문장이 잘못되었습니다.")
            print(f"전체 문장의 라인: {whole_text[start+i]}")
            print(f"wrong_sorce 문장의 라인 : {wrong_source[i]}")
            print("=======================")

    # # 라인 수가 다른 경우
    # if len(lines1) != len(lines2):
    #     print("Difference in the number of lines:")
    #     print(f"  String 1 has {len(lines1)} lines")
    #     print(f"  String 2 has {len(lines2)} lines")

def check_directory(USER_DIRECTORY):
    
    current_directory = os.getcwd()
    directory_name = os.path.basename(current_directory).strip()

    if USER_DIRECTORY != directory_name:
        raise Exception(f"현재 디렉토리({directory_name})와 파일 이름({USER_DIRECTORY})이 일치하지 않습니다.")
 
if __name__ == "__main__":

    # 해당 디렉토리의 파일들에 출처 정보 삽입
    PLZ_INSERT_EXPLAIN = "해당 내용은 다음 강의를 참고하여 정리하였습니다. "
    PLZ_INSERT_SOURCE_TITLE = "실전! 스프링 부트와 JPA 활용1 - 웹 애플리케이션 개발"
    PLZ_INSERT_SOURCE_URL = "https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8-JPA-%ED%99%9C%EC%9A%A9-1/dashboard"
    PLZ_INSERT_SOURCE_IMG_URL = "https://cdn.inflearn.com/public/courses/324119/course_cover/07c45106-3cfa-4dd6-93ed-a6449591831c/%E1%84%80%E1%85%B3%E1%84%85%E1%85%AE%E1%86%B8%205%20%E1%84%87%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A1%204.png"



    # 현재 디렉토리가 맞는지 확인 (파일이 잘못 입력될 수도 있으니 꼭 확인)
    PLZ_INSERT_DIRECTORY_NAME = "JPA 기본"
    check_directory(PLZ_INSERT_DIRECTORY_NAME)

    delete_source(PLZ_INSERT_EXPLAIN, PLZ_INSERT_SOURCE_TITLE, PLZ_INSERT_SOURCE_URL, PLZ_INSERT_SOURCE_IMG_URL)
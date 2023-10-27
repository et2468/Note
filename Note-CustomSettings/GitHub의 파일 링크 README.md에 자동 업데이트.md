# GitHub의 파일 링크 README.md에 자동 업데이트

**제작배경**

레파지토리가 많아지며 관리가 어려워, 이들을 통합하기로 하였다.

통합 후 레파지토리 구조가 복잡해졌고, 한눈에 알아보기 쉽게 README.md에 트리형으로 파일링크를 만들기로 하였다.

하나하나 적으며 만들기는 무리일 것 같아 자동화 프로그램을 만들기로 하였다.

아래의 참고자료를 스켈레톤 코드로 직접 만들어 보기로 하였다.



**최종코드와 결과물**

```python
import os
from urllib.parse import quote

def create_readme():
    readme_startline = "# 개발 공부를 기록한 통합 레파지토리입니다.\n\n"
    readme_treeline = generate_readme_treeline("./", 2)
    readme = readme_startline + readme_treeline

    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)

def generate_readme_treeline(directory, depth):
    readme_treeline = ""
    for path in os.listdir(directory):
        full_path = os.path.join(directory, path)
        if os.path.isdir(full_path) and not path.endswith(("img", "git")):
            readme_treeline += f"{'#' * depth} {path}\n"
            readme_treeline += generate_readme_treeline(full_path, depth + 1)
        elif os.path.isfile(full_path):
            file_name = os.path.basename(full_path)
            encoded_file_name = quote(full_path)
            readme_treeline += f"- [{file_name}]({encoded_file_name})\n"
    return readme_treeline

if __name__ == "__main__":
    create_readme()
```













**참고자료**

[[GitHub] 레포지토리의 파일 링크 README.md에 자동 업데이트](https://cherish-my-codes.tistory.com/entry/GitHub-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EC%9D%98-%ED%8C%8C%EC%9D%BC-%EB%A7%81%ED%81%AC-READMEmd%EC%97%90-%EC%9E%90%EB%8F%99-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8)
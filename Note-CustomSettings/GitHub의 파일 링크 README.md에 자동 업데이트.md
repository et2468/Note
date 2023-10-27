# GitHub의 파일 링크 README.md에 자동 업데이트

**제작배경**

레파지토리가 많이 생성되어 관리가 어려워지고, 그로 인해 레파지토리를 통합하기로 결정하였습니다.

통합된 레파지토리의 구조가 복잡하여, 파일 및 디렉토리를 한눈에 알아보기 쉽게 하기 위해 README.md에 트리형 파일 링크를 생성하기로 하였습니다.

각 파일 및 디렉토리를 수동으로 작성하는 것은 현실적으로 어렵기 때문에 자동화 프로그램을 개발하기로 결정하였습니다.

이 작업을 위해 참고 자료를 활용하여 스켈레톤 코드를 직접 커스텀하여 프로그램을 개발하기로 하였습니다.



**최종코드**

```python
import os
from urllib.parse import quote

def create_readme():
    readme_startline = "# 개발 공부를 기록한 통합 레파지토리입니다.\n\n"
    readme_treeline = generate_readme_treeline(".", 2)
    readme = readme_startline + readme_treeline

    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)

def generate_readme_treeline(directory, depth):
    readme_treeline = ""
    for sub in os.listdir(directory):
        full_path = f"{directory}/{sub}"
        if os.path.isdir(full_path) and not sub.endswith(("img", "git")):
            readme_treeline += f"{'#' * depth} {sub}\n"
            readme_treeline += generate_readme_treeline(full_path, depth + 1)
        elif os.path.isfile(full_path):
            encoded_file_name = quote(full_path)
            readme_treeline += f"- [{sub}]({encoded_file_name})\n"
    return readme_treeline

if __name__ == "__main__":
    create_readme()
```



**결과물**

[README.md 자동생성 코드를 적용한 레파지토리 링크](https://github.com/et2468/Note/tree/master#%EA%B0%9C%EB%B0%9C-%EA%B3%B5%EB%B6%80%EB%A5%BC-%EA%B8%B0%EB%A1%9D%ED%95%9C-%ED%86%B5%ED%95%A9-%EB%A0%88%ED%8C%8C%EC%A7%80%ED%86%A0%EB%A6%AC%EC%9E%85%EB%8B%88%EB%8B%A4)



**코드 간략설명**

README.md 파일은 `readme_startline` 및 `readme_treeline` 두 부분으로 구성되며, 이 구조는 저자가 임의로 만든 것입니다.

- `readme_startline`
  - README.md 파일의 제목 부분을 나타냅니다.
  - 이 부분은 단순한 텍스트로 구성되며 별도의 상세 설명이 없습니다.
- `readme_treeline`
  - README.md 파일의 디렉토리 구조를 나타내는 부분입니다.
  - **여기에 핵심 알고리즘이 포함되어 있으며, 나중에 자세히 설명할 예정입니다.**



두 문자열을 합쳐서 README.md 파일을 열고 write 함수를 사용하여 내용을 기록하였습니다.



**핵심 코드설명**

아래는 `readme_treeline`를 생성하는 `generate_readme_treeline()` 재귀 함수의 동작에 대한 요약입니다.



1. 먼저, 루트 디렉토리의 하위 경로를 하나씩 검색합니다.
2. 해당 경로가 디렉토리 또는 파일인지에 따라 조건을 나누어 처리합니다.

3-1. 경로가 디렉토리인 경우:

- 먼저, 다음 디렉토리가 "img" 또는 "git" 디렉토리일 때는 `readme_treeline`에 추가하지 않습니다.
- 디렉토리 깊이에 따라 적절한 수의 "#"와 해당 디렉토리의 이름을 `readme_treeline` 문자열에 추가합니다. 예를 들어, "## Note-JPA"를 `readme_treeline`에 추가하는데, 이는 `readme_treeline += "## Note-JPA\n"`과 같이 될 것입니다.
- 그런 다음, 다음 재귀 함수를 호출하여 다음 하위 디렉토리에서 2번부터 작업을 반복합니다.

3-2. 경로가 파일인 경우:

- 파일의 이름과 상대 경로를 사용하여 Markdown 파일 링크 형식의 문자열인 `- [파일 이름](상대 경로)`를 `readme_treeline` 문자열에 추가합니다.

4. 재귀 호출이 모두 완료되면 최종 파일 트리형의 문자열 `readme_treeline`이 완성됩니다.



**참고사항**

1. GitHub에서는 파일 경로에서 역슬래시(`\`) 대신 슬래시(/)를 사용해야 합니다.
   - 윈도우 환경에서 `full_path  = os.path.join(directory, path)`을 사용하면 경로가 역슬래시로 연결되므로, 이는 GitHub에서 유효한 경로가 아닙니다.
   - 대신 윈도우 환경에서 `full_path = f"{directory}/{sub}"`과 같이 슬래시를 사용해야 합니다.
2. GitHub에서 Markdown 파일의 링크 문법인 `[제목](링크)`에서 링크에 공백이 포함되면 제대로 작동하지 않습니다.
   - 이 문제를 해결하기 위해 링크 형식을 URL 인코딩하여 공백을 `%20`으로 바꿀 수 있습니다.
   - `from urllib.parse import quote` 함수를 사용하여 문자열을 URL로 인코딩할 수 있습니다.
   - 영어 알파벳과 숫자는 일반적으로 URL에서 사용 가능한 문자로 간주되어 `quote` 함수가 이러한 문자를 인코딩하지 않는 것으로 보입니다.



**참고자료**

[[GitHub] 레포지토리의 파일 링크 README.md에 자동 업데이트](https://cherish-my-codes.tistory.com/entry/GitHub-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EC%9D%98-%ED%8C%8C%EC%9D%BC-%EB%A7%81%ED%81%AC-READMEmd%EC%97%90-%EC%9E%90%EB%8F%99-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8)
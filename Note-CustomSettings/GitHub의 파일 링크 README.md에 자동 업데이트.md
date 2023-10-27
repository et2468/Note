# GitHub의 파일 링크 README.md에 자동 업데이트

**제작배경**

레파지토리가 많아지며 관리가 어려워, 이들을 통합하기로 하였다.

통합 후 레파지토리 구조가 복잡해졌고, 한눈에 알아보기 쉽게 README.md에 트리형으로 파일링크를 만들기로 하였다.

하나하나 적으며 만들기는 무리일 것 같아 자동화 프로그램을 만들기로 하였다.

참고자료를 스켈레톤 코드로 직접 커스텀하여 만들어 보기로 하였다.



**최종코드와 결과물**

```python
import os
from urllib.parse import quote

def create_readme(output_file_path="./README.md"):
    readme_startline = "# 개발 공부를 기록한 통합 레파지토리입니다\n\n"
    readme_treeline = generate_readme_treeline(".", 2)
    readme = readme_startline + readme_treeline

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(readme)

def generate_readme_treeline(directory, depth):
    readme_treeline = ""
    for sub in sorted(os.listdir(directory)):
        full_path = f"{directory}/{sub}"
        if os.path.isdir(full_path) and not sub.endswith(("img", "git")):
            readme_treeline += f"{'#' * depth} {sub}\n"
            readme_treeline += generate_readme_treeline(full_path, depth + 1)
        elif os.path.isfile(full_path):
            encoded_file_name = quote(sub)
            readme_treeline += f"- [{sub}]({encoded_file_name})\n"
    return readme_treeline

if __name__ == "__main__":
    create_readme()
```

[README.md 자동생성 코드를 적용한 레파지토리 링크](https://github.com/et2468/Note/tree/master#%EA%B0%9C%EB%B0%9C-%EA%B3%B5%EB%B6%80%EB%A5%BC-%EA%B8%B0%EB%A1%9D%ED%95%9C-%ED%86%B5%ED%95%A9-%EB%A0%88%ED%8C%8C%EC%A7%80%ED%86%A0%EB%A6%AC%EC%9E%85%EB%8B%88%EB%8B%A4)



**코드 간략설명**

우선 README.md 파일은 `readme_startline`과 `readme_treeline`으로 나뉜다. (이 구조는 필자가 임의로 만든 구조)

- `readme_startline`
  - README.md의 제목부분이다.
  - 단순한 텍스트로 별도로 설명할 것은 없다.
- `readme_treeline`
  - README.md의 디렉토리 구조를 나타내는 부분이다.
  - **이곳에 핵심 알고리즘이 있으며 뒤에 자세히 설명하겠다.**



두 문자열을 합친 문자열을 README.md를 열어 write 해주었다.



**핵심 코드설명**

`readme_treeline`는 README.md에서 디렉토리 구조를 트리형식으로 작성한 텍스트 문자열이다.

이를 생성하기 위한 `generate_readme_treeline()` 재귀함수에 대해 설명하겠다.



1. 우선 root directory의 하위 path를 하나씩 조회한다.

2. 해당 path가 directory냐 file이냐에 따라 조건 분기를 나누어 처리한다.

3-1. path가 directory일 때

- 우선 다음 directory가 `img파일`이거나 `git파일`일 때는 `readme_treeline`에 작성하지 않는다.
- `"#" x 다음 directory 깊이` + `해당 directory 이름`을 `readme_treeline` 문자열에 추가한다.
  - ex.) `"##` `Note-JPA"`을 `readme_treeline`에 추가 
  - `readme_treeline += "## Note-JPA\n"`
- 문자열에 추가한 이후에 다음 재귀함수로 2번부터 다시 시작한다.

3-2. path가 file일 때

- `- [file 이름](file 상대경로)`, 즉 md파일의 링크연결 문법 형식 문자열을 `readme_treeline` 문자열에 추가한다.

4. 재귀가 마무리 되면 파일트리가 완성된다.



**참고사항**

1. Github에서는 경로에서 `\`를 인식하지 못하므로 `/`를 사용해주어야한다.

- 윈도우에서 `full_path = os.path.join(directory, path)`을 사용하면 두 문자열이 `\`로 합쳐지므로 원격저장소에서 링크를 클릭하면 404페이지가 뜬다.

- 윈도우에선 `full_path = f"{directory}/{sub}"`으로 작성해 주어야한다.



2. Github에선 md파일의 링크문법 `[제목](링크)`에 링크에 띄워쓰기가 있으면 작동하지 않는다.

- 이를 위해 링크형식을 



**참고자료**

[[GitHub] 레포지토리의 파일 링크 README.md에 자동 업데이트](https://cherish-my-codes.tistory.com/entry/GitHub-%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EC%9D%98-%ED%8C%8C%EC%9D%BC-%EB%A7%81%ED%81%AC-READMEmd%EC%97%90-%EC%9E%90%EB%8F%99-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8)
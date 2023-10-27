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
            file_name = os.path.basename(full_path)
            encoded_file_name = quote(full_path)
            readme_treeline += f"- [{file_name}]({encoded_file_name})\n"
    return readme_treeline

if __name__ == "__main__":
    create_readme()
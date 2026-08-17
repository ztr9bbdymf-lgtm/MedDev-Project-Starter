"""MedDev-Project-Starter v0.1：创建医疗器械研发项目基础目录。"""

from datetime import datetime
from pathlib import Path

PROJECT_DIRECTORIES = [
    "01_项目立项", "02_设计输入", "03_技术资料", "04_设计开发",
    "05_测试验证", "06_供应商资料", "07_AI分析", "08_项目记录",
]
INVALID_NAME_CHARACTERS = '<>:"/\\|?*'


def is_valid_project_name(name: str) -> bool:
    """检查项目名称是否适合作为 Windows 文件夹名称。"""
    if not name or not name.strip() or any(c in name for c in INVALID_NAME_CHARACTERS):
        return False
    if name[-1] in {" ", "."}:
        return False
    return name.upper() not in {"CON", "PRN", "AUX", "NUL"} and not (
        name.upper().startswith(("COM", "LPT")) and name[3:].isdigit()
    )


def create_project(project_name: str, parent_directory: Path | None = None) -> Path | None:
    """创建项目目录，成功返回项目路径；失败返回 None。"""
    project_name = project_name.strip()
    if not is_valid_project_name(project_name):
        print("项目名称为空或包含 Windows 不允许的字符，未创建项目。")
        return None

    project_directory = (parent_directory or Path.cwd()) / project_name
    if project_directory.exists():
        print(f"目标文件夹已存在，未覆盖任何内容：{project_directory}")
        return None

    try:
        project_directory.mkdir()
        for directory_name in PROJECT_DIRECTORIES:
            (project_directory / directory_name).mkdir()
        created_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
        readme = f"""# {project_name}

## 项目名称

{project_name}

## 创建时间

{created_time}

## 项目目录说明

- `01_项目立项`：项目立项相关资料
- `02_设计输入`：设计输入及需求资料
- `03_技术资料`：产品和技术参考资料
- `04_设计开发`：设计开发过程资料
- `05_测试验证`：测试、验证及确认资料
- `06_供应商资料`：供应商相关资料
- `07_AI分析`：AI 辅助分析资料
- `08_项目记录`：会议、沟通及其他项目记录

本目录由 MedDev-Project-Starter 自动生成。
"""
        (project_directory / "README.md").write_text(readme, encoding="utf-8")
    except OSError as error:
        print(f"创建项目失败：{error}")
        return None
    print(f"项目创建成功：{project_directory}")
    return project_directory


def main() -> None:
    print("MedDev-Project-Starter v0.1")
    create_project(input("请输入项目名称："))


if __name__ == "__main__":
    main()

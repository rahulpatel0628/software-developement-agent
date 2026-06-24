from pathlib import Path


def create_directory(directory_path: str) -> None:
    Path(directory_path).mkdir(parents=True,exist_ok=True)


def write_file(file_path: str,content: str) -> str:
    path = Path(file_path)
    path.parent.mkdir(parents=True,exist_ok=True)

    with open(path,"w",encoding="utf-8") as f:
        f.write(content)

    return str(path)


def read_file(file_path: str) -> str:

    with open(file_path,"r",encoding="utf-8") as f:
        return f.read()

def read_directory(directory_path: str) -> dict:
    files = {}

    for file in Path(directory_path).rglob("*.py"):

        with open(file,"r",encoding="utf-8") as f:
            files[str(file)] = f.read()

    return files

def update_file(file_path: str,content: str) -> None:

    with open(file_path,"w",encoding="utf-8") as f:
        f.write(content)



def readfile(path: str) -> str:
    with open(path, "r") as file:
        content = file.read()
        return content
        
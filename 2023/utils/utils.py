def readfile(path: str) -> str:
    with open(path, "r") as file:
        content = file.read()
        return content


def is_eq[T](a: T, b: T) -> bool:
    if a != b:
        print(f"{a} is not equal to {b}")
    return a == b

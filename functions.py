FILEPATH = "todos_file.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as f:
        content = f.readlines()
        return content


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as f:
        f.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")

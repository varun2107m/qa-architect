import os


def write_file(path, content):

    parent = os.path.dirname(path)

    if parent:
        os.makedirs(
            parent,
            exist_ok=True
        )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)
        
        

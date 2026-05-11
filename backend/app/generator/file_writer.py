import os


def write_file(
    path,
    content
):

    parent_dir = os.path.dirname(path)

    if parent_dir:

        os.makedirs(
            parent_dir,
            exist_ok=True
        )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)
        

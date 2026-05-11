import os


def create_folder_structure(
    base_path,
    folders
):

    for folder in folders:

        folder_path = os.path.join(
            base_path,
            folder
        )

        os.makedirs(
            folder_path,
            exist_ok=True
        )
        
        

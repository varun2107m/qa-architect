import os
import zipfile
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/download-framework")
def download_framework(path: str):

    zip_path = f"{path}.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf:

        for root, dirs, files in os.walk(path):

            for file in files:

                file_path = os.path.join(root, file)

                arcname = os.path.relpath(file_path, path)

                zipf.write(file_path, arcname)

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="qa-framework.zip"
    )

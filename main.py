from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from pathlib import *
import uuid
import sys
import os

sys.path.append('..')

app = FastAPI()
dir = Path(__file__).parent / 'photoHolder'
 
 
@app.post("/")
def read_root(file: UploadFile):
    try:
        fileName = f'{uuid.uuid4()}_{file.filename}'
        new_file = open(Path(dir / fileName),'wb')
        new_file.write(file.file.read())
        new_file.close()
        fileDir = Path(dir / fileName)

        return "successful"

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/files")
def file_contents(files: List[UploadFile]):
    try:
        for file in files:
            fileName = f'{uuid.uuid4()}_{file.filename}'
            new_file = open(Path(dir / fileName),'wb')
            new_file.write(file.file.read())
            new_file.close()

        return parse_directory('/workspaces/dartar/innoglobalchack-2023/photoHolder')
        return 'successful'
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

def parse_directory(directory_path):
    file_links = []
    
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory_path):
        print(f"Директория '{directory_path}' не существует.")
        return file_links

    # Перебираем файлы в директории
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Создаем полный путь к файлу
            file_path = os.path.join(root, file)
            # Добавляем ссылку на файл в массив
            file_links.append(file_path)
    
    return file_links


from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pathlib import *
import uuid
import sys
import os

sys.path.append('..')

app = FastAPI()
dir = Path(__file__).parent.parent / 'core' / 'outputData'
 
 
@app.post("/")
def read_root(file: UploadFile):
    try:
        if file.filename.split('.')[1] !='dat':
            raise Exception('wrong type of file')
        fileName = f'{uuid.uuid4()}_{file.filename}'
        new_file = open(Path(dir / fileName),'wb')
        new_file.write(file.file.read())
        new_file.close()
        fileDir = Path(dir / fileName)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
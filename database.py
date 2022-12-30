import os
from deta import Deta
from dotenv import load_dotenv

# initialisation database DETA_KEY
load_dotenv(".env")  # la DETA_KEY est cache
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)


def get_file_drive(name_drive, file_):
    d = deta.Drive(name_drive)
    get_d = d.get(f"{file_}")
    content = get_d.read()
    get_d.close()
    return content


def put_file_drive(name_drive, file_, path_local):
    d = deta.Drive(name_drive)
    d.put(f"{file_}", path=f"{path_local}/{file_}")


def delete_file_drive(name_drive, file_):
    d = deta.Drive(name_drive)
    d.delete(f"{file_}")


def list_files(name_drive):
    d = deta.Drive(name_drive)
    return d.list().get('names')

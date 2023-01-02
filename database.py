import os
import sys
from deta import Deta
from dotenv import load_dotenv
import pickle
import streamlit_authenticator as stauth

# initialisation database DETA_KEY
load_dotenv(".env")  # la DETA_KEY est cache
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
drive = deta.Drive("simple_drive")
create_avatar_drive = False

db = deta.Base("ga144_db")  # users database

path_image = 'avatar/png/'  # avatar/png local
path_avatar_drive = 'avatar'  # fichiers stocke avatar/001.png
list_avatar = os.listdir(path_image)  # list png local

avatar_drive = deta.Drive(path_avatar_drive)  # avatar Drive

if create_avatar_drive:  # creation et stockage des fichiers avatar/png
    # copie des fichiers /avatar vers drive
    for l in list_avatar:
        print(l)
        avatar_drive.put(l, path=path_image + l)  # file to send, path= local source


# generation hashed_passwords et sauvegrde dans le fichier hashed_pwd.plk
def generate_hashed_passwords(name, username, password_):
    hashed_passwords = stauth.Hasher(password_).generate()

    # print(f"generation password :{hashed_passwords}")
    # ecriture du fichier passwords
    # print("ecriture fichier :")
    with open('hashed_pwd.plk', 'wb') as f:
        pickle.dump(name, f)
        pickle.dump(username, f)
        pickle.dump(hashed_passwords, f)
        f.close()


def read_hashed_passwords(file_):
    # lecture fichier hashed_pwd.plk
    with open(file_, 'rb') as f:
        name_ = pickle.load(f)
        username_ = pickle.load(f)
        password_ = pickle.load(f)
        f.close()
        return name_, username_, password_


def readfile(filename):
    with open(filename) as f:
        content = f.readlines()
        return content


def put_database(dict_):
    db.put(dict_)


def fetch_all(db):
    res = db.fetch(db)
    return res.items


def get_database(database_, key_):
    return database_.get(key_)


def fetch_projet(database_ , query_):
    res = database_.fetch(query_)
    return res.items
def update_database(database_, update_values_, key_):
    d = get_database(database_, key_) # lecture {}
    d.update(update_values_) # update {}
    database_.put(d)



a = fetch_projet(db, {"name_project": 'led', "name": 'toto'} )
sys.exit()

name_ = 'Emmanuel'
a = get_database(db,  '1')
print(a)
update_database(db, {'name' : name_} , '1')
sys.exit()

def delete_database(database_, query_):
    fetch_res = database_.fetch(query_)
    for item in fetch_res.items:
        db.delete(item["key"])



# delete_database(db, {"name": "Emmanuel"})


def get_code(getname_node, db):
    return db.get(getname_node)['code']


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

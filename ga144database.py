import os
import sys
import glob
from deta import Deta
from dotenv import load_dotenv

# initialisation database DETA_KEY
load_dotenv(".env")  # la DETA_KEY est cache
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)


def readfile(filename):
    with open(filename) as f:
        content = f.readlines()
        return content


# datas nom du projet , qui corrrespond au nom du repertoire
name_project = 'ledpulse'

# fichiers dans repertoire name_project
# listdir = glob.glob(f"{name_project}/*.node")
listdir = os.listdir(name_project)  # list les noms des fichiers dans le repertoire name_project
print(listdir)

# generation dictionnaire node : code
dictnodes = {}
for l in listdir:
    dictnodes.update({l: readfile(f"{name_project}/{l}")})  # {node : code}
print(dictnodes)

db = deta.Base("ga144_db")


def insert_database(node, code, name_project):
    return db.put({'key': node, 'name_node': node, 'code': code, 'name_project': name_project})


def values_to_database(dictnodes_):
    # insert node code name_project in  database
    for key, value in dictnodes_.items():
        insert_database(key, "".join(value), name_project)


def fetch_all():
    res = db.fetch()
    return res.items


def fetch_projet(projet_, node_):
    res = db.fetch({"name_project": 'ledpulse', "name_node?contains": node_})
    return res.items


def get_code(getname_node):
    return db.get(getname_node)['code']


node = '500.node'
projet = 'ledpulse'

# values_to_database(dictnodes)


print("fetch all: ", fetch_all())
print(f"code: {node}\n", get_code(node))  # code du node en parametre
print(f"select: {projet}", fetch_projet(projet, '.node'))

nodes = fetch_projet(projet, '.node')  # liste de dictionnaire
for l in nodes:
    print(l["key"], "\n", l["code"])

'''
# file_in_lib = glob.glob(f"lib/*.ga") # list fichiers dans /lib
file_in_lib = os.listdir("lib") # list fichiers dans /lib
print(file_in_lib)

# creation et copie fichiers /lib
drive = deta.Drive("simple_drive")
lib = deta.Drive('lib')
# copie des fichiers /lib vers drive
for l in file_in_lib:
    print(l, 'lib/'+l)
    lib.put(l, path='lib/'+l) # file to send, path= local source

# list des fichiers sur drive
result = lib.list()
all_files = result.get("names")
print(result)
'''


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


print(get_file_drive("lib", "delay.ga"))

file = 'logic.ga'
path_destination = 'lib'
path_local = 'lib'
print(f"put the file {file}")
put_file_drive(path_destination, file, path_local)  # path destination et pathlocal ont le meme nom

file = 'gpio.ga'
path_destination = "lib"
print(f"delete file  {file}")
delete_file_drive(path_destination, file)

print(f"list  {path_destination}  : {list_files(path_destination)}")

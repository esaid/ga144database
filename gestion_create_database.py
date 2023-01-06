import database
import os

# --------------------------------------------------
#  avatar png
path_avatar_local = 'avatar/png/'  # avatar/png Local
create_avatar_drive = False
# --------------------------------------------------

# --------------------------------------------------
# generation hashed passwords
# Authentification
name = ["admin", "emmanuel said"]
username = ["admin", "esaid"]
passwords = ["1234", "1234"]  # 1234  1234


file_hashed_passwords = 'hashed_pwd.plk'
create_hashed_passwords = False
# --------------------------------------------------

# --------------------------------------------------
# lib

path_lib_local = 'lib/'  # fichiers dans /lib Local
create_lib_drive = False
# --------------------------------------------------

# --------------------------------------------------
# users database
creation_user = False

# project database
creation_project = False
# --------------------------------------------------

if create_hashed_passwords:
    # generation fichier si ajout ou modification mot de passe
    database.generate_hashed_passwords(name, username, passwords, file_hashed_passwords)

# creation fichiers png avatar vers Drive
if create_avatar_drive:  # creation et stockage des fichiers avatar/png
    list_avatar = os.listdir(path_avatar_local)  # list png local
    # copie des fichiers /avatar vers drive
    for l in list_avatar:
        print(l)
        database.put_file_drive(database.avatar_drive, l, path_avatar_local)  # file to send from path_avatar_local

if create_lib_drive:
    # file_in_lib = glob.glob(f"lib/*.ga") # list fichiers dans /lib
    file_in_lib = os.listdir(path_lib_local)  # list fichiers dans /lib Local
    # print(file_in_lib)
    # copie des fichiers /lib vers drive
    for l in file_in_lib:
        database.put_file_drive(database.lib_drive, l, path_lib_local)  # file to send from path_lib_local

if creation_user:
    # generation dictionnaire user
    dict_db_user = {
        'surname': 'Emmanuel',
        'name': 'SAID',
        'username': "esaid",
        'email': "emmanuel.said@gmail.com",
        'avatar': '003.png',
        'key': '1'
    }
    database.put_database(database.db_user, dict_db_user)  # ecriture dans datatbase user

if creation_project:
    # generation dictionnaire projet
    dict_db_project = {
        'username': "esaid",
        'name_project': 'ledpulse',
        'public': True,
        'comment': " ",
        'key': '1'
    }
    name_project_folder = f"{dict_db_project['username']}_{dict_db_project['name_project']}"  # concatenation user_name_project
    database.put_database(database.db_project, dict_db_project)  # ecriture dans datatbase project

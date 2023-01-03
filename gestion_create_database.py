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

path_lib_local = 'lib'  # fichiers dans /lib Local
create_lib_drive = False
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
        database.avatar_drive.put(l, path=database.path_avatar_drive + l)  # file to send, path= local source

if create_lib_drive:
    # file_in_lib = glob.glob(f"lib/*.ga") # list fichiers dans /lib
    file_in_lib = os.listdir(path_lib_local)  # list fichiers dans /lib Local
    # print(file_in_lib)
    # copie des fichiers /lib vers drive
    for l in file_in_lib:
        database.lib_drive.put(l, path=database.path_lib_destination + l)  # file to send, path_lib_destination

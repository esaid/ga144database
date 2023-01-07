import os
import sys
from deta import Deta
from dotenv import load_dotenv  # python-dotenv
import pickle
import streamlit_authenticator as stauth

# --------------------------------------------------
# initialisation database DETA_KEY
load_dotenv(".env")  # la DETA_KEY est cache
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
drive = deta.Drive("simple_drive")
# --------------------------------------------------

# --------------------------------------------------
# initialisation Base et Drive
# Base pour user , project , lien commun username
db_user = deta.Base('user')  # users database
db_project = deta.Base('project')  # project database
# Drive pour avatar , lib, project_name ( concatenation username_name_project )

path_avatar_drive = 'avatar'  # fichiers stocke avatar/001.png
avatar_drive = deta.Drive(path_avatar_drive)  # avatar/ Drive
path_lib_drive = 'lib'
lib_drive = deta.Drive(path_lib_drive)  # lib/ Drive


# --------------------------------------------------
def autentificator_list_dict(list_usernames_, list_email_, list_name_, list_passwords_, list_emails_prehautorized_,
                             list_value_cookies_):
    list_user = ["email", "name", "password"]
    list_cookies = ["expiry_days", "key", "name"]
    list_value_prehautorized = {"emails": list_emails_prehautorized_}

    # generation user list
    l_user_values = []
    for n in range(len(list_user) - 1):
        l_user_values.append([list_email_[n], list_name_[n], list_passwords_[n]])

    # list to dict
    credentials = {}
    usernames = {}
    cookie = {'cookie': dict(zip(list_cookies, list_value_cookies_))}
    prehautorized = {'preauthorized': list_value_prehautorized}

    user_values = {}
    for n in range(len(list_usernames_)):
        usernames[list_usernames_[n]] = dict(zip(list_user, l_user_values[n]))

    usernames = {'usernames': usernames}
    config = {'credentials': usernames, **cookie, **prehautorized}  # merge dict
    return config


# generation hashed_passwords et sauvegrde dans le fichier file_
def generate_hashed_passwords(name, username, password_, file_):
    hashed_passwords = stauth.Hasher(password_).generate()
    print(f"generation password :{hashed_passwords}")
    # ecriture du fichier passwords
    # print("ecriture fichier :")
    with open(file_, 'wb') as f:
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


def put_database(database_, dict_):
    database_.put(dict_)


def fetch_all(database_):
    res = database_.fetch()
    return res.items


def get_database(database_, key_):
    return database_.get(key_)


def filter_database(database_items_ , key_):
    l_ = []
    for l in database_items_:
        l_.append(l[key_])
    return l_

    return res.items


def fetch_projet(database_, query_):  # fetch_projet(db_user, {"name_project": 'led', "name": 'toto'} )
    res = database_.fetch(query_)
    return res.items


def update_database(database_, update_values_, key_):
    d = get_database(database_, key_)  # lecture {}
    d.update(update_values_)  # update {}
    database_.put(d)


# a = fetch_projet(db_user, {"name_project": 'led', "name": 'toto'})
# sys.exit()

# name_ = 'Emmanuel'
# a = get_database(db_user, '1')
# print(a)
# update_database(db_user, {'name': name_}, '1')
# sys.exit()


def delete_database(database_, query_):  # delete_database(db_user, {"name": "Emmanuel"})
    fetch_res = database_.fetch(query_)
    for item in fetch_res.items:
        db_user.delete(item["key"])


# delete_database(db_user, {"name": "Emmanuel"})


def get_code(getname_node, db):
    return db.get(getname_node)['code']


def get_file_drive(drive_, file_):
    get_d = drive_.get(f"{file_}")
    content = get_d.read()
    get_d.close()
    return content


def put_file_drive(drive_, file_, path_local):
    drive_.put(f"{file_}", path=f"{path_local}{file_}")


def delete_file_drive(drive_, file_):
    drive_.delete(f"{file_}")


def list_files(drive_):
    return drive_.list().get('names')

import os
import sys
import glob
from deta import Deta
from dotenv import load_dotenv
import database
import streamlit as st
import streamlit_authenticator as stauth

# generation dictionnaire user
dict_db_user = {
    'surname': 'Emmanuel',
    'name': 'SAID',
    'username': "esaid",
    'avatar': '003.png',
    'key': 1
}

# generation dictionnaire projet
dict_db_project = {
    'username': "esaid",
    'name_project': 'ledpulse',
    'public': True,
    'comment': " ",
    'key': 1
}

name_project_folder = f"{dict_db_project['username']}_{dict_db_project['name_project']}"  # concatenation user_name_project

database.put_database(dict_db_user)  # ecriture dans datatbase user
database.put_database(dict_db_project)  # ecriture dans datatbase project
# sys.exit()

path_avatar_drive = 'avatar'
if "avatar" not in st.session_state:
    avatar = ''

# read hashed passwords name , username
name, username, hashed_passwords = database.read_hashed_passwords('hashed_pwd.plk')
# print(f"lecture fichier et decodage {hashed_passwords}")
authenticator = stauth.Authenticate(name, username, hashed_passwords, 'some_cookie_name', 'some_signature_key',
                                    cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('GA144', 'main')
placeholder = st.empty()

with placeholder.container():
    st.session_state["avatar"] = st.selectbox("my avatar 👇", database.list_files(database.path_avatar_drive))
    st.image(database.get_file_drive(path_avatar_drive, st.session_state["avatar"]), width=70)

if authentication_status:
    placeholder.empty()  # status ok, clear st.image(avatar)
    st.write(f'Welcome *{name}*')
    st.image(database.get_file_drive(database.path_avatar_drive, st.session_state["avatar"]), width=70)
    authenticator.logout('Logout', 'main')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

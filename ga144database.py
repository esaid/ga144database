import os
import sys

import yaml
from yaml import SafeLoader

import database
import streamlit as st
import streamlit_authenticator as stauth

path_avatar_drive = 'avatar'
if "avatar" not in st.session_state:
    avatar = ''

# read hashed passwords name , username
name, username, hashed_passwords = database.read_hashed_passwords('hashed_pwd.plk')
# print(f"lecture fichier et decodage {hashed_passwords}")
# authenticator = stauth.Authenticate(name, username, hashed_passwords, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

#authenticator = stauth.Authenticate(
   # config['credentials'],
   # config['cookie']['name'],
   # config['cookie']['key'],
   # config['cookie']['expiry_days'],
   # config['preauthorized']
#)
authenticator = stauth.Authenticate(name, username , hashed_passwords ,  'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('GA144', 'main')

placeholder = st.empty()

with placeholder.container():
    st.session_state["avatar"] = st.selectbox("my avatar 👇", database.list_files(database.avatar_drive))
    st.image(database.get_file_drive(database.avatar_drive, st.session_state["avatar"]), width=70)

if authentication_status:
    placeholder.empty()  # status ok, clear st.image(avatar)
    st.write(f'Welcome *{name}*')
    st.image(database.get_file_drive(database.avatar_drive, st.session_state["avatar"]), width=70)
    authenticator.logout('Logout', 'main')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

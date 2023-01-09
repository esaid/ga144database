import os
import sys

import yaml
from yaml import SafeLoader
import json
import database
import streamlit as st
import streamlit_authenticator as stauth

path_avatar_drive = 'avatar'
if "avatar" not in st.session_state:
    avatar = ''
# read datas from user.database
d = database.fetch_all(database.db_user)  # all items user databse
next_key = database.next_key(d)

list_usernames = database.filter_database(d, "username")  # all values username
list_name = database.filter_database(d, "name")  # all values name
list_email = database.filter_database(d, "email")  # all values email
list_passwords = database.filter_database(d, "password")  # values password
list_emails_prehautorized = ["emmanuel.said@gmail.com"]
list_value_cookies = [30, "random_signature_key", "random_cookie_name"]
# read list_passwords ( hashed values)
# list_name, list_usernames, list_passwords = database.read_hashed_passwords('hashed_pwd.plk')

config = database.autentificator_list_dict(list_usernames, list_email, list_name, list_passwords,
                                           list_emails_prehautorized, list_value_cookies)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


try:
    st.session_state["avatar"] = st.selectbox("my avatar 👇", database.list_files(database.avatar_drive))
    st.image(database.get_file_drive(database.avatar_drive, st.session_state["avatar"]), width=70)

    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
        # st.write(config) # recueration des valeurs register_user
        last_username = list(config['credentials']['usernames'])[-1]
        last_name = config['credentials']['usernames'][last_username]['name']
        last_email = config['credentials']['usernames'][last_username]['email']
        last_password = config['credentials']['usernames'][last_username]['password']
        dict_db_user = {
            'name': last_name,
            'username': last_username,
            'email': last_email,
            'avatar':  st.session_state["avatar"],
            'password': last_password,
            'key': str(next_key)
        }
        st.write(dict_db_user)
        st.write(last_username,last_name , last_email, last_password)
        database.put_database(database.db_user, dict_db_user)  # ecriture dans datatbase user

except Exception as e:
    st.error(e)


name, authentication_status, username = authenticator.login('GA144', 'main')

placeholder = st.empty()

with placeholder.container():
    if authentication_status:
        placeholder.empty()  # status ok, clear st.image(avatar)
        st.write(f'Welcome *{name}*')
        st.image(database.get_file_drive(database.avatar_drive, st.session_state["avatar"]), width=70)
        authenticator.logout('Logout', 'main')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')

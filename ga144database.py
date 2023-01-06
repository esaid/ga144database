import os
import sys

import yaml
from yaml import SafeLoader

# import database
import streamlit as st
import streamlit_authenticator as stauth

import database

path_avatar_drive = 'avatar'
if "avatar" not in st.session_state:
    avatar = ''

# generation hashed passwords
# Authentification


list_value_cookies = [30, 'random_signature_key', 'random_cookie_name']
list_usernames = ["admin", "esaid"]
list_email = ['admin@gmail.com', 'toto@gmail.com']
list_name = ["admin", "emmanuel said"]
list_passwords = ["1234", "1234"]  # 1234  1234
list_emails_prehautorized = ['admin@gmail.com']

list_user = ['email', 'name', 'password']
list_cookies = ['expiry_days', 'key', 'name']
list_value_prehautorized = {'emails': list_emails_prehautorized}

# generation user list
l_user_values = []
for n in range ( len ( list_user ) - 1 ):
    l_user_values.append ( [list_email[n], list_name[n], list_passwords[n]] )

# list to dict
credentials = {}
usernames = {}
cookie = {'cookie': dict ( zip ( list_cookies, list_value_cookies ) )}
prehautorized = {'preauthorized': list_value_prehautorized}

user_values = {}
for n in range ( len ( list_usernames ) ):
    usernames[list_usernames[n]] = dict ( zip ( list_user, l_user_values[n] ) )

usernames = {'usernames': usernames}
config = {'credentials': usernames, **cookie, **prehautorized} # merge dict


# read hashed passwords name , username
# name, username, hashed_passwords = database.read_hashed_passwords ( 'hashed_pwd.plk' )
# print(f"lecture fichier et decodage {hashed_passwords}")
# authenticator = stauth.Authenticate(name, username, hashed_passwords, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

# with open ( 'config.yaml' ) as file:
#    config = yaml.load ( file, Loader=SafeLoader )

c = config['credentials']
cn = config['cookie']['name']
ck = config['cookie']['key']
ced = config['cookie']['expiry_days']
cp = config['preauthorized']

authenticator = stauth.Authenticate (
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
# authenticator = stauth.Authenticate ( list_name, list_usernames, hashed_passwords, 'some_cookie_name',
# 'some_signature_key',cookie_expiry_days=30 )
st.write("Hello")
name, authentication_status, username = authenticator.login ( 'GA144', 'main' )
st.stop()
sys.exit()
placeholder = st.empty ()

with placeholder.container ():
    st.session_state["avatar"] = st.selectbox ( "my avatar 👇", database.list_files ( database.avatar_drive ) )
    st.image ( database.get_file_drive ( database.avatar_drive, st.session_state["avatar"] ), width=70 )

if authentication_status:
    placeholder.empty ()  # status ok, clear st.image(avatar)
    st.write ( f'Welcome *{name}*' )
    st.image ( database.get_file_drive ( database.avatar_drive, st.session_state["avatar"] ), width=70 )
    authenticator.logout ( 'Logout', 'main' )
elif authentication_status == False:
    st.error ( 'Username/password is incorrect' )
elif authentication_status is None:
    st.warning ( 'Please enter your username and password' )

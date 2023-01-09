
def autentificator_list_dict(list_usernames_, list_email_, list_name_, list_passwords_, list_emails_prehautorized_, list_value_cookies_):
    list_user = ['email', 'name', 'password']
    list_cookies = ['expiry_days', 'key', 'name']
    list_value_prehautorized = {'emails': list_emails_prehautorized_}

    # generation user list
    l_user_values = []
    for n in range ( len ( list_user ) - 1 ):
        l_user_values.append ( [list_email_[n], list_name_[n], list_passwords_[n]] )

    # list to dict
    credentials = {}
    usernames = {}
    cookie = {'cookie': dict ( zip ( list_cookies, list_value_cookies_ ) )}
    prehautorized = {'preauthorized': list_value_prehautorized}

    user_values = {}
    for n in range ( len ( list_usernames_ ) ):
        usernames[list_usernames_[n]] = dict ( zip ( list_user, l_user_values[n] ) )

    usernames = {'usernames': usernames}
    config = {'credentials': usernames, **cookie, **prehautorized}  # merge dict
    return config

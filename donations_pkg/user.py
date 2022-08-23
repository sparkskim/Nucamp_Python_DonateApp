"""
Workshop 3 - Donation Applet
By Sung Kim
Date 8/20/2022
"""


def login(database, username, password):
    """
    function that logins users with existing credentials
    """
    if username in database and database[username] == password:
        print("\n" + "Welcome back", username + "!")
        return username
    elif username in database and database[username] != password:
        print("\n" + "Password doesn't match the username.")
        return ""
    else:
        print("\n" + "Username not found. Please register.")
        return ""


def register(database, username, password):
    """
    function that registers new users
    """
    while True:
        username = username.casefold()
        if username in database:
            print("Username already registered.")
            return ""
        elif len(username) > 10:
            print("Username must be less than 10 letters. Please enter username again.")
            return ""
        elif len(password) < 5:
            print("Password must be at least 5 numbers. Please enter password again.")
            return ""
        else:
            print(username, "has been registered.")
            return username

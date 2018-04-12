import json


def get_stored_username():
    '''如果储存了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    '''提示用户输入用户名'''
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    '''问候用户'''
    username = get_new_username()
    if username:
        confirm_username(username)
    else:
        username = get_new_username()
        print("we'll remember you when you come back, " + username + "!")


def confirm_username(username):
    '''确认用户名是否正确'''
    confirm = input("%s: It's your name?[y/n]" % username)
    if confirm == 'y':
        print("welcome back, " + username + "!")
    elif confirm == 'n':
        greet_user()
    else:
        print("input Error")
        return confirm_username(username)


greet_user()

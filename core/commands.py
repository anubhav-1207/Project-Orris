def user_show():
    with open ('authentication/user.orr','r') as f:
        user = f.read()
        print(f'Logged in as {user}')


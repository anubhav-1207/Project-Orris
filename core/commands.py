import os

def user_show():
    with open ('authentication/user.orr','r') as f:
        user = f.read()
        print(f'Logged in as {user}')

def mkdir(dir_name):
    os.mkdir(f'system/{dir_name}')

def init(file_namepath):
    try:
        with open(f'system/{file_namepath}','w') as f:
            f.close()

    except FileExistsError:
        print(f'Error: File {file_namepath} already exists')

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except IsADirectoryError:
        print(f"Error: {file_namepath} is a directory")

def rid(file_namepath):
    try:
        os.remove(f'system/{file_namepath}')
    except FileNotFoundError:
        print("Error: No Such File Or Directory")
    
def enter(file_namepath,content):
    try:
        with open (f'system/{file_namepath}','a') as f:
            f.write(content+'\n')
    except:
        pass


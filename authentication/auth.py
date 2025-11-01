from cryptography.fernet import Fernet
from process.boot_manager import boot_manager

key_file = 'authentication/key.key'
password_file = 'authentication/pass.orr'
username_file = 'authentication/user.orr'

# --- Key handling ---
try:
    with open(key_file, 'rb') as f:
        key = f.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)

fernet = Fernet(key)

def auth():
    def auth_username():
        try:
            with open(username_file, 'r') as f:
                username = f.read().strip()
        except FileNotFoundError:
            username = input('No account found! Enter a new username Please: ').strip()
            with open(username_file, 'w') as f:
                f.write(username)
                auth_password()

    def auth_password():
        try:
            with open(password_file, 'rb') as f:
                enc_password = f.read()
            pass_checker = input("Password: ").strip()
            dec_password = fernet.decrypt(enc_password).decode()

            if pass_checker == dec_password:
                boot_manager()
            else:
                print('Wrong Password')
                auth_password()

        except FileNotFoundError:
            registered_password = input("No Account found! Enter a new password please: ").strip()
            enc_pass = fernet.encrypt(registered_password.encode())
            with open(password_file, 'wb') as f:
                f.write(enc_pass)
            return

        except Exception as e:
            print("Decryption failed:", e)
            auth_password()




    auth_username()
    auth_password()

# def reset_pass(new_pass):
#     with open(password_file,'r') as f:
#         old_pass = f.read()

#     password = input("Enter Old Password : ")
#     while True:
#         if password == old_pass:
#             with open(password_file,'w') as f:
#                 f.write(new_pass)
#                 break 

#         else:
#             continue
import os

unused_variable = 100

def login(username, password):
    if password == "password":
        print("Login Successful")
    else:
        print("Wrong Password")

command = input("Enter command: ")
os.system(command) 
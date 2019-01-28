#!/usr/bin/env python3.6
import string,random,time
from locker import Credentials,UsersData

def new_account(id,user_name,password):
    '''
    Function to creating new account
    '''
    new_user = Credentials(id,user_name,password)
    return new_user

def create_user(user):
    '''
    Function that saves the user's credentials
    '''
    user.create_account()

def authenticate(username,passkey):
    '''
    Function responsible for signing in
    '''
    return Credentials.authenticate_account(username,passkey)

def my_new_data(user_id,data_id,website,web_key):
    '''
    Function that creates new data for storing password
    '''
    new_data = UsersData(user_id,data_id,website,web_key)
    return new_data

def add_data(data):
    '''
    Function that saves the new data created
    '''
    data.add_password()

def display_data(data,number):
    '''
    Function that displays the user data
    '''
    return UsersData.display_data(data,number)

def data_existing(data):
    '''
    Function that checks if user data exists
    '''
    return UsersData.existing_data(data)

def password_generator(count):
    '''
    Function that generates a password
    '''
    pass_list=[]
    round = 1
    while round<=count:
        gen_password = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase )
        pass_list.append(gen_password)
        round+=1
    return ''.join(pass_list)

def copy_password(number,count):
    '''
    Function that copies the password to the clipboard
    '''
    UsersData.copy_password(number,count)
    
def main():
    '''
    Main function
    '''
    my_id=0
    # my_data_id = 0
    entries = []
    # print(password_generator(10))
    print("\n")
    print("       Welcome to password Locker")
    print("-"*40)
    while True:
        print("Type:\n  cc to create new account\n  ss to sign in\n  ex to exit")
        welcome_text = input().lower().strip()
        if welcome_text == "cc":
            print("Create account to continue:"+"\n"+"-"*25 + " \n Enter Username:")
            my_username = input("New Username: ")
            print(" Enter password:")
            my_password = input("New Password: ")

            print("\n")
            create_user(new_account(my_id,my_username,my_password))
            my_id+=1
            print(f"User {my_username} has been created.\nLogin to continue")
            entries.append(0)
            print("-"*27)

        elif welcome_text == "ss".lower():
            print("Enter username and password to continue:")
            print("-"*40)
            my_login = input("Username: ")
            my_key = input("Password: ")
            get_result = authenticate(my_login,my_key)
            if get_result == 0:
                print("\n")
                print("Invalid username and/or password")
                print("-"*27)
            elif get_result!=0:
                # print(f"{get_result.identify} has logged in")
                print("\n")
                print(f"Welcome {get_result.user_name}! What would you like to do?")
                while True:
                    print("Type:\n  ad - Add Password\n  vp - View Passwords\n  cp - copy password to clipboard\n  lo - Log Out")
                    get_input = input().lower()
                    if get_input == "ad":
                        print("Add website and password to store them securely:")
                        print("Enter Website:")
                        my_website = input()
                        print("How long do you want the password to be?")
                        password_length = int(input("Length of password: "))
                        my_webkey = password_generator(password_length)
                        # my_data_id = my_data_id+1
                        my_ident = get_result.identify
                        add_data(my_new_data(my_ident,entries[my_ident],my_website,my_webkey))
                        entries[my_ident]=entries[my_ident]+1
                        print("\nWait...")
                        time.sleep(1.5)
                        print("\n")
                        print(f"***Your password for {my_website} is {my_webkey}***")
                        # print(f"This is the {entries[my_ident]} entry")MKBViStksX 0h5SzxJxQe fOTSiyEZuQ
                        print("-"*45)

                    elif get_input == "vp":
                        if data_existing(get_result.identify):
                            length = entries[get_result.identify]
                            print(f"You have {length} passwords:")
                            print("\n")
                            data_my=0
                            while data_my < length:
                                get_password = display_data(get_result.identify,data_my)
                                print(f"{data_my+1}. {get_password.website} ---- {get_password.web_key}")
                                data_my+=1
                            print("\nEnter a command to continue")
                            print("-"*20)
                        else:
                            print("\nYou have no data.\nType ad to generate some passwords")
                            print("-"*20)

                    elif get_input == "cp":
                        if data_existing(get_result.identify):
                            print("Enter the index of password you want to copy:")
                            get_index = int(input("Enter index: "))-1
                            if get_index >= entries[get_result.identify] or get_index<0:
                                print("\n")
                                print(f"{get_index+1} is invalid. Enter the correct index of password to copy")
                                print("Type vp to confirm the correct index of password to copy")
                                print("-"*30)
                            elif get_index < entries[get_result.identify]:
                                copy_password(get_result.identify,get_index)
                                print("\n")
                                print(f"Password {get_index+1} on the list has been copied, and is ready for pasting")
                                print("-"*30)
                        else:
                            print("\nYou have no data.\nType ad to add some passwords")
                            print("-"*20)

                    elif get_input == "lo":
                        print("\n")
                        print(f"Goodbye {get_result.user_name}!")
                        print("-"*30)
                        break
                    
                    else:
                        print("Invalid entry. Enter command again")
                        print("\n"+"-"*40)

        elif welcome_text == "ex":
            print("\n")
            print(f"Goodbye!!")
            print("-"*30)
            break

        else:
            print("Invalid entry. Enter command again")
            print("\n"+"-"*40)


if __name__ == '__main__':
    main()
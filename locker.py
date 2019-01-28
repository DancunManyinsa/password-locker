import pyperclip
class Credentials:
   
    users_list=[]

    def __init__(self, identify, user_name, password):
        
        self.identify = identify
        self.user_name = user_name
        self.password = password

    def create_account(self):
        
        Credentials.users_list.append(self)
    
    @classmethod
    def authenticate_account(cls, name, key):
     
        for user in cls.users_list:
            if user.user_name == name and user.password == key:
               
                return user
        return 0

class UsersData:
   
    data_list = []
    def __init__(self,ident,data_id,website,web_key):
        self.ident = ident
        self.data_id = data_id
        self.website = website
        self.web_key = web_key
    
    def add_password(self):
       
        UsersData.data_list.append(self)
    
    @classmethod
    def display_data(cls,number,count):
       
        for password in cls.data_list:
            if password.ident == number:
                if password.data_id == count:
                    return password
    
    @classmethod
    def existing_data(cls,number):
      
        for data in cls.data_list:
            if data.ident == number:
                return True
        return False
    
    @classmethod
    def copy_password(cls,number,count):
        found_password = UsersData.display_data(number,count)
        pyperclip.copy(found_password.web_key)
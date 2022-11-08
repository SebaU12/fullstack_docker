class Account:
    def __init__(self, username, password, email):
        self.username = username 
        self.password = password 
        self.email = email
    def toDBCollection(self):
        return{
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
        

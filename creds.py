import getpass

class User:

    def authenticate(self):
        self.user = input('Username: ')
        self.pwd = getpass.getpass(prompt='Password: ')
        return [self.user, self.pwd]
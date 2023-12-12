class User:
    def __init__(self):
        self.users_file = 'users.txt'
        self.load_users()

    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                self.users = dict(line.strip().split(':') for line in file if line)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        with open(self.users_file, 'w') as file:
            for username, password in self.users.items():
                file.write(f"{username}:{password}\n")

    def register(self, username, password):
        if username in self.users:
            print("User already exists.")
            return False
        else:
            self.users[username] = password
            self.save_users()
            print("User registered successfully.")
            return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False

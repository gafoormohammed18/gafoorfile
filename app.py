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



class Inventory:
    def __init__(self):
        self.inventory_file = 'inventory.txt'
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.inventory_file, 'r') as file:
                self.items = dict(line.strip().split(':') for line in file if line)
        except FileNotFoundError:
            self.items = {}

    def save_inventory(self):
        with open(self.inventory_file, 'w') as file:
            for title, amount in self.items.items():
                file.write(f"{title}:{amount}\n")

    def add_item(self, title, amount):
        if title in self.items:
            self.items[title] = str(int(self.items[title]) + amount)
        else:
            self.items[title] = str(amount)
        self.save_inventory()

    def delete_item(self, title):
        if title in self.items:
            del self.items[title]
            self.save_inventory()
        else:
            print("Item not found.")

    def view_inventory(self):
        print("This is the Current List of Books")
        print(f"{'Title':<20} {'Amount':<10}")
        for title, amount in self.items.items():
            print(f"{title:<20} {amount:<10}")



def main_menu():
    user_system = User()
    inventory_system = Inventory()

    while True:
        print("\n1 - For login\n2 - For Register User\n9 - Exit")
        choice = input("Enter your choice: ")

        if choice == "2":
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            user_system.register(username, password)
        elif choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_system.login(username, password):
                while True:
                    print(f"\nInventory Menu: Welcome {username}")
                    print("3 - View Inventory\n4 - Add Book\n5 - Delete Book\n6 - Logout")
                    user_choice = input("Enter your choice from the Menu: ")
                    if user_choice == "3":
                        inventory_system.view_inventory()
                    elif user_choice == "4":
                        title = input("Please enter title you want to add: ")
                        amount = int(input("How many copies? "))
                        inventory_system.add_item(title, amount)
                        inventory_system.view_inventory()
                    elif user_choice == "5":
                        title = input("Enter the title of the comic to delete: ")
                        inventory_system.delete_item(title)
                        inventory_system.view_inventory()
                    elif user_choice == "6":
                        print("you signed off of your account")
                        break
                    else:
                        print("Invalid choice, please try again.")
        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main_menu()

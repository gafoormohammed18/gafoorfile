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


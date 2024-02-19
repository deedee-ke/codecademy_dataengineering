# Define a class to represent a menu
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  # Define a string representation for the Menu object
  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  # Define a method to calculate the total bill for purchased items
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price

# Define dictionaries for menu items
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

# Create Menu objects for different times of day
brunch = Menu('Brunch', brunch_items, 1100, 1600)
early_bird = Menu('Early-bird dinner', early_bird_items, 300, 1800)
dinner = Menu('Dinner', dinner_items, 1700, 2300)
kids = Menu('Kids', kids_items, 1100, 2100)

# Test the string representation and calculate_bill method for the brunch menu
print(brunch)
print(brunch.calculate_bill(purchased_items = ['pancakes', 'home fries', 'coffee']))

# Define a class to represent a franchise
class Franchise:
  def __init__(self, address, menus, name):
        self.address = address
        self.menus = menus
        self.name = name

  # Define a string representation for the Franchise object
  def __repr__(self):
        return f"The {self.name} franchise is located at {self.address}"

  # Define a method to retrieve available menus at a given time
  def available_menus(self, time):
    available_menus = []
    self.time = time
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

# Create a list of menus for a franchise
menus = [brunch, early_bird, dinner, kids]

# Create Franchise objects for different locations
flagship_store = Franchise("1232 West End Road", menus, "flagship")
new_installment = Franchise("12 East Mulberry Street", menus, "new installment")

# Test the string representation and available_menus method for the flagship store
print(flagship_store)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

# Define a class to represent a business
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Create a Business object with franchises
Business("Basta Fazoolin' with my Heart", franchises = [flagship_store, new_installment])

# Define a menu for a different type of cuisine
arepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_menu_items, 1000, 2000)

# Create a franchise for the new cuisine
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu], 'arepas place')

# Create a business with the new franchise
business = Business("Take a' Arepa", [arepas_place])

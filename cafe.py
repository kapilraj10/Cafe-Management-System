# Hity Cafe Menu
menu = {
    'Pizza': 400,
    'Pasta': 100,
    'Burger': 250,
    'Salad': 150,
    'Coffee': 80,
    'Tea': 50,
    'Momo': 130,
    'Noodles': 70,
    'Chowmein': 110,
    'Sandwich': 120, 
    'Tacos': 200,      
    'Ice Cream': 90,   
    'Fries': 70,       
    'Brownie': 60,
    'Samosa': 40,      
    'Curry': 250,      
    'Rice': 100,       
    'Dumplings': 150,  
    'Pancakes': 80,    
    'Smoothie': 110,
}

# Greet the customer
print("Welcome to Hity Cafe!")
print("\nHere is our Menu:\n")

# Display the menu
for item, price in menu.items():
    print(f"{item}: RS{price}")

# Order section
order_total = 0
ordering = True 

# Take orders in a loop
while ordering:
    item = input("\nEnter the name of the item you want to order: ").capitalize()
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available yet!")

    another_order = input("\nDo you want to add another item? (Yes/No): ").lower()
    if another_order != "yes":
        ordering = False  

# Display the total amount
print(f"\nThe total amount for your order is: RS{order_total}")
print("Thank you for visiting Hity Cafe!")

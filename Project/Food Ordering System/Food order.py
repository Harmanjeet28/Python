import getpass

# Food Ordering app
print("This is a food ordering app")

print("\nBefore we start we needed your login information to proceed:")
userEmail = input("Email/Username : ")
userPassword = getpass.getpass("Password : ")

print("\nNice to meet you ", userEmail)

print("\n\nWelcome to Our Restaurant!")
print("\nToday's Menu:")

# Menu in Dictionary
menu = {
    "Caesar Salad": 8.99,
    "Garlic Bread": 5.50,
    "Stuffed Mushrooms": 9.25,
    "Grilled Salmon": 15.99,
    "Spaghetti Carbonara": 12.50,
    "T-Bone Steak": 19.75,
    "Chocolate Lava Cake": 7.99,
    "Vanilla Ice Cream": 4.25,
    "Fruit Salad": 6.50,
    "Freshly Squeezed Orange Juice": 3.99,
    "Red Wine (glass)": 8.50,
    "Soft Drinks": 2.25
}

cart = {}  # Initialize an empty cart as a dictionary to store items and quantities

# Function to display cart and menu
def display_menu():
    print("\nToday's Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def display_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nYour cart:")
        for item, quantity in cart.items():
            print(f"{item}: Quantity - {quantity}")

display_menu()

# Adding items to the cart
userChoice = input("\n\nWould you like to add items to your cart (yes/no)? : ")

while userChoice.lower() == "yes":
    userSearch = input("Type to search for the product: ")

    # Check Items from Dictionary
    if userSearch in menu:
        quantity = int(input(f"How many '{userSearch}' do you want to add? "))
        if userSearch in cart:
            cart[userSearch] += quantity
        else:
            cart[userSearch] = quantity
        print(f"{quantity} {userSearch} added to cart.")
    else:
        print("Sorry, that item is not on the menu.")

    userChoice = input("Would you like to add more items to your cart (yes/no)? : ")

# Display cart and give option to remove items
display_cart()

remove_choice = input("Would you like to remove items from your cart (yes/no)? : ")

while remove_choice.lower() == "yes" and cart:
    display_cart()
    item_to_remove = input("Enter the item you want to remove from your cart: ")

    if item_to_remove in cart:
        del cart[item_to_remove]
        print(f"{item_to_remove} removed from cart.")
    else:
        print("Item not found in cart.")

    remove_choice = input("Would you like to remove more items from your cart (yes/no)? : ")

# Display final cart
print("\nYour final cart:")
display_cart()

# Payment section
print("\n\nGreat! Let's continue towards Checking out then!")
print("How do you want to pay?")
print("\n\nPayment Methods :")
print("1. Cash")
print("2. Credit/Debit")
print("3. Magical Invisible money (cRyPtO?)")

userMoney = input("\nJust mention the payment type : ")

if userMoney == "1":
    print("Place money in the booklet the server provided")
elif userMoney in ["2", "3"]:
    print("Just Tap/Swipe the card on the machine")
else:
    print("Hey, that's illegal. Pay up!")

print("\n\nHope you had a fun time ordering your meal. See you soon!")

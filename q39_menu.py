def display_q39_menu():

    print("\nQ39 Menu:")
    print("1- Wings $13.25")
    print("2- Burnt End Burger $16.50")
    print("3- Brisket $12.99")

def get_total_for_q39():
    total = 0
    while True:
        display_q39_menu()

        choice = input("Enter 1, 2, or 3 to order an item: ")

        if choice == "1":
            price = 13.25
        elif choice == "2":
            price = 16.50
        elif choice == "3":
            price = 12.99
        else:
            
            print("Invalid option. Please enter 1, 2, or 3.")
            continue 
        
        
        try:
            quantity = int(input("How many would you like to order? "))
            if quantity <= 0:
                print("Please enter a valid quantity (greater than 0).")
                continue 
        except ValueError:
            print("Please enter a number for quantity.")
            continue

        # Add the total for the item ordered
        total += price * quantity
        print(f"Your total for now is ${total:.2f}")

        # Ask the user if they want to add more items
        more_items = input("Do you want to add more items (Y/N)? ").lower()
        if more_items == "n":
            break  # Exit the loop if the user is done
    return total

def calculate_delivery_fee_and_tax(total):
    # Check if the total is less than $35 for delivery fee
    if total < 35:
        delivery_fee = 10
        print(f"Your order is less than $35, so you will have to pay a $10 delivery fee.")
    else:
        delivery_fee = 0
        print("You qualify for free delivery because your order is $35 or more.")

    # Calculate the tax (4.3%)
    tax = total * 0.043
    total_with_tax_and_fee = round(total + delivery_fee + tax, 2)

    # Print final total with tax and delivery fee
    print(f"Your order total with tax and delivery fee is: ${total_with_tax_and_fee}")
    return total_with_tax_and_fee

# Main program where everything happens
def main():
    print("Welcome to 101 DELIVERY!")

    # Get the total from Q39 menu
    total = get_total_for_q39()

    # Calculate and print the final total with delivery fee and tax
    final_total = calculate_delivery_fee_and_tax(total)

# Call the main function to start the program
main()


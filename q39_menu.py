def q39_menu():
    print("Q39 Menu:")
    print("1 - Wings $13.25")
    print("2 - Burnt End Burger $16.50")
    print("3 - Brisket $12.99")

def take_order():
    total_price = 0

    while True:
        q39_menu()
        choice = input("what would you like to order (1, 2, 3): ")

        if choice == "1":
            amount = int(input("How many Wings would you like to order? "))
            total_price += 13.25 * amount
            print("You ordered {amount} Wings.")
        elif choice == "2":
            amount = int(input("How many Burnt End Burgers would you like to order? "))
            total_price += 16.50 * amount
            print("You ordered {amount} Burnt End Burger(s).")
        elif choice == "3":
            amount = int(input("How many Briskets would you like to order? "))
            total_price += 12.99 * amount
            print("You ordered {amount} Brisket(s).")
            break
        else:
            print("Invalid choice, please choose 1, 2, 3, or 4.")
        
        print("Your total is: ${total_price:.2f}")
        more_items = input("Would you like to order more? (yes/no): ").strip().lower()
        if more_items != "yes":
            break

    return total_price

def calculate_delivery_fee(total_price):
    if total_price < 35:
        return 10
    else:
        return 0

def calculate_tax(total_price):
    return total_price * 0.043

def calculate_final_total(total_price):
    delivery_fee = calculate_delivery_fee(total_price)
    tax = calculate_tax(total_price)
    final_total = total_price + delivery_fee + tax
    return final_total, delivery_fee, tax

def show_summary(final_total, delivery_fee, tax):
    print("--- Order Summary ---")
    print("Delivery Fee: ${delivery_fee:.2f}")
    print("Tax: ${tax:.2f}")
    print("Total: ${final_total:.2f}")

def main():
    print("Welcome to Q39 Restaurant!")
    total_price = take_order()
    
    final_total, delivery_fee, tax = calculate_final_total(total_price)

    show_summary(final_total, delivery_fee, tax)

if __name__ == "__main__":
    main()


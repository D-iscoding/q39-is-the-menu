def q39_menu():
    print("Q39 Menu:")
    print("1 - Wings $13.25")
    print("2 - Burnt End Burger $16.50")
    print("3 - Brisket $12.99")


def take_order():
    sub_total = 0

    while True:
        q39_menu()
        choices = input("What would you like to order (1, 2, 3): ")

        if choices == "1":
            amount = int(input("How many Wings would you like to order? "))
            sub_total += 13.25 * amount
            print("Wings", amount)

        elif choices == "2":
            amount = int(input("How many Burnt End Burgers would you like to order? "))
            sub_total += 16.50 * amount
            print("Burnt End Burger(s)", amount)

        elif choices == "3":
            amount = int(input("How many Briskets would you like to order? "))
            sub_total += 12.99 * amount
            print("Brisket(s)", amount)

        else:
            print("Invalid, please choose 1, 2, or 3.")

        print("Your subtotal is: ${round(sub_total, 2)}")
        
        more_items = input("Would you like to order more? (yes/no): ").lower()
        if more_items == "no":
            break

    return round(sub_total, 2)


def calculate_order_total(sub_total):
    delivery_fee = 10 if sub_total < 35 else 0
    tax = sub_total * 0.043
    order_total = sub_total + delivery_fee + tax

    return round(order_total, 2), round(delivery_fee, 2), round(tax, 2)


def show_order_summary(order_total, delivery_fee, tax):
    print("---- Order Summary ----")
    print("Delivery Fee: $",delivery_fee)
    print("Tax Fee: $", tax) 
    print("Your Total: $", order_total)


# Program starts here

sub_total = take_order()
order_total, delivery_fee, tax = calculate_order_total(sub_total)
show_order_summary(order_total, delivery_fee, tax)

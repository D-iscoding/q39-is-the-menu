def q39_menu():
    print("Q39 Menu:")
    print("1 - Wings $13.25")
    print("2 - Burnt End Burger $16.50")
    print("3 - Brisket $12.99")


def take_order():
    sub_total = 0

    while True:
        q39_menu()
        choices = input("what would you like to order (1, 2, 3): ")

        if choices == "1":
            amount = int(input("How many Wings would you like to order? "))
            sub_total += 13.25 * amount
            print("Wings", amount)

        elif choices == "2":
            amount = int(
                input("How many Burnt End Burgers would you like to order? "))
            sub_total += 16.50 * amount
            print("Burnt End Burger(s)", amount)

        elif choices == "3":
            amount = int(input("How many Briskets would you like to order? "))
            sub_total += 12.99 * amount
            print("Brisket(s)", amount)
            break
        else:
            print("Invalid, please choose 1, 2, or 3.")

        print("Your total price is", sub_total)
        more_items = input("Would you like to order more? (yes/no): ").lower()
        if more_items == "no":
            break

    return sub_total


def calculate_delivery_fee(sub_total):
    if sub_total < 35:
        return 10
    else:
        return 0


def calculate_order_total(sub_total):
    if sub_total < 35:
        devilvery_fee = 5
    else:
        devilvery_fee = 0

# Program starts here


sub_total = take_order()

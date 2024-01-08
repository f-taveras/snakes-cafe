print("*********************************")
print("** Welcome to the snakes Cafe **")
print("** Please see out menu below  **")
print("**                            **")
print("**Type 'quit' any time to quit**")

appetizers = ["Wings", "Cookies", "Spring Rolls"]
dessert = ["Ice Cream", "Cake", "Pie", "a 10"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
devider = "---------"

menu = [item.lower() for item in appetizers + entrees + dessert + drinks]
order_count = {}

print("\nAppetizers")
print(devider)
for item in appetizers:
    print(item)

print("\nEntrees")
print(devider)

for item in entrees:
    print(item)

print("\nDessert")
print(devider)
for item in dessert:
    print(item)

print("\nDrinks")
print(devider)
for item in drinks:
    print(item)
print()


print("*********************************")
print("**What would you like to order?**")
print("*********************************")


while True:
    userOrder = input(">").lower()
    if userOrder.lower() == 'quit':
        print("\nYour order summary: ")
        for item, count in order_count.items():
            print(f"**** {count} of {item} ****")
        print("\nThank you for visiting, All this looks like a 10...")
        break
    if userOrder in menu:
        if userOrder in order_count:
            order_count[userOrder] += 1
        else:
            order_count[userOrder] = 1
        if order_count[userOrder] >= 2:
            print(str(order_count[userOrder]) + " orders of " + userOrder + " added to your meal")
        else:
            print(str(order_count[userOrder]) + " order of " + userOrder + " added to your meal")
    else:
        print("It is not that kind of place, please try again...")



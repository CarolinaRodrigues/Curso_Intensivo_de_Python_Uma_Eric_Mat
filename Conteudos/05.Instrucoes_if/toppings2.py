requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in  requested_toppings:
    print("Adding "+ requested_topping + ".")
print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers rigth now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
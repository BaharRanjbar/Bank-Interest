def interest(user_inventory, interest_rates,num_of_year):
                                                        #  result = initial_money(user_inventory)
    for i in range(num_of_year):
        user_inventory =int((user_inventory * interest_rates) + user_inventory)
                                                        # result *= 1 + rate(interest_rates)
    return user_inventory



user_inventory = int(input("How many do you have? "))
interest_rates = float(input("What is the iterest rate of the bank? "))
num_of_year = int(input("for How many years? "))


print(interest(user_inventory, interest_rates,num_of_year))

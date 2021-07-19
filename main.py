"""
Evive Software Engineer Test
Author: Kevin Hernandez
"""

# MEAL FORMAT: 1: MAIN, 2: SIDE, 3: DRINK, 4: DESSERT (if the meal is dinner)
BREAKFAST_MENU = {1: "Eggs", 2: "Toast", 3: "Coffee"}
LUNCH_MENU = {1: "Sandwich", 2: "Chips", 3: "Soda"}
DINNER_MENU = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def take_order():
    """
    takes an input of a meal name followed by comma-separated order numbers.
    :param order: a meal order in the format of ([meal] 1,2,2,3,... etc)
    :return: tuple of string meal and a list of nums
    """
    order_list = []
    order = input()
    order_details = order.split(" ")
    nums = order_details[1]  # the list of orders should always come second
    nums = nums.split(",")
    for num in nums:
        num = int(num)
        order_list.append(num)

    order_list.sort()
    order_details.pop()  # remove the second entry, which was a string of numbers

    # since no order can go without a main or a side, do a check here if the order is
    # safely formatted
    if 1 not in order_list:
        return("Unable to process: Main is missing")
    if 2 not in order_list:
        return("Unable to process: Side is missing")

    order_details.append(order_list)
    return order_details

def order_breakfast(order_nums):
    """
    takes in a list of numbers between 1-3 and returns the corresponding
    names of those orders, each with a quantity count.
    :param order_nums: a list of nums between 1-3
    :return: the list of orders in words, ex: Eggs, Toast, Water
    """
    order_string = ""
    order_count = {1:0, 2:0, 3:0}  # keep track of number of times the same order appears
    set_order = set(order_nums)
    # count the number of times an order appears
    for number in set_order:
        count = order_nums.count(number)
        order_count[number] = count
    str = ""
    for order in order_count:
        if (order_count[order] > 1):
            str += "" + BREAKFAST_MENU[order] + "({0})".format(order_count[order])
        else:
            str += "" + BREAKFAST_MENU[order]
        if order < 3:
            str += ", "
    return str

def order_lunch(order_nums):
    pass

def order_dinner(order_nums):
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order = take_order()
    meal = order[0]
    order_nums = order[1]
    if meal == "Breakfast":
        print(order_breakfast(order_nums))
    elif meal == "Lunch":
        order_lunch(order_nums)
    elif meal == "Dinner":
        order_dinner(order_nums)
    else:
        print("Unable to process: enter a valid meal name.")


    # print_hi(BREAKFAST_MENU[3])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

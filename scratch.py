"""
Evive Software Engineer Test
Author: Kevin Hernandez
July 19, 2021
"""
BREAKFAST_MENU = {1: "Eggs", 2: "Toast", 3: "Coffee"}
LUNCH_MENU = {1: "Sandwich", 2: "Chips", 3: "Soda"}
DINNER_MENU = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}
DEFAULT_DRINK = "Water"
MAX_ORDER_NUM = 4  # the maximum an order number can be


class Meal():
    """
    class that builds a meal from a given meal (Breakfast, Lunch, or Dinner) and order details (a list of
    order numbers, none greater than MAX_ORDER_NUM)
    """
    def __init__(self, meal_name, order_details):
        self.meal_name = meal_name  # one of Breakfast, Lunch, or Dinner.
        self.order_details = order_details  # the order list that the user gave
        self.main = None  # the name of the main
        self.main_count = 0
        self.side = None  # the name of the side
        self.side_count = 0
        self.drink = DEFAULT_DRINK  # the name of the drink (default is water)
        self.drink_count = 0
        self.dessert = None  # the name of the dessert (if dinner)
        self.dessert_count = 0
        self.complete_meal_name = ""

    def count_order_details(self):
        """
        count the number of food items in the order
        :return: error message if order formatting is incorrect
        """
        set_order = set(self.order_details)
        # count the number of times an order appears
        for number in set_order:
            if number > MAX_ORDER_NUM:
                return("Unable to process: order is invalid.")
            count = self.order_details.count(number)
            if number == 1:
                self.main_count = count
            elif number == 2:
                self.side_count = count
            elif number == 3:  # change the drink from water to another drink on the menu if applicable
                if self.meal_name == "Breakfast":
                    self.drink = BREAKFAST_MENU[number]
                elif self.meal_name == "Lunch":
                    self.drink = LUNCH_MENU[number]
                elif self.meal_name == "Dinner":
                    self.drink = DINNER_MENU[number]
                self.drink_count = count
            elif number == 4 and self.meal_name == "Dinner":
                self.dessert_count = count

    def set_food_names(self):
        """
        set the names of the items based on what meal it is
        :return:  n/a
        """
        if self.meal_name == "Breakfast":
            self.main = BREAKFAST_MENU[1]
            self.side = BREAKFAST_MENU[2]
            self.drink = DEFAULT_DRINK
        elif self.meal_name == "Lunch":
            self.main = LUNCH_MENU[1]
            self.side = LUNCH_MENU[2]
            self.drink = DEFAULT_DRINK
        elif self.meal_name == "Dinner":
            self.main = DINNER_MENU[1]
            self.side = DINNER_MENU[2]
            self.drink = DEFAULT_DRINK
            self.dessert = DINNER_MENU[4]

    def build_meal(self):
        """
        build the meal from a correctly formatted order ([{meal}, [{order numbers}]])
        :return: meal details and quantities, or error messsage
        """
        self.set_food_names()
        self.count_order_details()
        error_msg = ""

        # handle error messages below. concatenate more specific errors when applicable.
        if self.main_count < 1:
            error_msg = "Unable to process: Main is missing"
        if self.side_count < 1:
            if error_msg:
                error_msg += ", side is missing"
            else:
                error_msg = "Unable to process: Side is missing"
        if (self.meal_name == "Lunch") and self.main_count > 1:
            error_msg = "Unable to process: Sandwich cannot be ordered more than once"
        elif (self.meal_name == "Dinner") and self.dessert_count < 1:
            if error_msg:
                error_msg += ", dessert is missing"
            else:
                error_msg = "Unable to process: Dessert is missing"

        if error_msg:  # if an error message is stored, return it.
            return error_msg
        else:
            # the following variables are for the final print statement, if there are multiple of one item (ex: Eggs(3))
            main_number_str = ""
            side_number_str = ""
            drink_number_str = ""
            dessert_number_str = ""
            if self.main_count > 1:
                main_number_str = "(" + str(self.main_count) + ")"
            if self.side_count > 1:
                side_number_str = "(" + str(self.side_count) + ")"
            if self.drink_count > 1:
                drink_number_str = "(" + str(self.drink_count) + ")"
            if self.dessert_count > 1:
                dessert_number_str = "(" + str(self.dessert_count) + ")"

            # don't include dessert if the meal is not dinner
            if self.meal_name != "Dinner":
                self.complete_meal_name = (self.main + main_number_str + ", " + self.side + side_number_str + ", " +
                                           self.drink + drink_number_str)
                return self.complete_meal_name
            # always include dessert with dinner
            else:
                needs_water = ""
                print(self.drink_count)
                if self.drink_count > 0:
                    needs_water = "Water"
                    self.complete_meal_name = (self.main + main_number_str + ", " + self.side + side_number_str + ", " +
                                               self.drink + drink_number_str + ", " + needs_water + ", " +
                                               self.dessert + dessert_number_str)
                else:
                    self.complete_meal_name = (self.main + main_number_str + ", " + self.side + side_number_str + ", " +
                                               self.drink + drink_number_str + ", " + self.dessert + dessert_number_str)
                return self.complete_meal_name

    def display_order(self):
        """
        display the full order
        :return: n/a
        """
        if self.complete_meal_name:
            print(self.complete_meal_name)

class Food():
    def __init__(self):
        self.order_number = None
        self.name = None
        self.meal = None
        self.is_required = False

    def display_name(self):
        print(self.name)

class Main(Food):
    """
    the main course of a meal
    """
    def setup(self):
        self.order_number = 1
        self.is_required = True

    def meal_food(self):
        if self.meal == "Breakfast":
            self.name = BREAKFAST_MENU[self.order_number]
        if self.meal == "Lunch":
            self.name = LUNCH_MENU[self.order_number]
        if self.meal == "Dinner":
            self.name = DINNER_MENU[self.order_number]

    def build_meal(self):
        pass

class Side(Food):
    """
    the side of a meal
    """
    def setup(self):
        self.order_number = 2
        self.is_required = True

class Drink(Food):
    """
    the drink of a meal
    """
    def setup(self):
        self.order_number = 3
        self.is_required = False
        self.name = "Water"  # drink default across all meals is water

class Dessert(Food):
    """
    the dessert of a meal (only available for dinner)
    """
    def setup(self):
        self.order_number = 4
        self.is_required = False
        self.name = "Cake"  # the default and only dessert available is cake
        self.meal = "Dinner"  # dessert is only available for dinner

def take_order():
    """
    takes an input of a meal name followed by comma-separated order numbers.
    :return: tuple of string meal and a list of nums
    """
    order_list = []
    order = input()
    order_details = order.split(" ")
    if (len(order_details) <= 1) or (len(order_details) > 2):  # check for acceptable formatting
        print("Unable to process: Main is missing, side is missing")
        return
    nums = order_details[1]  # the list of orders should always come second
    nums = nums.split(",")
    for num in nums:
        num = int(num)
        order_list.append(num)

    order_list.sort()
    order_details.pop()  # remove the second entry, which was a string of numbers

    order_details.append(order_list)
    return order_details


def create_meal():
    """
    full meal ordering program. this is the only function passed into __main__.
    :return: a written-out meal order, complete with quantities of each item if applicable.
             can also return an error message
    """
    order = take_order()
    if order:  # if the order has a correct format ("meal", [order numbers])
        order_name = order[0]
        order_details = order[1]
        meal = Meal(order_name, order_details)
        print(meal.build_meal())


if __name__ == '__main__':
    create_meal()

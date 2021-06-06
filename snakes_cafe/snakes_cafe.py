import textwrap

######### Global Variables

user_meal = []
menu_message_array = []
header = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
menu = {
    "Appetizers" : ["Wings", "Cookies", "Spring Rolls"],
    "Entrees" : ["Salmon" , "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts" : ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

footer= """
***********************************
** What would you like to order? **
***********************************
"""

######### Show Input messege  

def creat_show_menu_array(menu):
    for category in menu:
        menu_message_array.append("")
        menu_message_array.append(category)
        menu_message_array.append("----------")
        for item in menu[category]:
            menu_message_array.append(item)

creat_show_menu_array(menu)
show_menu = '\n'.join(menu_message_array)

input_message = f"""
{header}
{show_menu}
{footer}
"""
######### Handling user Inputs

### Helper functions

def quit_handler(user_input):
    if user_input.lower() == "quit":
        print("Thank you for your time ! Bye Bye")
        exit()

def check_user_input_in_menu(user_input,menu):
    for category in menu:
        lower_case_category = map(lambda x : x.lower(),menu[category])
        if user_input.lower() in lower_case_category:
            return True

def check_item_in_user_meal(user_input,user_meal):
    counter = 0
    for meal in user_meal:
        if meal.lower() == user_input.lower():
            counter = counter +1
    return counter

def show_user_input_details(user_input,menu):
        user_meal.append(f"{user_input[0].upper() + user_input[1:].lower()}")
        print()
        print("#" * 50)
        print (textwrap.dedent(f"""
        {check_item_in_user_meal(user_input,user_meal)} order of {user_input[0].upper() + user_input[1:].lower()} have been added to your meal
        """))
        print("Your menu consist of :")
        print(f'{textwrap.dedent(" ".join(user_meal))}')
        user_input= input("\n > ")
        user_input_handler(user_input,menu)

### Main function

def user_input_handler(user_input, menu):
    quit_handler(user_input)
    if check_user_input_in_menu(user_input, menu) == True :
        show_user_input_details(user_input,menu)
    else:
        print("")
        print("This item is not on the menu, But we can order it for you")
        user_meal.append(f"{user_input[0].upper() + user_input[1:].lower()}")
        print("")
        print("Your menu consist of :")
        print(f'{textwrap.dedent(" ".join(user_meal))}')
        user_input= input("\n > ")
        user_input_handler(user_input,menu)

user_input= input(input_message)
user_input_handler(user_input, menu)





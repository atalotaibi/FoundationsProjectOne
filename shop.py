####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "atallah's cupcake"#complete me!
signature_flavors = ["vanilla","lemon","orange"]#complete me!
order_list = []
def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for key in menu:
        print ("%s: %f"%(key,menu[key]))



def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for o_flavors in original_flavors:
        print (o_flavors)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for s_flavors in signature_flavors:
        print (s_flavors)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if (order in menu) or (order in original_flavors) or (order in signature_flavors):
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print ("Enter your order: ")
    while True:
        user_order = raw_input()
        if user_order == "Exit":
            break
        elif is_valid_order(user_order) == True:
            order_list.append(user_order)
        else:
            print ("try again")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5000:
        print "The order can be paid with credit card"
    else:
        print "the order is not eligible for credit card payment"


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for user_order in order_list:
        if user_order in menu:
            total += menu[user_order] 
        elif user_order in original_flavors:
            total += original_price 
        else:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for user_order in order_list:
        print (user_order)
    print (get_total_price(order_list))
    total = get_total_price(order_list)
    accept_credit_card(total)
    print (cupcake_shop_name)

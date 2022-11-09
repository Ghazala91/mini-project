# Mini Project - Ghazala Rehman
# add some product names
# CREATE products list



products_list = ["Pizza", "Burger", "Fries", "Chicken Wings", "Nuggets", "Coke", "Water"]


# PRINT main menu options
def main_menu1():
    print('--Main Menu--')
    print ('[1] -- Products Menu' )
    print ('[2] -- Order Menu' )
    print ('[0] -- Exit' )
    
main_menu1()


# GET user input for main menu option
option = int(input('Enter Main Menu Option:'))


# IF user input is 0:
# EXIT app


if option == 0:
    
        print('Thanks for using the app, see you next time !')
        exit()



# # products menu
# ELSE IF user input is 1:
# PRINT product menu options

elif option == 1:
         


    def product_menu():
        
        print ('--Product Menu--')
        print ('1 -- Product List' )
        print ('2 -- Add Product' )
        print ('3 -- Update Product' )
        print ('4 -- Delete Product' )
        print ('0 -- Main Menu' )
product_menu()

option2 = int(input('Select Product Menu Option:'))# GET user input for product menu option      




if option2 == 0:# IF user input is 0:
   main_menu1()# RETURN to main menu
    

# ELSE IF user input is 1:
# PRINT products list

elif option2 == 1:
    print(products_list)

    
    


    
                      

# ELSE IF user input is 2:
# CREATE new product
# GET user input for product name
# APPEND product name to products list

if option2 == 2:
    
        add_product = input('Add a new Product')
        print(add_product)
        products_list.append(add_product)
        print(products_list)
    
product_menu()
           
               

# ELSE IF user input is 3:
#     # STRETCH GOAL - UPDATE existing product
# PRINT product names with its index value

if option2 == 3:
    for i in range(len(products_list)):
        item = products_list[i]
        print(i, item)

    index_update = int (input('Enter index of product to update'))#  GET user input for product index value  
    update_product = str(input('Enter a product to update it with:'))# GET user input for new product name
    products_list[index_update] = update_product# # UPDATE product name at index in products list
    print(products_list)
    



# ELSE IF user input is 4:
# # STRETCH GOAL - DELETE product
# PRINT products list
# GET user input for product index value
# DELETE product at index in products list

elif option2 == 4:
    for i in range(len(products_list)):
        item = products_list[i]
        print(i, item)
        
    del_product = int(input('Enter product index to delete'))
    products_list[del_product] = products_list
    print(products_list)
   


# else:
#     print('Invalid Input, please try again!')
#     product_menu()


# Week 2

# # orders menu
# ELSE IF user input is 2:

elif option ==2:
    order_dict = [{"customer_name": "John",
                    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                    "customer_phone": "0789887334",
                    "status": "preparing"
                }]

order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

def orders_menu():
    
        print ('--Order Menu--')
        print ('1 -- Orders Dictionary' )
        print ('2 -- Create Order ' )
        print ('3 -- Update Order status' )
        print ('4 -- Delete Order' )
        print ('0 -- Main Menu' )

orders_menu()


option3 = int(input('Select Order Menu Option:'))





if option3 == 0:# IF user input is 0:
    main_menu1()# RETURN to main menu
    

# ELSE IF user input is 1:
#  PRINT orders dictionary

elif option3 == 1:
        print(order_dict)

#  ELSE IF user input is 2:
#  GET user input for customer name
#  GET user input for customer address
#  GET user input for customer phone number
#  SET order status to be 'PREPARING'
#  APPEND order to orders list


elif option3 == 2:
        print("Create New Order")


customer_name = input('Enter customer name')
customer_address = input('Enter customer address')
customer_phone_number = int(input('Enter customer phone number'))
new_dict = {"Name": customer_name, "Address": customer_address, "Telephone": customer_phone_number, "Order status": order_status[0]}
order_dict.append(new_dict)
print(order_dict)


# ELSE IF user input is 3:
#  # UPDATE existing order status
# PRINT orders list with its index values


if option3 == 3:
        for i in range(len(order_dict)):
            item = order_dict[i]
        print(i, item)

#         GET user input for order index value 
#  order_index = int (input('Enter order index '))
 
#         PRINT order status list with index values 
#         GET user input for order status index value 
#         UPDATE status for order 



    



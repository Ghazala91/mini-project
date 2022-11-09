# Week 2

# # orders menu
# ELSE IF user input is 2:

# elif option ==2:
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

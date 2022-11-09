# Week 2

# # orders menu
# ELSE IF user input is 2:

order_dict = [{
 "customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334",
 "status": "preparing"
}]

def orders_menu():
    
        print ('--Order Menu--')
        print ('1 -- Orders Dictionary' )
        print ('2 -- Order Menu ' )
        print ('3 -- Update Order status' )
        print ('4 -- Delete Order' )
        print ('0 -- Main Menu' )


option = int(input('Select Order Menu Option:'))


# if option ==2:
    
print(orders_menu)


#  IF user input is 0:
#  RETURN to main menu

if option == 0:
    main_menu1()

# ELSE IF user input is 1:
#  PRINT orders dictionary

elif option == 1:
    print (order_dict)

#  ELSE IF user input is 2:
#  GET user input for customer name
#  GET user input for customer address
#  GET user input for customer phone number

elif option == 2:
    print("Create New Order")
    customer_name = input('Enter customer name')
    customer_address = input('Enter customer address')
    customer_phone_number = int(input('Enter customer phone number'))


#  SET order status to be 'PREPARING'
#  APPEND order to orders list
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

new_dict = {"Name": customer_name, "Address": customer_address, "Telephone": customer_phone_number, "Preparing": order_status}

order_dict.append(new_dict)

print(order_dict)





# ELSE IF user input is 3:
#  # UPDATE existing order status
#  PRINT orders list with its index values
#  GET user input for order index value
#  PRINT order status list with index values
#  GET user input for order status index value
#  UPDATE status for order
#  ELSE IF user input is 4:
#  # STRETCH - UPDATE existing order


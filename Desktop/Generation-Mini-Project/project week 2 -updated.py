# Mini Project - Ghazala Rehman
# add some product names
# CREATE products list



from pickle import NONE


products_list = ["Pizza", "Burger", "Fries", "Chicken Wings", "Nuggets", "Coke", "Water"]


# PRINT main menu options
def main_menu1():
    print('--Main Menu--')
    print ('[1] -- Products Menu' )
    print ('[2] -- Order Menu' )
    print ('[0] -- Exit' )
    

def product_menu():
        
        print ('--Product Menu--')
        print ('1 -- Product List' )
        print ('2 -- Add Product' )
        print ('3 -- Update Product' )
        print ('4 -- Delete Product' )
        print ('0 -- Main Menu' )

def orders_menu():
    
        print ('--Order Menu--')
        print ('1 -- Orders Dictionary' )
        print ('2 -- Create Order ' )
        print ('3 -- Update Order status' )
        print ('3 -- Update Order' )
        print ('5 -- Delete Order' )
        print ('0 -- Main Menu' )

order_dict = { 
    "customer_name": "John dict",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
 }
                 

order_list = [{ 
    "customer_name": "John 1",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
 },
 { 
    "customer_name": "John 2",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
 }]
   
   
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]
    



# GET user input for main menu option

main_menu1_option = int(input('\n Welcome to G R! \n ' '\n 1- Product Menu' ' \n 2- Order Menu' '\n 0- Exit ' '\n'))
orders_menu_option = int(input('\n Orders Menu \n ' '\n 1- Orders Dictionary' ' \n 2- Create Order' '\n 3- Update Order status ' '\n 4- Update Order' '\n 5- Delete Order' '\n 0- Main Menu' '\n'))


# IF user input is 0:
# EXIT app

while True:

    if main_menu1_option == 0:    
        print('Thanks for using the app, see you next time !')
        exit()



# # products menu
# ELSE IF user input is 1:
# PRINT product menu options

    elif main_menu1_option == 1:
        product_menu()
        

        option2 = int(input('Select Product Menu Option:'))# GET user input for product menu option      




        if option2 == 0:# IF user input is 0:
    #    main_menu1()# RETURN to main menu
         main_menu1_option = int(input('\n Welcome to G R! \n ' '\n 1- Product Menu' ' \n 2- Order Menu' '\n 0- Exit ' '\n'))
         continue
    

# ELSE IF user input is 1:
# PRINT products list

        elif option2 == 1:
            print(products_list)
            continue

    
    


    
                      

# ELSE IF user input is 2:
# CREATE new product
# GET user input for product name
# APPEND product name to products list

        elif option2 == 2:
    
            add_product = input('Add a new Product')
            print(add_product)
            products_list.append(add_product)
            print(products_list)
    
            continue
            
           
               

# ELSE IF user input is 3:
#     # STRETCH GOAL - UPDATE existing product
# PRINT product names with its index value

        elif option2 == 3:
            for i in range(len(products_list)):
                item = products_list[i]
                print(i, item)

            index_update = int (input('Enter index of product to update'))#  GET user input for product index value  
            update_product = str(input('Enter a product to update it with:'))# GET user input for new product name
            products_list[index_update] = update_product# # UPDATE product name at index in products list
            print(products_list)
            continue
        
    



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
            continue
    

# Week 2

# # orders menu
# ELSE IF user input is 2:


    elif main_menu1_option == 2:
        # orders_menu()
         




        if orders_menu_option == 0:# IF user input is 0:
            main_menu1()# RETURN to main menu
            continue

    

# ELSE IF user input is 1:
#  PRINT orders dictionary

        elif orders_menu_option == 1:
         print(order_dict)
         break
                

#  ELSE IF user input is 2:
#  GET user input for customer name
#  GET user input for customer address
#  GET user input for customer phone number
#  SET order status to be 'PREPARING'
#  APPEND order to orders list


        elif orders_menu_option == 2:
            for i in range(len(order_list)):
                # print("Create New Order")
                customer_name = input('Enter customer name')
                customer_address = input('Enter customer address')
                customer_phone_number = int(input('Enter customer phone number'))
                status = "Preparing"
                order_list.append({"Name": customer_name, "Address": customer_address, "Telephone": customer_phone_number, "Order status": status })
                print(order_list)
                # break






# ELSE IF user input is 3:
#  # UPDATE existing order status
# PRINT orders list with its index values

    

        elif orders_menu_option == 3:
            for i in range(len(order_list)):
             item = order_list[i]
             print(i, item)

            order_index = int (input('Enter index of order to update'))#  GET user input for order index value  
            
            for (i, item2) in enumerate(order_status):
                print(i, item2)
            status_index = int (input('Enter order status index '))#GET user input for order status index value 
            order_list[order_index]["status"] = order_status[status_index]
            # print(order_list)
            # continue


# ELSE IF user input is 4:
#  # STRETCH - UPDATE existing order
#  PRINT orders list with its index values
#  GET user input for order index value 
# FOR EACH key-value pair in selected order:
#  GET user input for updated property
#  IF user input is blank:
#  do not update this property
#  ELSE:
#  update the property value with user input

        elif orders_menu_option == 4:
            for (i, item3) in enumerate (order_list):
             print(i, item3)
            index_dict = int(input('Enter order to update'))

            for key,values in order_list[index_dict].items():
             print(key+" : "+values)
            choose_key = input('Enter the item you want to update')
            order_list[index_dict]= choose_key
            print(choose_key)
            # while True:
            updated_property = input('Enter updated customer address')
            
            if updated_property == '':
                # print(order_list)
             print('')
             
                 
            # else:
                    # print('add')
                    # order_list.append[updated_property] = customer_address[order_list]
                    
                # order_list[customer_address] = updated_property
                # print(order_list)



# ELSE IF user input is 5:
#  # STRETCH GOAL - DELETE order

        elif orders_menu_option == 5:
            for i in range(len(order_list)):
                item4 = order_list[i]
                print(i, item4) #  PRINT orders list

        # order_index = int (input('Enter order index '))# GET user input for order index value 
            del_order_index = int (input('Enter order index to delete'))# GET user input for order index value 
            order_list[del_order_index]= order_list  #  DELETE order at index in order list
            print(order_list)
            continue


    



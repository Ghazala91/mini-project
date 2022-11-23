import sys
import csv



# LOAD products list 
products_list = []
with open('./products.csv', 'r', newline='') as file:
         reader = csv.DictReader(file)
         products_list = [row for row in reader]
         file.close()

# LOAD couriers list
couriers_list = []
with open('./couriers.csv', 'r', newline='') as file:
         reader = csv.DictReader(file)
         couriers_list = [row for row in reader] 
         file.close()

         

# LOAD order list
orders_list = []
with open('./orders.csv', 'r', newline='') as file:
         reader = csv.DictReader(file)
         orders_list = [row for row in reader] 
         file.close()

# saving in orders.csv file
def save_orders_file():
    
    with open ('./orders.csv', 'w') as file:
        order_field_names = ['name', 'address', 'telephone', 'courier', 'status', 'items']
        writer = csv.DictWriter(file, fieldnames=order_field_names)
        # instruct the writer to know to write the headers
        writer.writeheader()
        # instruct the writer to write the row
        writer.writerows(orders_list)
        file.close()

# saving in products.csv file
def save_products_file():
    
    with open ('./products.csv', 'w') as file:
        product_field_names = ['name', 'price']
        writer = csv.DictWriter(file, fieldnames=product_field_names)
        # instruct the writer to know to write the headers
        writer.writeheader()
        # instruct the writer to write the row
        writer.writerows(products_list)
        file.close()

# saving in couriers.csv file
def save_couriers_file():
    with open ('./couriers.csv', 'w') as file:
        courier_field_names = ['name', 'phone_number']
        writer = csv.DictWriter(file, fieldnames=courier_field_names)
 # instruct the writer to know to write the headers
        writer.writeheader()
 # instruct the writer to write the row
        writer.writerows(couriers_list)
        file.close()


 
   
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

# PRINT main menu options
def main_menu_options():
    while True:
        # print('--Main Menu--')
        # print ('1 -- Products Menu' )
        # print ('2 -- Couriers Menu' )
        # print ('3 -- Orders Menu' )
        # print ('0 -- Exit' )   
     
        main_menu1_option = int(input('\n Welcome to G R! \n ' 'Choose your option:' '\n 1- Products Menu' ' \n 2- Couriers Menu'' \n 3- Orders Menu' '\n 0- Exit ' '\n'))
        

        if main_menu1_option == 0:    
            save_products_file()
            save_couriers_file()
            save_orders_file()
            print('Thanks for using the app, see you next time !')
            exit()

        elif main_menu1_option == 1:
            product_menu_options()

        elif main_menu1_option == 2:
            couriers_menu_options()

        elif main_menu1_option == 3:
            orders_menu_options()

def product_menu_options():
        
        print ('--Product Menu--')
        print ('1 -- Product List' )
        print ('2 -- Add Product' )
        print ('3 -- Update Product' )
        print ('4 -- Delete Product' )
        print ('0 -- Main Menu' )

        option1 = int(input('Select Product Menu Option:'))# GET user input for product menu option      

        if option1 == 0:# IF user input is 0:
            main_menu_options()

        elif option1 == 1:
            print(products_list)
            product_menu_options()

        elif option1 == 2:

            add_product_name = input('Add a new Product')
            add_product_price = input('Add new Product Price')
            product_dict = {'name': add_product_name, 'price': add_product_price}
            products_list.append(product_dict)
            save_products_file()
            print(products_list)
            product_menu_options()

        elif option1 == 3:
            for i in range(len(products_list)):
                item = products_list[i]
                print(i, item)

            index_update = int (input('Enter index of product to update'))#  GET user input for product index value  
            if 0 <= index_update < len(products_list):
                    print()
            else:
                print("Index doesn't exist in the List")
                        
            for key,values in products_list[index_update].items():
                    print(key+" : "+values)
         
           
            update_product = str(input('Enter a product to update it with or press enter to leave it unchanged:'))
            if update_product != "":
                products_list[index_update]["name"] = update_product # UPDATE product name at index in products list

            update_product_price = str(input('Update product price or press enter to leave it unchanged:'))
            if update_product_price != "":
                products_list[index_update]["price"] = update_product_price

            save_products_file()
            print(products_list)
            product_menu_options()

        elif option1 == 4:
            for i in range(len(products_list)):
                item = products_list[i]
                print(i, item)

            del_product = int(input('Enter product index to delete'))
            del products_list[del_product]
            save_products_file()
            print(products_list)
            product_menu_options()

def couriers_menu_options():
        print ('--Couriers Menu--')
        print ('1 -- Couriers List' )
        print ('2 -- Create New Courier' )
        print ('3 -- Update Courier' )
        print ('4 -- Delete Courier' )
        print ('0 -- Main Menu' )

        option2 = int(input('Select Courier Menu Option:'))


        if option2 == 0:# IF user input is 0:
            main_menu_options()# RETURN to main menu

            # ELIF user inputs 1:
            #  PRINT couriers list
        elif option2 == 1:
                print(couriers_list)
                couriers_menu_options()

        elif option2 == 2:
        
            create_new_courier = input('Create new Courier')
            create_new_courier_phone = int(input('Create new Courier phone number'))
            new_courier_dict = {'name': create_new_courier, 'phone_number': create_new_courier_phone}
            couriers_list.append(new_courier_dict)
            save_couriers_file()
            print(couriers_list)
            couriers_menu_options()

        elif option2 == 3:
            for i in range(len(couriers_list)):
                item = couriers_list[i]
                print(i, item)

            index_courier = int (input('Enter index of Courier to update'))#  GET user input for courier index value 
            if 0 <= index_courier < len(couriers_list):
                    print()
            else:
                print("Index doesn't exist in the List")
                        
            for key,values in couriers_list[index_courier].items():
                    print(key+" : "+values)
            
            
            update_courier = str(input('Enter a courier name to update it with:'))#  GET user input for new courier name
            if update_courier !="":
                couriers_list[index_courier]["name"] = update_courier#  UPDATE courier name at index in couriers list

            update_courier_phone = str(input('Update courier phone number:'))
            if update_courier_phone != "":
                couriers_list[index_courier]["phone_number"] = update_courier_phone

            save_couriers_file()
            print(couriers_list)   
            couriers_menu_options()     

        elif option2 == 4:
            #  PRINT courier list
            for i in range(len(couriers_list)):
                item = couriers_list[i]
                print(i, item)
        
            del_courier = int(input('Enter courier index to delete'))#  GET user input for courier index value
            del couriers_list[del_courier] #  DELETE courier at index in courier list
            save_couriers_file()
            print(couriers_list)
            couriers_menu_options()

def orders_menu_options():
    
        print ('--Order Menu--')
        print ('1 -- Orders List' )
        print ('2 -- Create Order ' )
        print ('3 -- Update Order status' )
        print ('4 -- Update Order' )
        print ('5 -- Delete Order' )
        print ('0 -- Main Menu' )

        option3 = int(input('Select Orders Menu Option:'))

        if option3 == 0:# IF user input is 0:
            main_menu_options()# RETURN to main menu

        elif option3 == 1:
            print(orders_list)
            orders_menu_options()

        elif option3 == 2:
            for i in range(len(orders_list)):
                print("Create New Order")
                customer_name = input('Enter customer name')#  GET user input for customer name
                customer_address = input('Enter customer address') #  GET user input for customer address
                customer_phone = int(input('Enter customer phone number'))# GET user input for customer phonenumber


                # for i in range(len(products_list)): # PRINT products list with its index values
                #     item = products_list[i]
                #     print(i, item)


                for x in range(len(products_list)):
                    print(f'[{x}] {products_list[x]}')  

                order_product_list = input("Please product (with comma to seperate each entry) : ")

                for x in range(len(couriers_list)):
                    print(f'[{x}] {couriers_list[x]}') 
            # GET user inputs for comma-separated list of product index values
            # CONVERT above user input to a string e.g. "2,1,3"
            
                # c_s_product = [int(products_list) for x in input("Select index number from the above products\n").split(', ')]
                
            





                # PRINT couriers list with index value for each courier
                # for i in range(len(couriers_list)):
                #     item = couriers_list[i]
                #     print(i, item)

                # courier_index = int(input('Select index number from the couriers list'))   # GET user input for courier index to select courier
                # status = "Preparing"#  SET order status to be 'PREPARING'

                # CREATE new order dictionary with above properties
                # APPEND order dictionary to orders list
                order_courier_list = int(input("Enter the index from Courier list above : "))
                status = 'PREPARING'
                emptyDictionary = {}
                emptyDictionary['name'] = customer_name
                emptyDictionary['address'] = customer_address
                emptyDictionary['telephone'] = customer_phone
                emptyDictionary['status'] = status
                emptyDictionary['courier'] = order_courier_list 
                emptyDictionary['items'] = order_product_list
                orders_list.append(emptyDictionary)
                print(orders_list)
                save_orders_file()
                # orders_menu_options()

                orders_list.append(emptyDictionary)
                
                print(orders_list)

                # orders_list.append({"name": customer_name, "address": customer_address, "telephone":customer_phone, "courier": courier_index, "status": status, "items": item })#  APPEND order 
                # save_orders_file()
                # print(orders_list)
                orders_menu_options()
            
            

        elif option3 == 3:
            for i in range(len(orders_list)):
                item = orders_list[i]
                print(i, item)

            order_index = int (input('Enter index of order to update'))#  GET user input for order index value  
            
            for (i, item2) in enumerate(order_status):
                print(i, item2)
            status_index = int (input('Enter order status index '))#GET user input for order status index value 
            orders_list[order_index]["status"] = order_status[status_index]
            save_orders_file()
            print(orders_list)
            orders_menu_options()

            
        elif option3 == 4:
            print("Available Orders customers information")
            
            for (i, item3) in enumerate (orders_list):
                print(i, item3)
            index_order_update = int(input("Enter the index of order you want to update:"))
            if 0 <= index_order_update < len(orders_list):
                    print()
            else:
                print("Index doesn't exist in the List")
                        
            for key,values in orders_list[index_order_update].items():
                    print(key+" : "+values)
                
            cust_name= input("Please enter the name you want to update or press enter to leave it unchanged")
            if cust_name != "":
                    orders_list[index_order_update]["name"]=cust_name
            cust_add = input("Please enter your address to update or press enter to leave it unchanged")
            if cust_add != "":
                    orders_list[index_order_update]["address"] = cust_add
            cust_phone  = input("Enter phone number to update or press enter to leave it unchanged")
            if cust_phone != "":
                    orders_list[index_order_update]["telephone"] = cust_phone
            save_orders_file()
            print(orders_list)
            orders_menu_options()

        elif option3 == 5:
            for (i, item4) in enumerate (orders_list):
                print(i, item4)
            index_order_del = int(input("Enter the index of order you want to delete:"))# GET user input order index value
            if 0 <= index_order_del < len(orders_list):
                del orders_list[index_order_del]
                save_orders_file()
                print(orders_list)
                orders_menu_options()
                
            else:
                    print("Index doesn't exist in the List")



main_menu_options()




        
       
        

    


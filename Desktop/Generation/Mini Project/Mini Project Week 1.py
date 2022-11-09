# Mini Project - Ghazala Rehman
# add some product names
# CREATE products list

products_list = ["Pizza", "Burger", "Fries", "Chicken Wings", "Nuggets", "Coke", "Water"]


# PRINT main menu options
def main_menu1():
    print('--Main Menu--')
    print ('[1] -- Products Menu' )
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

elif option == 1:
        

# PRINT product menu options    

    def product_menu():
    
        print ('--Product Menu--')
    print ('1 -- Product List' )
    print ('2 -- Add Product' )
    print ('3 -- Update Product' )
    print ('4 -- Delete Product' )
    print ('0 -- Main Menu' )



print(product_menu)

# GET user input for product menu option

option = int(input('Select Product Menu Option:'))


# IF user input is 0:


if option == 0:
# RETURN to main menu
     main_menu1()


# ELSE IF user input is 1:
# PRINT products list
elif option == 1:
    print(products_list)
    print(product_menu)
                      

# ELSE IF user input is 2:

elif option == 2:

# CREATE new product
# GET user input for product name
# APPEND product name to products list

    add_product = input('Add a new Product')
    print(add_product)
    products_list.append(add_product)
    print(products_list)
    
           
               

# ELSE IF user input is 3:
#     # STRETCH GOAL - UPDATE existing product
# PRINT product names with its index value

elif option == 3:
    for i in range(len(products_list)):
        item = products_list[i]
        print(i, item)

#  GET user input for product index value        
    index_update = int (input('Enter index of product to update'))

# GET user input for new product name
# # UPDATE product name at index in products list
    update_product = str(input('Enter a product to update it with:'))
    products_list[index_update] = update_product
    print(products_list)
    



# ELSE IF user input is 4:
# # STRETCH GOAL - DELETE product
# PRINT products list
# GET user input for product index value
# DELETE product at index in products list

elif option == 4:
    for i in range(len(products_list)):
        item = products_list[i]
        print(i, item)

    
    del_product = int(input('Enter product index to delete'))
    products_list[del_product] = products_list
    print(products_list)
   


else:
    print('Invalid Input, please try again!')
    product_menu()
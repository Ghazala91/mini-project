from file_helper import FileHelper

class OrderManager:
    def __init__(self) -> None:
        pass

    #get_file_contents function is a required argument
    #This is a form of Method Injection
    #get_file_contents is 'contructed' outside of get_orders
    def get_orders(self, get_file_contents): 
        csvAsDict = []  

        #get_file_contents constructed outside, 1 less dependency
        fileContents = get_file_contents("orders.csv")
        for row in fileContents:
            csvAsDict.append({"order_number": row['order_number'], "full_name": row['full_name'], "item": row['item']})
        return csvAsDict

    def display_orders(self, orders: list[dict]):
        print ("Order info: ", orders)



from order_manager import OrderManager
from file_helper import FileHelper

order_manager = OrderManager()

#file_helper now constructed outside of get_orders
file_helper = FileHelper()

#Pass in get_file_contents function as an argument
orders = order_manager.get_orders(file_helper.get_file_contents)

order_manager.display_orders(orders)

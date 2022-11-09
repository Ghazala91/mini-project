from order_manager import OrderManager

def get_orders_test():
    #Test data
    expected_orders = [{'order_number': '1234', 'full_name': 'zach hodges', 'item': 'cabbages'}, {'order_number': '12345', 'full_name': 'megha', 'item': 'lettuce'}]

    order_manager = OrderManager()

    actualOrders = order_manager.get_orders(mock_get_file_contents)
    
    assert expected_orders == actualOrders

    print(actualOrders)
    print("get_orders_test: Passed")


#mocked get_file_contents
#What is the avantage of this? 
#We only care about what get_orders() returns/outputs, so by mocking the below function it's no longer coupled to get_orders()
#and we can control what it returns. The get_orders_tests should not care about what get_file_contents returns.
def mock_get_file_contents(fileName): 
    return [{'order_number': '1234', 'full_name': 'zach hodges', 'item': 'cabbages'}, {'order_number': '12345', 'full_name': 'megha', 'item': 'lettuce'}]

get_orders_test()
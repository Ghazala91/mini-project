from src.calc import increment, decrement, concatenate_names
import unittest


class Test_TestCalcConcat(unittest.TestCase):
    def test_increment(self):
        expected_output = 4
        
        actual_output = increment(3)
        
        assert actual_output == expected_output

    def test_decrement(self):
        expected_output = 4
        
        actual_output = decrement(3)
        
        assert actual_output == expected_output
    
    def test_concatenate_names():
        first_name = 'Ghazala'
        last_name = 'Rehman'
        expected_name = 'GhazalaRehman'
        
        actual_name = concatenate_names(first_name, last_name)
        
        assert actual_name == expected_name
import unittest
import sys
sys.path.append('library')
from output import Output
from process import Process
import utilities


class TestOutput(unittest.TestCase):
    def test_sort_based_on(self):
        list1 = ['4', '3', '5', '1', '2']
        list2 = ['b', 'c', 'a', 'e', 'd']

        list2 = Output.sort_based_on(list1, list2)

        assert list2 == ['e', 'd', 'c', 'b', 'a']
    
    def test_sort_lists(self):
        list1 = ['1', '2', '3', '4', '5']
        list2 = ['a', 'b', 'c', 'd', 'e']
        list3 = ['e', 'd', 'c', 'b', 'a']

        list1, list2, list3 = Output.sort_lists(list1, list2, list3)

        assert list1 == ['5', '4', '3', '2', '1']
        assert list2 == ['e', 'd', 'c', 'b', 'a']
        assert list3 == ['a', 'b', 'c', 'd', 'e']



if __name__ == '__main__':
    unittest.main()

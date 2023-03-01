import unittest
from search import linear_search,binarySearchRecursive,binarySearchIterative

class SearchTestCase(unittest.TestCase):
    """Test for linear search"""
    def test_linear_search(self):
        values = [8,6,8,7,2,1,5,9,4]
        self.assertEqual(linear_search(values,8),0)
        self.assertEqual(linear_search(values,4),8)
        self.assertEqual(linear_search(values,7),3)
        self.assertEqual(linear_search(values,3),-1)

    """Test for recursive binary search"""
    def test_binary_search_recursive(self):
        values = [2,3,4,10,40]
        self.assertEqual(binarySearchRecursive(values,0,len(values)-1,2),0)
        self.assertEqual(binarySearchRecursive(values,0,len(values)-1,40),4)
        self.assertEqual(binarySearchRecursive(values,0,len(values)-1,4),2)
        self.assertEqual(binarySearchRecursive(values,0,len(values)-1,9),-1)

    """Test for iterative binary search"""
    def test_binary_search_iterative(self):
        values = [2,3,4,10,40]
        self.assertEqual(binarySearchIterative(values,2),0)
        self.assertEqual(binarySearchIterative(values,40),4)
        self.assertEqual(binarySearchIterative(values,4),2)
        self.assertEqual(binarySearchIterative(values,9),-1)

if __name__ == "__main__":
    unittest.main()


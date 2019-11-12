import unittest
from student_form import *

class TestNewAlgorithm(unittest.TestCase):
    def test_sort(self):
            array_test=[('102', 'david', 'joshi','Ethical Hacking','rajgadh' ,'982433242'),
                        ('123','subash','rimal','Bsc(Hons)computing','naxal','980605348')]
            expected_result =[('102', 'david', 'joshi','Ethical Hacking', 'rajgadh','982433242'),
                              ('123','subash','rimal','Bsc(Hons)computing','naxal','980605348')]
            sort_by = 0 # sorting by Id, Change values accordance to index value to sort by different parameters.
            bubble_sort(array_test,sort_by)
            self.assertEqual(array_test, expected_result)

    def test_search(self):
        search_by = 1 # searching by First Name, Change values accordance to index value to searching by different parameters.
        search_for = "subash"
        array_test = [('102', 'david', 'joshi', 'Ethical Hacking', '982433242'),
                  ('123', 'subash', 'rimal', 'Bsc(Hons)computing', 'naxal', '980605348')]

        expected_result=[('123', 'subash', 'rimal', 'Bsc(Hons)computing', 'naxal', '980605348')]
        mylist = search(array_test,search_by,search_for)
        self.assertEqual(mylist, expected_result)

if __name__ == '__main__':
    unittest.main()
root.mainloop()

import unittest


def remove_all(list, obj):
    """tous les objets `obj` sont retirés de la liste `list`"""
    while obj in list:
        list.remove(obj)

class TestRemoveAll(unittest.TestCase):
    def test_not_exist_remove(self):
        A = ['a']
        remove_all(A, 'b')
        self.assertListEqual(A, ['a'])
    def test_one_remove(self):
        A = ['a']
        remove_all(A, 'a')
        self.assertListEqual(A, [])
    def test_all_remove(self):
        A = ['a', 'a', 'a']
        remove_all(A, 'a')
        self.assertListEqual(A, [])
    def test_all_remove_but_one(self):
        A = ['b', 'a', 'b']
        remove_all(A, 'b')
        self.assertListEqual(A, ['a'])


unittest.main()
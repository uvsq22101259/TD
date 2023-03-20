#!/usr/bin/python3

import unittest

def append_unique(list, obj):
    """
    l'objet `obj` est ajouté à la liste `list` si il n'y est pas déjà présent
    """
    list.append(obj)
    

def remove_all(list, obj):
    """tous les objets `obj` sont retirés de la liste `list`"""
    for i in range(len(list)):
        if list[i] == i:
            list.sort(i)

def merge_unique(list_a, list_b):
    """
    le contenu de la liste `list_b` est ajouté à `list_a` si pas deja présent
    """
    list_a.extend(list(list_b))
    

def split_integer(list):
    """
    la liste `list` est separée en deux listes, l'une contenant les entiers, et
    l'autre le reste
    retour de la fonction : liste des entiers, liste des autres objets
    """
    entier = []
    autre =[]
    for i in list:
        if type(i) == int:
            entier.append(i)
        else:
            autre.append(i)
    

class TestAppendUnique(unittest.TestCase):
    def test_basic_append(self):
        A = []
        append_unique(A, 'a')
        self.assertListEqual(A, ['a'])
    def test_not_unique_append(self):
        A = ['a']
        append_unique(A, 'a')
        self.assertListEqual(A, ['a'])

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

class TestMergeUnique(unittest.TestCase):
    def test_null_merge(self):
        A = []
        B = []
        merge_unique(A, B)
        self.assertListEqual(A, [])
        B = ['a']
        merge_unique(A, B)
        self.assertListEqual(A, ['a'])
        B = []
        merge_unique(A, B)
        self.assertListEqual(A, ['a'])
    def test_simple_merge(self):
        A = ['a']
        B = ['b']
        merge_unique(A, B)
        self.assertListEqual(A, ['a', 'b'])
    def test_not_unique_merge(self):
        A = ['a']
        B = ['a', 'b']
        merge_unique(A, B)
        self.assertListEqual(A, ['a', 'b'])
        B = ['b']
        merge_unique(A, B)
        self.assertListEqual(A, ['a', 'b']) 

class TestSplitInteger(unittest.TestCase):
    def test_null_split(self):
        A = []
        I, O = split_integer(A)
        self.assertListEqual(I, [])
        self.assertListEqual(O, [])
    def test_only_integers_split(self):
        A = [1, 2]
        I, O = split_integer(A)
        self.assertListEqual(I, [1, 2])
        self.assertListEqual(O, [])
    def test_only_others_split(self):
        A = [3.14, 'a', []]
        I, O = split_integer(A)
        self.assertListEqual(I, [])
        self.assertListEqual(O, [3.14, 'a', []])
    def test_split(self):
        A = [1, 3.14, 'a', 2, 3, []]
        I, O = split_integer(A)
        self.assertListEqual(I, [1, 2, 3])
        self.assertListEqual(O, [3.14, 'a', []])

if __name__ == '__main__':
    unittest.main()

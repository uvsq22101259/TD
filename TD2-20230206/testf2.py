import unittest


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
    return entier, autre


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
    
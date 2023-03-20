

import os
import tempfile
import unittest

def file_cat(path_in):
    file_in = open(path_in,"r")
    ligne = file_in.readline()
    while ligne != "":
        print(ligne, end=" ")
        ligne = file_in.readline()
    file_in.close()

def file_copy(path_in, path_out):
    file, n_file = open(path_in,"r"), open(path_out,"w")
    n_file.writelines(file.readlines())

def file_move(path_in, path_out):
    with open(path_in) as fin:
        ligne = fin.readline()
    os.remove(path_in)
    with open(path_out,"w") as fout:
        fout.writelines()
    

def file_find(path, filename):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name == filename:
                print(os.path.join(root, name))

def file_diff(path_a, path_b):
    with open(path_a,"r") as a :
        with open(path_b,"r") as b:
            print(a.readlines() == b.readlines())

def file_sed_char(path, target, modif):
    with open(path) as f:
        lignes = f.readlines()
    with open(path,"w") as f_out:
        for ligne in lignes:
            f_out.write(ligne.replace(target,modif))

def file_sed_string(path, target, modif):
    with open(path) as f:
        lignes = f.readlines()
    with open(path,"w") as f_out:
        for ligne in lignes:
            f_out.write(ligne.replace(target,modif))
            print("bite")

def file_grep_char(path_in, target):
    with open(path_in) as f:
        texte =  f.read()
    for i in range(len(texte)):
        if texte[i] == target:
            print(i)

def file_grep_string(path_in, target):
    taille = len(target)
    with open(path_in, "r+") as file:
        occurence = []
        nline = 0
        for line in file:
            nline += 1
            while target in line :
                ind = line.index(target)
                occurence.append((nline,ind))
                line = line[:ind+taille].replace(target," "*taille)+ line[ind+taille:]
               
        return occurence

def file_grep_line(path_in, target):
    with open(path_in,"r") as file:
        return target in file.readlines()

class TestBasicFileGrepString(unittest.TestCase):
    def test_empty_file(self):
        tmp_f = tempfile.NamedTemporaryFile()
        tmp_f.flush()

        prev = os.dup(1)
        os.close(1)
        _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        file_grep_string(tmp_f.name, 'a')
        os.dup2(prev, 1)

        tmp_f.close()
        with open('__buffer__') as exec_res:
            good_lines = []
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)
        
        os.unlink('__buffer__')

    def test_simple_search(self):
        tmp_f = tempfile.NamedTemporaryFile(mode='w')
        tmp_f.writelines([
            "123\n",
            "abc\n",
            "ABC\n"
        ])
        tmp_f.flush()

        prev = os.dup(1)
        os.close(1)
        _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        file_grep_string(tmp_f.name, 'abc')
        os.dup2(prev, 1)

        tmp_f.close()
        with open('__buffer__') as exec_res:
            good_lines = ['1:0\n']
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)

print(file_grep_string("text.txt", "aB"))


import os
import tempfile
import unittest
import pwd 
from time import gmtime
def mode_octal_to_str(octal_value):
    octal_str = octal_value
    print(octal_str)
    permission = ""
    for i in range(len(octal_str)):
        
        if int(octal_str[i]) - 4 >= 0:
            permission += "r"
        else:
            permission += "-"

        if  int(octal_str[i]) == 2 or  int(octal_str[i])% 3 == 0 or  int(octal_str[i]) ==  7:
            permission += "w"     
        else : 
            permission += "-"

        if int(octal_str[i]) % 2== 1:
            permission += "x"
        else:
            permission += "-"
        
    return permission

def mode_str_to_octal(str_value):
    octal_value = "0o"
    for i in range(3):
        val = 0
        if "r" in str_value[i]:
            val += 4
        if "w" in str_value[i]:
            val += 2
        if "x" in str_value[i]:
            val += 1
        octal_value += str(val)
    return int(octal_value,8)
            

def change_mode(path_in, new_mode):
    os.chmod(path_in, new_mode)

def touch(path_in):
    os.utime(path_in)

def dir_list(path_in):
    return os.listdir(path_in)

def dir_all_list(path_in):
    for fich in dir_list(path_in) :
        info = os.stat(fich)
        mode = mode_octal_to_str(oct(info.st_mode)[-3:])
        user = pwd.getpwuid(info.st_uid).pw_name
        size = info.st_size
        time = gmtime(info.st_atime)
        y = time.tm_year
        m = time.tm_mon
        d = time.tm_mday
        mois = {1:"Jan.",2:"Fev.",3:"Mars",4:"Avril",5:"Mai",6:"Juin",
                7:"Juillet",8:"Août",9:"Sept.",10:"Oct.",11:"Nov.",12:"Dec."}
        name = os.path.basename(fich)
        print( mode, user, size, d, mois[m], y, name)

def dir_rec_list(path_in):
    for dir in os.walk(path_in):
        print(dir)

class TestSimpleDirList(unittest.TestCase):
    def test_empty_dir(self):
        with tempfile.TemporaryDirectory() as folder:
            prev = os.dup(1)
            os.close(1)
            _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
            dir_rec_list(folder)
            os.dup2(prev, 1)

        with open('__buffer__') as exec_res:
            good_lines = []
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')

    def test_two_files(self):
        with tempfile.TemporaryDirectory() as folder:
            files = [tempfile.NamedTemporaryFile(dir=folder) for _ in range(2)]
            for file in files:
                file.flush()

            prev = os.dup(1)
            os.close(1)
            _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
            dir_rec_list(folder)
            os.dup2(prev, 1)

            for file in files:
                file.close()

        with open('__buffer__') as exec_res:
            good_lines = [os.path.basename(file.name) + '\n' for file in files]
            good_lines.sort()
            exec_lines = exec_res.readlines()
            exec_lines.sort()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')

    def test_two_dirs(self):
        with tempfile.TemporaryDirectory() as folder_A:
            file_A = tempfile.NamedTemporaryFile(dir=folder_A)
            file_A.flush()

            with tempfile.TemporaryDirectory(dir=folder_A) as folder_B:
                file_B = tempfile.NamedTemporaryFile(dir=folder_B)
                file_B.flush()

                prev = os.dup(1)
                os.close(1)
                _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
                dir_rec_list(folder_A)
                os.dup2(prev, 1)

                file_A.close()
                file_B.close()

        with open('__buffer__') as exec_res:
            fol_base_A = os.path.basename(folder_A)
            fol_base_B = os.path.basename(folder_B)
            good_lines = [
                os.path.basename(file_A.name) + "\n",
                fol_base_B + "\n",
                fol_base_B + "/" + os.path.basename(file_B.name) + "\n"
            ]
            good_lines.sort()
            exec_lines = exec_res.readlines()
            exec_lines.sort()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')

    

print(dir_rec_list(os.getcwd()))
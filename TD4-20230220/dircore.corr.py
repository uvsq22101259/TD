#!/usr/bin/python3

import os
import tempfile
import unittest
from pwd import getpwuid
import time

def mode_octal_to_str(octal_value):
    octal_perm = [
        (octal_value // 64) % 8,    # user perm
        (octal_value // 8) % 8,     # group perm
        octal_value % 8             # other perm
    ]

    str_perm = [
        '---', '--x', '-w-', '-wx',
        'r--', 'r-x', 'rw-', 'rwx'
    ]

    str_value = ""
    for perm in octal_perm:
        str_value += str_perm[perm]

    return str_value

def mode_str_to_octal(str_value):
    octal_perm = {
        0: {'-': 0, 'r': 0o400},
        1: {'-': 0, 'w': 0o200},
        2: {'-': 0, 'x': 0o100},

        3: {'-': 0, 'r': 0o040},
        4: {'-': 0, 'w': 0o020},
        5: {'-': 0, 'x': 0o010},

        6: {'-': 0, 'r': 0o004},
        7: {'-': 0, 'w': 0o002},
        8: {'-': 0, 'x': 0o001}
    }

    if len(str_value) != 9:
        raise ValueError

    octal_value = 0
    for key, value in enumerate(str_value):
        octal_value += octal_perm[key][value]

    return octal_value

def change_mode(path_in, new_mode):
    os.chmod(path_in, new_mode)

def touch(path_in):
    if os.path.exists(path_in):
        os.utime(path_in)
    else:
        a = os.open(path_in, os.O_CREAT)
        os.close(a)

def dir_list(path_in):
    files = os.listdir(path_in)

    for file in files:
        print(file)

def dir_all_list(path_in):
    files = os.listdir(path_in)

    print("# mode user size last_access_time name")
    for file in files:
        stat = os.stat(path_in + '/' + file)
        print("%s %s %d %s %s" % (
            mode_octal_to_str(stat.st_mode),
            getpwuid(stat.st_uid).pw_name,
            stat.st_size,
            time.strftime("%d %b %Y", time.gmtime(stat.st_atime)),
            file
        ))

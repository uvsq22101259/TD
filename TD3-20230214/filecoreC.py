#!/usr/bin/python3

import os
import tempfile
import unittest

def file_cat(path_in):
    with open(path_in) as f_in:
        line = f_in.readline()
        while line != '':
            print(line, end='')
            line = f_in.readline()

def file_copy(path_in, path_out):
    with open(path_in) as f_in:
        with open(path_out, 'w') as f_out:
            f_out.writelines(f_in.readlines())

def file_move(path_in, path_out):
    with open(path_in) as f_in:
        lines = f_in.readlines()
    os.remove(path_in)
    with open(path_out, 'w') as f_out:
        f_out.writelines(lines)

def file_diff(path_a, path_b):
    with open(path_a) as f_a:
        lines_a = f_a.readlines()
    with open(path_b) as f_b:
        lines_b = f_b.readlines()
    return lines_a == lines_b

def file_sed_char(path, target, modif):
    with open(path) as f_in:
        lines = f_in.readlines()
    with open(path, 'w') as f_out:
        for line in lines:
            f_out.write(line.replace(target, modif))

def file_sed_string(path, target, modif):
    with open(path) as f_in:
        lines = f_in.readlines()
    with open(path, 'w') as f_out:
        for line in lines:
            f_out.write(line.replace(target, modif))

def file_grep_char(path_in, target):
    with open(path_in) as f_in:
        c = f_in.read(1)
        while c != '':
            if c == target:
                print(f_in.tell() - 1)
            c = f_in.read(1)

def file_grep_line(path_in, target):
    with open(path_in) as f_in:
        lines = f_in.readlines()
    for line in lines:
        if target == line[:-1]:
            print(True)
            return
    print(False)

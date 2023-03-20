#!/usr/bin/python3

import os

def file_cat(path_in):
    fd = os.open(path_in, os.O_RDONLY)
    rd_buff = os.read(fd, 16)
    while len(rd_buff) != 0:
        print(rd_buff.decode(), end='')
        rd_buff = os.read(fd, 16)
    os.close(fd)

def file_copy(path_in, path_out):
    fd_in = os.open(path_in, os.O_RDONLY)
    fd_out = os.open(path_out, os.O_WRONLY | os.O_CREAT, 0o660)
    rd_buff = os.read(fd_in, 16)
    while len(rd_buff) != 0:
        os.write(fd_out, rd_buff)
        rd_buff = os.read(fd_in, 16)
    os.close(fd_in)
    os.close(fd_out)

def file_move(path_in, path_out):
    os.link(path_in, path_out)
    os.unlink(path_in)

def file_find(path, filename):
    list = os.listdir(path)
    for elt in list:
        if elt == filename:
            print(path + '/' + filename)
        if os.path.isdir(path + '/' + elt):
            file_find(path + '/' + elt, filename)

def file_diff(path_a, path_b):
    fd_a = os.open(path_a, os.O_RDONLY)
    fd_b = os.open(path_b, os.O_RDONLY)
    buff_a = os.read(fd_a, 16)
    buff_b = os.read(fd_b, 16)
    while len(buff_a) != 0 or len(buff_b) != 0:
        if buff_a != buff_b:
            os.close(fd_a)
            os.close(fd_b)
            return False
        buff_a = os.read(fd_a, 16)
        buff_b = os.read(fd_b, 16)
    os.close(fd_a)
    os.close(fd_b)
    return True

def file_sed_char(path, target, modif):
    fd = os.open(path, os.O_RDWR)
    b_target = bytes(target, 'utf-8')
    b_modif = bytes(modif, 'utf-8')
    char = os.read(fd, 1)
    while len(char) != 0:
        if char == b_target:
            os.lseek(fd, -1, os.SEEK_CUR)
            os.write(fd, b_modif)
        char = os.read(fd, 1)
    os.close(fd)

def file_sed_string(path, target, modif):
    fd = os.open(path, os.O_RDONLY)
    content = b''
    buff = os.read(fd, 16)
    while len(buff) != 0:
        content += buff
        buff = os.read(fd, 16)
    os.close(fd)
    content = content.decode().replace(target, modif).encode('utf-8')
    fd = os.open(path, os.O_WRONLY | os.O_TRUNC)
    os.write(fd, content)
    os.close(fd)

def file_grep_char(path_in, target):
    fd = os.open(path_in, os.O_RDONLY)
    b_target = bytes(target, 'utf-8')
    char = os.read(fd, 1)
    while len(char) != 0:
        if char == b_target:
            print(os.lseek(fd, 0, os.SEEK_CUR) - 1)
        char = os.read(fd, 1)
    os.close(fd)

def file_grep_line(path_in, target):
    fd = os.open(path_in, os.O_RDONLY)
    content = b''
    buff = os.read(fd, 16)
    while len(buff) != 0:
        content += buff
        buff = os.read(fd, 16)
    os.close(fd)
    content = content.decode().split('\n')
    if target in content:
        print(True)
        return
    print(False)

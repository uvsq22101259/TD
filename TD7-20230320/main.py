import os

os.mkfifo("/home/elie/Documents/TD_405/TD7-20230320/tubenome", 0o666)
print(".")
fd = os.open("/home/elie/Documents/TD_405/TD7-20230320/tubenome", os.O_WRONLY)
print(".")
os.write(fd, b"hello world!")
print(".")

os.close(fd)
print(".")
p = os.fork()

if not p:
    fd = os.open("/home/elie/Documents/TD_405/TD7-20230320/tubenome", os.O_RDONLY)
    MSG = os.read(fd , 64)
    os.close(fd)
    print(MSG)
print("hey")
os.unlink("/home/elie/Documents/TD_405/TD7-20230320/tubenome")
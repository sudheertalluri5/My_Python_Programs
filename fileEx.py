with open("C:/Networking/hamming_code.c",'r') as File1:
    file_stuff=File1.read()
    print(file_stuff)
print(File1.closed)
print(file_stuff)

file_stuff=open("C:/Networking/hamming_code.c",'r')
print(file_stuff.read())
print(file_stuff.closed)
file_stuff.close()
print(file_stuff.closed)

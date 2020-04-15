with open("C:/py_prog/isappend.txt",'a') as file1:
    file1.write("YES")
with open("C:/py_prog/isappend.txt",'r') as file2:
    print(file2.read())
print(file1)

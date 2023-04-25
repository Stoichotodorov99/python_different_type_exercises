import sys
sorted_file= open("new_file.txt","w")
with open(sys.argv[1],"r") as file:
    for i in sorted(file):
        sorted_file.write(i)
fp = open("text.txt", "r") #this is open for reading
print(fp.read()) #read () method gets entire file content
fp.close() #this is good practice

#same thing using a context manager
with open ("text.txt, "r"") as f:
    print(f.read())
#no need to close

#read the file line by line
print("now we read it line by line")
with open ("text.txt", "r") as f:
    for line in f: #f is iterable
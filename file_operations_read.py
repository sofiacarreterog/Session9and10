fp = open("text.txt") # this is open for reading
print(fp.read()) # read() method gets the entire file content
fp.close() #this is good practice

# same thing using a context manager!
# this is more pythonic
with open("text.txt", "r") as f:
    print(f.read())
# no need to close

# read the file line by line
with open("text.txt", "r") as f:
    for line in f: # f is iterable and we get each individual line
        print(f.read())
        # print(lind, end="")
        print(line.rstrip())
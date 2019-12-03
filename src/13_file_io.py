"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('./src/foo.txt', 'r')
with open('./src/foo.txt') as f:
    read_data = f.read()
    print(read_data)

"""for i in f:
    print(i)
f.close()"""

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open('./src/bar.txt', 'w')
f.write("one line\ntwo line\nthree line\n")
f.close()

f = open('./src/bar.txt', 'r')
with open('./src/bar.txt') as f:
    read_data = f.read()
    print(read_data)
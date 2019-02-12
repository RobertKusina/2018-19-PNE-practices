# Example of reading a file located in our local file system

NAME = "mynotes.txt"

# Open the file
#myfile is an object, inside there will be things

myfile = open(NAME, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are : {}".format(contents))

myfile.close()

f = open(NAME, 'a')
f.write("THIS IS A TEXT EXAMPLE FOR ADDING TO MY FILE")
f.close()
print("This is the end")

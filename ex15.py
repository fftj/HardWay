# importing argv for getting arguments from CLI
from sys import argv

# assigning names to two arguments
script, filename = argv

# getting file into txt
txt = open(filename)

# output of filename
print "Here's your file %r:" % filename
# output of the file
print txt.read()

# asking for input
print "Type the filename again:"
# waiting for the input with the custom prompt
file_again = raw_input("> ")

# reopening same file and getting it to another variable
txt_again = open(file_again)

# reoutputting the file content to the screen
print txt_again.read()

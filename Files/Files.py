
# using files in python

# write to a file
with open("names.txt", "w") as f: # with "w" being "write".
    f.write("Saad Mann"+ "\n") # \n will separate the lines.
    f.write("Chuann Gumm"+ "\n")
    f.write("Rose Garden") # the last line that will be written should not contain "/n" as it will cause an error.
# end with

# run this and then write click "files" under solution explorer and open click "open folder in file explorer "names.txt" should in here. 

# writing numbers to a file
with open("numbers.txt", "w") as file:
    with open("numbers.txt", "w") as file:
        file.write(str(49)+ "\n")
        file.write(str(50)+ "\n")
        file.write(str(51)+ "\n") # when writing numbers, they must be converted to strings, integers will cause an error.
# end with

# same as before, run this and repeat the file opening process for "numbers.txt".

# reading a file - one column of data
with open("names.txt", "r") as myFile: # with "r" being "read".
    for line in myFile:
        print(line)
        # end for
# end with

# there should now be a blank line between each name within "names.txt".

# reading a file - names into a list
nameList = [] # empty list

with open("names.txt", "r") as f:
    for row in f:
        nameList.append(row)
    # end for
# end with
print(nameList)

# when we run this, we get the contents of the file (as well as "\n" which shows separation between lines).

# reading a file - numbers into a list
numList = [] # empty list

with open("numbers.txt", "r") as file:
    for row in file:
        numList.append(int(row)) # we're using "int" to get back the actual numbers instead of the strings which they had been converted to.
    # end for
# end with
print(numList)

# print lists
for index in range(len(nameList)):
    print(nameList[index])
# end for

for index in range(len(numList)):
    print (numList[index])
# end for                 


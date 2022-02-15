# Ryan Lugo: RJL 2/15/22

opFile = open("my_file.txt","r+")
contents = opFile.read()

opFile.write("RJL 2/15/22\n")
opFile.write("'Hello World!'\n")
opFile.write("I make games for fun.\n")
opFile.close()
name = input("enter file: ")
handle = open(name, "r")
text = handle.read()
words = text.split()
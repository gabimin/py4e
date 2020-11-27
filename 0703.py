count = 0
inputfile = input("Enter the file name: ")

if inputfile == "na na boo boo" :
    print("NA NA BOO BOO TO YOU - You have been punk'd!")

else:
    try:
        openfile = open(inputfile)
    except:
        print("File cannot be opened:", inputfile)
        quit()

    for line in openfile :
        if not line.startswith("Subject") : continue
        else :
            count = count + 1

    print("There were", count, "subject lines in", inputfile)

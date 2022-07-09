def swapFile():
    file1 = input("Please enter your first file: ")
    file2 = input("Please enter your second file: ")
    
    with open(file1,"r") as x:
        dataX = x.read()

    with open(file2,"r") as y:
        dataY = y.read()

    with open(file1,"w") as x:
        x.write(dataY)

    with open(file2,"w") as y:
        y.write(dataX)

swapFile()

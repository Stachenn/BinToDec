# Pozyskanie liczby
def decToBin():
    while True:
        userBin = input("Type dec num : ")
    
        try:
            userBinInt = int(userBin)
        except ValueError:
            print("Selected number isnt a int")
        else:
            break

    userBinTable = []
    binTable = []
    j = 1
    cursor = len(userBinTable)-1
    readyString = ""
    m = 0

    while True:
        binTable.append(j)
        if userBinInt <= j:
            break
        j = j * 2
#for i in binTable:
#       print(i)
    while True: 
        try:
            # Debugowanie znowu print("\n",binTable[cursor])
#if cursor <= -1:
#               break
            if binTable[cursor] <= userBinInt:
                readyString += "1"
                # Nie potrzebne instrukcja do debugowania ;) 
    #print(binTable[cursor], "|", userBinInt, "|1")
                userBinInt-=binTable[cursor]
            else:
                # To samo 
#print(binTable[cursor], "|", userBinInt, "| 0")
                readyString+= "0"
            cursor-=1
        except IndexError:
            break
    return f"Result : {str(readyString)}\n\n\n\n"

def binToDec():
    while True:
        userBin = input("Bin number to convert : ")
    
        try:
            userBinInt = int(userBin)
        except ValueError:
            print("Number isnt int")
        else:
            break
    j = 1
    cursorForDecompite = len(userBin)-1
    m = len(userBin)-1
    userBinTable = []
    binTable = []
    readyString = 0
    cursor = 0

    while True:
        if m == -1:
            break
        binTable.append(j)
        userBinTable.append(int(userBin[m]))
        j = j * 2
        m -= 1
    while True:
        try:
#print("ff")
#print(type(userBinTable[cursor]), "|", "1")
#print(userBin[cursor])
#print(userBinTable[cursor])
            if userBin[cursor] == "1":
                readyString += int(binTable[cursorForDecompite])
        #print("bin=",int(binTable[cursorForDecompite]))
        #print("ready=",readyString,"\n\n")
            if cursor == len(userBin)-1:
                break
            cursor += 1
            cursorForDecompite -= 1
        except IndexError:
            break
#print(readyString)
    return f"Result : {str(readyString)}\n\n\n\n"

def main():
    while True:
        print("\n| [C]Stachenn all rights reserved | \n\nChose a option? \n 1 - Bin to dec \n 2 - Dec to bin \n 3 - Exit")
        choice = input()
        if choice == "1":
            print(binToDec())
            break
        if choice == "2":
            print(decToBin())
            break
        if choice == "3":
            exit(0)
        else:
            print("Chosen choice is not in option")
while True:
    main()

def main():
    userInput = input("Enter the numner: ")

    userInput = int(userInput)

    if(userInput % 2 == 0):
        print("It's an even number")
    if(userInput % 2 != 0):
        print("It's not an even number")

while True:
    main()
    isQuit = input("Do you want to run again(Y/N)? ")
    if(isQuit == 'Y' or isQuit == 'y'):
        a = 1
    else:
        exit()

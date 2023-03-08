
def main():
    # Inizializing the variables
    number = input("Type the number: ")
    exponet = input("Type the exponent: ")
    answer = 0
    loop = 0
    run = True

    #Converting to Int
    number = int(number)
    exponet = int(exponet)

    # Finding the exponent
    while run:
        if loop == 1:
            answer = number * number
            loop = loop + 1
        elif loop == exponet:
            run = False
        elif loop != 1:
            answer = answer * number
            loop = loop + 1
    print(number, "raised to the power of", exponet, "is", answer)

    #Checks that user want to run the program again or not
    again = input("Do you want to run it again?(y/n): ")
    if again == "Y" or again == "y":
        main()
    else:
        exit(0)

print("Welcome!")
main()

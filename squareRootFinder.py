import math

def main():
    #The number which we find square root.
    number = input("Type a number: ")

    #Checks whether variable "number" is a string or not.
    try:
        number = int(number)
    except:
        print("Please type a number")
        main()

    squareRoot = math.sqrt(number)
    print(squareRoot)

    main()

main()

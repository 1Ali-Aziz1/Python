def main():
    year = input("year: ")
    
    year = int(year)
    
    if(year % 4 == 0):
        print(year,"is a leap year")
    elif(year % 4 != 0):
        print(year,"is not a leap year")
    else:
        print("There was an error.")

while True:
    main()

import random
print("Welcome to password creator")
num_val = input("How many numbers do you want in your password: ")
char_val = input("How many charectors do you want in your password: ")
symbol_val = input("How many symbols do you want in your password: ")

cap_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
low_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","m","n","o","p","q","r","s","t","u","v","x","x","y","z"]

def find_num(times):
    run = True
    loops = 0
    password = ""
    while run:
        num = random.randint(1, 9)
        str(num)
        password = password.join(num)
        if(loops == num_val):
            run = False
        else:
            loops = loops + 1
    return password
        
        

num_pass = find_num(num_val)
print(num_pass)
quitText = input("Do you wanna quit?(y/n)")

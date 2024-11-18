import random

def guesser(n):
    total_dots = 0
    dots_in_circle = 0
    
    for i in range(0, n):
        X = random.uniform(0, 1)
        Y = random.uniform(0, 1)
        plot = X**2 + Y**2
        
        if (plot <= 1):
          dots_in_circle += 1
          
        total_dots += 1
            
    return(4 * (dots_in_circle/total_dots))
     
num = int(input())
print(guesser(num))
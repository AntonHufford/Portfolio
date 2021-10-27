#monte carlo pi calculation. a unit circle is inscribed in a square. 
#random points are generated, the ratio of which fall in or out of the circle eventually converge to pi/4

inside = 0
total = 0
i = 0

import math
import random

iterations = int(input("How many iterations? "))

while i < iterations:
    
    x = round(random.uniform(0, 1), 2)
    y = round(random.uniform(0, 1), 2)
    distance = round(math.sqrt(x**2 + y**2), 2)
    i += 1

    if distance < 1:
        inside += 1
        total += 1
    else:
        total +=1

    pi = 4 * (inside / total)
    if i == iterations:
        print(pi)
        again = str(input("Another set of iterations? y/n: "))
        
        if again == "y":
            i = 0
            
        
   
        




    

    
  
    



          

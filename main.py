def factOrSum(x , y):
    if y == "factorial":
        total = 1
    
    
        for i in range (1, x + 1):
            total = total * i 
   
        return total
    else:

        total = 0

        for i in range (0, x ):
            total = total + i

        return total

print (factOrSum(10, "sum")) 
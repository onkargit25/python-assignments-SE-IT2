print("pROGRAM TO PRINT PRIME NUMBERS IN GIVEN RANGE")

max = int(input("Enter the higher limit"))

if max == 2:
    list_of_primes = [2]
    
if max > 2:
    list_of_primes = [2, 3]

for i in range (3, max + 1):
    is_prime = True
    
    for j in list_of_primes:
        if (i  % j ) == 0:
            is_prime = False
            break
    
    if is_prime:
        list_of_primes.append(i)
        
        
print(list_of_primes)

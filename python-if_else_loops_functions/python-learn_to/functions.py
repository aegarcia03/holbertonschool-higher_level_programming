# Solve for x
# x + 4 = 9 
# X will always be the 1st value received and will only deal with the addtion 

# Receive the string and split into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    # Convert the result into a string and join it to the string "x ="
    return "x = " + str(num2 - num1)
#print
print(solve_eq("x + 4 = 9"))

# Solve for x
# 4 + x = 9 

def solve_equ(equation):
    num1, add, x, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)

print(solve_equ("4 + x = 9"))

# mult and div 
def mult_div(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_div(5, 4)

print("5 * 4 = ", mult)
print("5 / 4 = ", divide)

# Return a list of prime numbers
# A prime can only be divided by 1 and itself
# 5 is a prime 1 and 5 = positive factor
# 6 is not a prime because it can be divided by 1, 2 ,3 and 6

# input max prime
# use a for loop and check if modules == 0 True

def is_prime(num):
    # a loop from 2 to the max num
    for i in range(2, num):
        if (num % i) == 0:
            return False
    
    return True

def getprime(max_number):
    
    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    
    return list_of_primes

max_num_to_check = int(input("Search for primes up to: "))

list_of_primes = getprime(max_num_to_check)

for prime in list_of_primes:
    print(prime)

# if the number of arguments is unknown
# I have to type *args

def sumAll(*args):3
    sum = 0

    for i in args:
        sum += i
    
    return sum

print("Sum: ", sumAll(1,2,47,9,20))
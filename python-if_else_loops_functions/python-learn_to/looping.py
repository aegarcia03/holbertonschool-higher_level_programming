# for loop i do know how many loops 
# print odds
for i in range (0, 21):
    if (i % 2) != 0:
        print("i = ", i)

# print floats
your_float = input("Enter a float: ")

your_float = float(your_float)
print("Round to 2 decimals : {:.2f}".format(your_float))

# while loop when i do not know how many times i have to use the loop
# I need to increase i 

import random

random_num = random.randrange(1, 51)

i = 1

while (i != random_num):
    i += 1

print("\nThe random value is: ", random_num)

# while loop, break, continue

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue

    if i == 15:
        break

    print("Odd: ", i)

    i += 1

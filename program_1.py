
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.

import  random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    numba1 = random.randint(1,6)
    numba2 = random.randint(1,6)
    return numba1 + numba2


# Mainline that calls the randDice function 100 times
total = 0
for i in range(100):
    total += randDice()

# Calculate the average and round it to 0.01
average = total / 100
print(f"Average of 100 rolls: {average:.2f}")

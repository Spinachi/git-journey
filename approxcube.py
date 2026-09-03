cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guess = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guess +=1

if abs(guess**3 - cube) >= epsilon:
    print("We could not find out the cube of ", cube)
else:
    print(guess, "is close to the cube root of cube", cube, ". It took", num_guess , "number of guesses.")   
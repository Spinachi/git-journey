#bisection sort works on nnumber when x>1 time complextity of O log 2  base n
cube = 0.3
epsilon = 0.1
number_guess = 0
low = 0
high = cube
if cube > 0 and cube < 1 :
    low = 0
    high = 1
guess = abs((low + high)/2.0)

while(abs(guess**3-abs(cube))>= epsilon and guess <= abs(cube)):
    if guess**3 < abs(cube):
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0        
    number_guess+=1
if cube < 0:
    guess = -guess    

print('number_guess',number_guess)
print(guess, "is close to the cube", cube)

import random

number = random.randrange(100)
for i in range(3):
    try:
        user = int(input('guess: '))
    except ValueError:
        print ('must be int')
        continue
    if user == number:
        print ('bravo')
        break
    elif user < number:
        print ('greater')
    else:
        print ('lesser')
print ('it was: %d' % number)

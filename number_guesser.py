import random

# r = random.randrange(-5, 11)
# r = random.randint(-5, 11)  # To get 11

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number, larger than Zero next time')
        quit()
else:
    print('Please type a number, next time')
    quit()

random_no = random.randint(0, top_of_range)

quesses = 0
while True:
    quesses += 1
    user_guess = input('Guess a number: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number, next time')
        continue

    # if user_guess == random_no:
    #     print("Yeah! You got it '" + str(user_guess)  + "' correctly")
    #     break
    # else:
    #     if user_guess > random_no:
    #          print('You were above the number')
    #     else:
    #         print('You were below the number')

    if user_guess == random_no:
        print("Yeah! You got it '" + str(user_guess)  + "' correctly")
        break
    elif user_guess > random_no:
        print('You were above the number')
    else:
        print('You were below the number')



print('You got it in', quesses, 'quess')
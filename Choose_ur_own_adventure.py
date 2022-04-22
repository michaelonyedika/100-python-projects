name = input('What is your name? ')


while True:
    x = input('Do you want to play the Adventure Game? [Yes(y)/No(n)] or q to quit: ').lower()

    if x == 'q' or x == 'quit':
        print('Good Bye. See you next time:)')
        quit()

    if x == 'yes' or x == 'y':
        break
    elif x == 'no' or x == 'n':
        print('Good Bye. See you next time:)')
        quit()
    else:
        print('Invalid input, Try again')
        continue

print('Yes', name, 'lets play the Adventure Game')


while True:
    user_input = input('The road you are on have come to an end. You can go left or right [left(l)/right(r)]: ' ).lower()

    if user_input == 'left' or user_input == 'l':
        while True:
            user_input = input('Here is a river you can swim across or walk round it. Type [swim(s)/walk(w)]: ').lower()
            if user_input == 'swim' or user_input == 's':
                print('You swam an got eaten by Alligator')
                print('You lose! Try again')
                quit()
            elif user_input == 'walk' or user_input == 'w':
                print('You walk until you run out of energy an died')
                print('You lose! Try again')
                quit()
            else:
                print('Invalid input, Try again')
                continue
    elif user_input == 'right' or user_input == 'r':
        while True:
            user_input = input('You come to a bride do you want to cross or go back home. [cross(c)/back(b)]: ').lower()
            if user_input == 'back' or user_input == 'b':
                print('You lose! Try again')
                quit()
            elif user_input == 'cross' or user_input == 'c':
                while True:
                    user_input = input('You met strangers do you want to talk to them or ignore them? '
                                       '[Talk(t)/Ignore(i)]: ').lower()
                    if user_input == 'ignore' or user_input == 'i':
                        print('You lose. Try again')
                        quit()
                    elif user_input == 'talk' or user_input == 't':
                        print('You talk to them and they gave you Gold. You Won! Congratulation')
                        quit()
                    else:
                        print('Invalid input, Try again')
                        continue
            else:
                print('Invalid input, Try again')
                continue
    else:
        print('Invalid input, Try again')
        continue


# print('Thank you for', name, 'for trying.')
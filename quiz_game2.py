welcome_msg = input('Welcome, do you want to play '
                    'the Quiz Game? (Yes/No): ').lower()

if welcome_msg != 'yes':
    quit()

print("The Quiz Game will ask you some basic computer "
      "science questions. \n Let's do it!")

score = 0
answer = input('What does CPU stand for? ').lower()
if answer == 'central processing unit':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer')

answer = input('What does PSU stand for? ').lower()
if answer == 'power supply':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer')

answer = input('What does GPU stand for? ').lower()
if answer == 'graphic processing unit':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer')

answer = input('What does RAM stand for? ').lower()
if answer == 'random access memory':
    print('Correct answer!')
    score += 1
else:
    print('Wrong answer')

print('You got', score, 'question(s) correctly')
print('You got', str(int(score / 4 * 100)) + '%')


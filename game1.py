import random 


def gamewin(comp, you):
    # if two values are equal declare a tie
    if comp == you:
        return None
    # check for all possiblities
    elif comp == 'Rock':
        if you == 'Paper':
            return False
        elif you == 'Scissor':
            return True
    elif comp == 'Paper':
        if you == 'Rock':
            return False
        elif you == 'Scissor':
            return True
    elif comp == 'Scissor':
        if you == 'Paper':
            return False
        elif you == 'Rock':
            return True

print('Comp Turn: Rock(Rock),Paper(Paper) or Scissor(Scissor) ?')
randno = random.randint(1, 3)

if randno == 1:
    comp = 'Rock'
elif randno == 2:
    comp = 'Paper'
elif randno == 3:
    comp = 'Scissor'
you=input('Your Turn: Rock(Rock),Paper(Paper) or Scissor(Scissor) ?')

a=gamewin(comp, you)

print(f'Computer choose {comp}')
print(f'You choose {you}')

if a==None:
    print('the game is a tie')
elif a:
    print('You Won')
else:
    print('You Lose')


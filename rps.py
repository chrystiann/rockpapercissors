import random
# importar esse arquivo primeiro
while True:
    print('Make your choice:')
    choice = str(input())
    choice = choice.lower()

    print("My choice is", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)
# statament if/elif/else para poder escolher
    print("Computer choice is", computer_choice)
    if choice in choices:
       # computer choice aq primeiro
        if choice == computer_choice:
            print('it is a tie')
        if choice == 'rock':
            if computer_choice == 'paper':
                print('you lose, sorry :(')
            elif computer_choice == 'scissors':
                print('You win!!!!! congrats :)')
        if choice == 'paper':
            if computer_choice == 'scissors':
                print('you lose, sorry :(')
            elif computer_choice == 'rock':
                print('You win!!!!! congrats :)')
        if choice == 'scissors':
            if computer_choice == 'rock':
                print('you lose, sorry :(')
            elif computer_choice == 'paper':
                print('You win!!!!! congrats :)')
    else:
        print('invalid choice, try again')
# imprimir os resultados da partida
    print()

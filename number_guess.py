import random

# compare input with random number
def compare_num(r):
    guess_num = int(input("Enter the guess : "))
    if guess_num == r:
        print("The number was guessed correctly") 
        new_game()       
    else:
        if guess_num > r:
            print("The number is smaller than the guess")
        else:
            print("The number is larger than the guess")
        compare_num(r)
        
# initialise a new game with a new random number
def new_game():
    game_start_check = (input("Start game (Y/N) : "))
    if game_start_check == 'Y':
        random_num = random.getrandbits(16) # random 16 bit number
        compare_num(random_num)    

new_game()
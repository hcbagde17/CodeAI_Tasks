import random
def read_file_to_list(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()  # Read all lines into a list
    # Optionally strip newline characters
    lines = [line.strip() for line in lines]
    return lines
def secret_f(lst):
    return random.choice(lst)
my_lst = read_file_to_list('')
secret=secret_f(my_lst)
def chk_guess(guess,secret):
    guess = guess.lower()
    if guess==secret:
        return 1
    else:
        for x,y in zip(guess,secret):
            if x == y:
                print("🟩", x, end=" ")
            elif x in secret:
                print("🟨", x, end=" ")
            else:
                print("⬛", x, end=" ")
            print()
        return 0
i=0
while i<6:
    gs = input("Enter your guess:")
    if len(gs)!=5 or not(gs.isalpha()) or gs not in my_lst:
        print("Enter your guess again with only 5 letters/no special characters/from the list!")
        continue
    else:
        i+=1
    trk = chk_guess(gs,secret)
    if trk==1:
        print("You guessed it right! You win!")
        break
else:
    print("You loose try again!")



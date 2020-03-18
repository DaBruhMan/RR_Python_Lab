print (" guess a number between 1-10 you have 4 guesses")

secret_number = 6
guess_count = 0
guess_limit = 4
out_of_guesses = False
guess= float(input("Enter guess:"))

while guess != secret_number and not (out_of_guesses):
    if guess_count<guess_limit:
        guess = float(input("Enter guess:"))
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
        print("Ha you are bad get a life you BUM")
else:
        print(" You are goated on the sticks WOW")
        
print("bye")
myFinalResponse =(input("Enter response:"))

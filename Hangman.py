
#Step 2
#Guessing a random word
import random
import word_list
import design
chosen_word = random.choice(word_list.word_list)

#Testing code
print(design.logo)
print(f'Pssst, the solution is {chosen_word}.')

#Creating a list of blanks "_" named display as same length as chosen_word
display=[]
for i in chosen_word:
  display+="_"
#Replacing the blank if the guess is right on the same position of correct guessed position
length=len(chosen_word)
p=0              # It determines how many times the while loop needs to be repeated
life=7           # Life of game
while p<length and life>0:
    guess = input("Guess a letter: ").lower()
    n=0
    q=0
    for letter in chosen_word:
        n+=1
        if life>0:
            if letter == guess:
                p+=1
                q+=1
                display[n-1]=guess
    if q>0:
        print(f'You guessed the letter {guess} is correct :)')
    elif q==0:
        life-=1
        print(f'Your guess was wrong, now you have left with {life} lifes.\n{design.stages[life]}')
    print(display)
if life==0:
    print("You lose:(")
else:
    print("You Won!!!")
    
    
    



import random
print("welcome to hangman")
wordlist=["python","laptop","programming","sunflower","watermelon","emerald","dress","beautiful","oxygen","cellphone","Lip","variable"]
randomword=random.choice(wordlist)
for i in randomword:
    print("Length of the word is",len(randomword))
    break
def hangman(wrong):
    if wrong==0:
        print("6 chance left")
        print("_")
        print("     |")
        print("     |")
        print("     |")
        print("    ==")  
    elif wrong==1:
        print("5 chance left")
        print("_")
        print("  O  |")
        print("     |")
        print("     |")
        print("    ==")  
    elif wrong==2:
        print("4 chance left")
        print("_")
        print("  O  |")
        print("  |  |")
        print("     |")
        print("    ==")  
    elif wrong==3:
        print("3 chance left")
        print("_")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ==")  
    elif wrong==4:
        print(" only 2 chance left")
        print("__")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ==")  
    elif wrong==5:
        print("This is your last chance!..")
        print("_ ")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ==") 
    elif wrong==6:
        print("_ ")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ==") 
        print("you lose:(")
        print("Your word was","-",randomword)
def correct(guessedletters):
    count=0
    correct=0
    for i in randomword:
        print("_",end=" ")
        if i in guessedletters:
            print(randomword[count],end=" ")
            correct+=1
        else:
            pass
        count+=1
    return correct
# def prints():
#     for i in randomword:
#         pass
len_word=len(randomword)
wrong_guessed=0
guessed_index=0
current_letter=[]
right_guess=0
while wrong_guessed!=6 and right_guess!=len_word:
    print("\n")
    user_guess=input("enter guessed letter:")
    if user_guess in randomword:
        guessed_index+=1
        current_letter.append(user_guess)
        right_guess=correct(current_letter)
        # prints()
        if user_guess in randomword:
            print("=you win")
        else:
            print("you lose")
    else:
        wrong_guessed+=1
        current_letter.append(user_guess)
        hangman(wrong_guessed)
        right_guess=correct(current_letter)
    print()
print("Game over:")
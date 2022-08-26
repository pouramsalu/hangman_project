import random
# from worrd import word_list
word_list = ["pizza", "book", "apple", "mango", "orange", "python", "project","software","classroom","window","door","fish"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.lower()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:


                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried ", guess, "!")
            elif guess != word:
                print(guess, " is not in that word :")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
            
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("*Congratulatuon* You won!!")
    else:
        print("I'm sorry, you lose the game. The word was is"+' ' + word + ". good luck next time!")

def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     /|\
                   |      |
                   |     / \
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     /|\
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     /|\
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     /|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]

    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)
main()




# import random
# print("You are in  Hangman World")
# def hangman():
#     list1=["salu","python","disco","riamroi","manipur","butterflies","hangman","project"]
#     word=random.choice(list1)
#     guessed_letter=6
#     str=''
#     v=set('abcdefghijklmnopqrstuvwxyz')
#     while len(word)>0:
#         word_var=""
#         for letter in word:
#             if letter in str:
#                 word_var=word_var+letter
#             else:
#                 word_var=word_var+"_ "
#         if word_var==word:
#             print(word_var)
#             print("Wow  you won 🥳")
#             break
#         print("guess the word",word_var,)
#         guess=input("enter the word...")
#         if guess in v:
#             str=str+guess
#         else:
#             print("enter valid character")
#             guess=input()
#         if guess not in word:
#             if guessed_letter==6:
#                 print("  __")
#                 print("       |")
#                 print("       |")
#                 print("       |")
#                 print(" =======")
#             if guessed_letter==5:
#                 print("o___")
#                 print("     |")
#                 print("     |")
#                 print(" =====")
#             if guessed_letter ==4:
#                 print(" o__")
#                 print(" |   |")
#                 print("     |")
#                 print(" =====")
#             if guessed_letter ==3:
#                 print("3 time is left ")
#                 print(" o___")
#                 print("/|    |")
#                 print("      |")
#                 print(" ======")
#             if guessed_letter ==2:
#                 print("2 time is left choose right")
#                 print(" o___")
#                 print("/|\   |")
#                 print("      |")
#                 print(" =======")
#             if guessed_letter ==1:
#                 print("only one trun is left):!!")
#                 print(" o___")
#                 print("/|\   |")
#                 print("/     |")
#                 print(" =======")
#             if guessed_letter ==0:
#                 print("ooppssss sorry you loss")
#                 print(" o___")
#                 print("/|\    |")
#                 print("/ \    |")
#                 print(" =======")
#                 break
#             guessed_letter=guessed_letter-1
# name=input("enter your name__(:")
# print("WELCOME To Hangman Game ",name)
# hangman()


import random

#  Initiates the functions
def hangman():
    game(main_menu(choose_language()))

def choose_language():
    language = input("English or Spanish :").title()
    return language

#  Initiate values for the secret word and greets the user
def main_menu(language):
    english_words = ['cat', 'dog', 'everything', 'some', 'another', 'cuddly', 'pretty', 'penny', 'desk', 'fridge']
    spanish_words = ['perro', 'frijole', 'escritorio', 'gato', 'termo', 'botella', 'escoba', 'pescado', 'ayuda']
    if language == "English":
        user_name = input("Enter your name: ")
        word_list = english_words
        secret_word = word_list[random.randrange(0, len(word_list))]
        print("Welcome " + user_name + ".")
        return secret_word
    elif language == "Spanish":
        word_list = spanish_words
        secret_word = word_list[random.randrange(0, len(word_list))]
        user_name = input("Escribe su nombre: ")
        print("Bienvenido/a " + user_name + ".")
        return secret_word
    else:
        print("Try writing it again please")
        game(main_menu())


#  Evaluates the secret word vs guesses
def game(secret_word):
    guesses_list = list(len(secret_word)* "_")
    secret_word_list = list(secret_word)
    lives = 10

    while lives > 0 and guesses_list != secret_word_list:
        print(guesses_list)
        print("Lives = " + str(lives))
        guess = input("Enter a letter to guess \n:")
        result = secret_word.find(guess)

        if result == -1:
            print("The letter ' " + guess + " ' is not in the word")
            lives -= 1
        else:
            result_list = [result]
            while result != -1:
                result = secret_word.find(guess, result + 1)
                if result == -1:
                    break
                else:
                    result_list.append(result)

            num_occurrences = len(result_list)
            print("\nThere are " + str(num_occurrences) + " " + guess + "'s in the word")

            for i in range(0, len(result_list)):
                guesses_list[result_list[i]] = guess
    if lives == 0:
        print("Almost, better luck next time!")
    elif lives > 0 and guesses_list == secret_word_list:
        print("Noiiicee cool cool cool cool you win!")
    else:
        print("Weird you shouldn't be here....")


hangman()

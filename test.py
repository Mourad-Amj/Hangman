import random    

possible_words = ['becode', 'learning', 'mathematics', 'sessions']
word_to_find = list(random.choice(possible_words))
correctly_guessed_letters= ["_"]*len(word_to_find)

print(possible_words)
print(word_to_find)
print(correctly_guessed_letters)
guess=input("Enter one letter : ")

if guess.isalpha() is False:
        print("No special characters allowed! Only enter a letter, please : ")
elif len(guess)>1:
        print("No more than one characters! Only enter a letter, please : ")

for letter in range(len(word_to_find)):
    if word_to_find[letter] == guess:
        correctly_guessed_letters[letter] = guess
    elif correctly_guessed_letters[letter] == guess:
        correctly_guessed_letters[letter] = word_to_find[letter]

print(correctly_guessed_letters)
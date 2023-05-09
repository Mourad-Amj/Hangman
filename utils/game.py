import random

class hangman:

    def __init__(self) :
        """
        Constructor method that initializes the attributes of the Hangman class.
        """
        self.lives=5
        self.turn_count=1
        self.error_count=0

        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        # initializes the correctly guessed letters list with the appropriate number of underscores
        self.correctly_guessed_letters= ["_"]*len(self.word_to_find)
        self.wrongly_guessed_letters=[]

    def verification(self, guess):
        """
        Method that checks if the given letter is in the word to be found.
        If the letter is in the word, it updates the correctly guessed letters list.
        If the letter is not in the word, it updates the wrongly guessed letters list.
        :param guess: A string representing the letter that the user has guessed.
        :return: A boolean indicating whether the guess was correct or not.
        """
        if (guess in self.word_to_find):
            for letter in range(len(self.word_to_find)):
                if self.word_to_find[letter] == guess:
                    self.correctly_guessed_letters[letter] = guess
                elif self.correctly_guessed_letters[letter] == guess:
                    self.correctly_guessed_letters[letter] = self.word_to_find[letter]
            return True
        else:
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
            self.error_count +=1
            return False

    def play(self):
        """
        Method that gets user input for a letter guess, and calls the verification method to check if the guess is correct.
        :return: A string indicating whether the guess was good or bad.
        """
        print(self.correctly_guessed_letters)        
        guess=input("Enter one letter : ")
        if guess.isalpha() is False:
            return print("No special characters allowed! Only enter a letter, please : ")
        elif len(guess)>1:
            return print("No more than one characters! Only enter a letter, please : ")
        elif self.verification(guess) == True:
            return print("good guess ")
        else:
            return print("bad guess ")

    def start_game(self):
        """
        Method that starts the game and runs a loop until the game is over.
        """
        print("Start game")
        while(self.lives != 0 and "_" in self.correctly_guessed_letters):
            self.play()
            print(self.correctly_guessed_letters)
            print(f"Turn :  {self.turn_count}")
            print(f"Life :  {self.lives}")
            print(f"Error_counat :  {self.error_count}")
            self.turn_count +=1
            print("New turn ! ")
            print(f"Turn :  {self.turn_count}")
        if self.lives != 0:
            self.well_played()
        else:
            self.game_over()

    def game_over(self):
        """
        Method that prints a game over message.
        """        
        print("GAME OVER . . . ")

    def well_played(self):
        """
        Method that prints a success message with the word found and the number of turns and errors.
        """
        print(f"You found the word: '{''.join(self.word_to_find)}' in {self.turn_count} turns with {self.error_count} errors!")
        print("Well played")

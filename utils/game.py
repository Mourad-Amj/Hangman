import random

class Hangman:

    lives=5
    turn_count=1
    error_count=0
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self) :
        """
        Constructor method that initializes the attributes of the Hangman class.
        """
        self.word_to_find = list(random.choice(self.possible_words))
        # initializes the correctly guessed letters list with the appropriate number of underscores
        self.correctly_guessed_letters= ["_"]*len(self.word_to_find)
        self.wrongly_guessed_letters=[]

    def verification(self, guess):
        """
        Method that checks if the given letter is in the word to be found.
        If the letter is in the word, it updates the correctly guessed letters list.
        If the letter is not in the word, it updates the wrongly guessed letters list.
        A boolean indicating whether the guess was correct or not.
        """
        if (guess in self.word_to_find):
            for letter in range(len(self.word_to_find)):
                if self.word_to_find[letter] == guess:
                    self.correctly_guessed_letters[letter] = guess
            return True
        else:
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
            self.error_count +=1
            return False

    def play(self):
        """
        Method that gets user input for a letter call "guess", and calls the verification method to check if the guess is correct.
        A Bool indicating whether the guess was good or bad.
        """       
        guess=input("Enter one letter : ").lower()
        if guess.isalpha() is False:
            return print("No special characters allowed! Only enter a letter, please : ")
        elif len(guess)>1:
            return print("No more than one characters! Only enter a letter, please : ")
        elif self.verification(guess) == True:
            return print("  Good guess ")
        else:
            return print("  Bad guess ")

    def start_game(self):
        """
        Method that starts the game and runs a loop until the game is over.
        """
        print("*** START GAME : ***")
        print(" This is the word to find : ")
        print(self.correctly_guessed_letters)
        self.print_hangman()
        while(self.lives != 0 and "_" in self.correctly_guessed_letters):
            self.play()
            
            print(f"  Turn :  {self.turn_count}")
            print(f"  Life :  {self.lives}")
            print(f"  Error count :  {self.error_count}")
            print(f"  Wrong guesses :  {self.wrongly_guessed_letters}")
            self.turn_count +=1
            print("***** New turn ! ****")
            print(f"  Turn :  {self.turn_count}")
            print(self.correctly_guessed_letters)
        if self.lives != 0:
            self.well_played()
        else:
            self.game_over()

    def game_over(self):
        """
        Method that prints a "Game over" message.
        """        
        print("*** GAME OVER . . . ***")

    def well_played(self):
        """
        Method that prints a success message with the word found and the number of turns and errors.
        """
        print(f"You found the word: '{''.join(self.word_to_find)}' in {self.turn_count} turns with {self.error_count} errors!")
        print(" *** Well played !! ***")

    def print_hangman(self):
        """
        Method that prints a Hangman.
        """
        drawing_hangman = ["    +---+","    |   |","    O   |","   /|\\  |","   / \\  |","        |","  ========",]
        for line in drawing_hangman:
            print(line)

player = Hangman()
player.start_game()
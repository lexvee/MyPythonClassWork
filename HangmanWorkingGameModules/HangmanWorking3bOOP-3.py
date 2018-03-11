from HangmanWorking3bOOP import FileAction as fa
# if impoting the method directly use - from HangmanWorking3bOOP.FileAction import pickword

class GameProcess():   

    word = fa.pickword("words.txt")
    length = len(word)
    max_attempts = length + 1
    available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

    def _get_guess():
        ''' gets the guessed letter from player '''
        guess = input("\n\n  Please guess a letter: ").lower()
        return guess
    
    def _del_alphabeth(alphabeth,choice_range):
        if alphabeth in choice_range:
           letters_remaining = str.replace(choice_range,alphabeth,"_ ")
           return letters_remaining

    def _progress_so_far(word, guessed_letters):
        newstring = []
        for index in range(len(word)):
            letters = word[index]
            if letters in guessed_letters:
                newstring.append(letters)
            else:
                newstring.append("_")
        return newstring

    def _game_intro(max_attempts, length, available_letters):
        print ("  I am looking for a word that contains", length, " letters")
        print ("  ---------------")
        print ("  You have", max_attempts, "guesses to make.")
        print ("  Available letters: ", available_letters)
        return None

        

    @classmethod
    def eval_guess(self):

        ''' Gets guess from player,checks if 

        word contains the guess and print progress made

        so far, else return failure report '''
        self._game_intro(self.max_attempts, self.available_letters, self.length)
        
        guess=self._get_guess()
        ## word=self.word
        ## max_attempt=self.length+1
        available_letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        guessed_letters = []
        newstring = []
        correct_guesses = 0
        wrong_guesses = 0

        while True and self.max_attempts >= 1:
            while (guess == '' or len(guess) !=1) : 
                print ("  Guess must be a single letter !")
                guess = self._get_guess()
            if guess in guessed_letters:
                print (" This letter has been guessed!")
                guess = self._get_guess()                
            else:
                guessed_letters.append(guess)
                if guess not in self.word:
                    print ("   Opps!", guess, "is not in the word")
                    print ("   -----------------")
                    self.max_attempts -= 1  
                    print ("  you have ", self.max_attempts, "attempts left")
                    available_letters = self._del_alphabeth(guess,available_letters)
                    print ("  Available letters: ", available_letters)
                    wrong_guesses += 1
                    guess = self._get_guess()
                else:  
                    print ("   Good guess: '", guess, "' appeared", self.word.count(guess), "times")
                    print ("   progress so far: ", self._progress_so_far(self.word,guessed_letters))
                    available_letters = self._del_alphabeth(guess,available_letters)
                    print ("\n  Available Letters:  ", available_letters)

                    correct_guesses += self.word.count(guess) 
                    if  correct_guesses == self.length:
                        print (" \n\n\t\t Great Job! the word is ", self.word.upper(), "!!!")
                        print ("\t\t wrong guesses: ",wrong_guesses)
                        break
                    else:
                        guess = self._get_guess()

        else:

            print ("\n\t ************************************")

            print ("\t\t\t\tGame Over!".upper()) # terminate the game

            print ("\t ************************************")

            print ("\n\t\t The word is ", self.word.upper())

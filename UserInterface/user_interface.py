

class ui:

    def mainMenu(self):
        print('play')
        print('add')
        print('x')

    def mainCommand(self):
        command = input('Enter command:\n >>> ')
        command = command.split(' ')
        return command

    def saveSentenceCommand(self):
        command = input('Enter sentence \n > ')
        return command

    def addSentence(self,controller):
        while True:
            try:
                command = self.saveSentenceCommand()
                controller.addSentence(command)
                print('Sentece succesfully saved')
                return 0
            except ValueError as error:
                print(error)

    def getUserGuess(self):
        command = input('Enter your guess\n >')
        command = command.split(' ')
        return  command

    def wasUsed(self,guess,existing_guess):
        '''
        This function checks if a guess
        was used before
        '''
        for ex in existing_guess:
            if ex.lower() == guess.lower():
                return 1
        return 0

    def format(self,sentence,index,hangman):
        print('Sentence is: ')
        print(sentence)
        print('Hangman is: '+hangman[:index])

    def gamePlay(self,controller):
        print('This is your sentence')
        sentence = controller.RandomSentence()
        print(sentence)
        hangman = 'hangman'
        index = 0
        existing_guesses = []

        while index < 7:
            try:
                guess = self.getUserGuess()
                if len(guess) != 1:
                    raise ValueError('Invalid guess')
                if self.wasUsed(guess[0],existing_guesses) == 1:
                    raise ValueError('You already used this letter')
                existing_guesses.append(guess[0].lower())
                if controller.isInSentence(sentence,guess[0].lower()) == 0:
                    index += 1
                controller.modifyShow(sentence,guess[0])
                if index == 7:
                    print('You lose..')
                    print('Sentence was:')
                    print(sentence.senr())
                    return 0
                if controller.isWon(sentence) == 1:
                    print('You won')
                    print(sentence)
                    return 0
                self.format(sentence,index,hangman)
            except ValueError as error:
                print(error)

    def app_exe(self,controller):
        '''
        Main Menu for the app
        '''
        while True:
            try:
                self.mainMenu()
                command  = self.mainCommand()
                if len(command) == 1:
                    if command[0].lower() == 'play':
                        self.gamePlay(controller)
                    elif command[0].lower() == 'add':
                        self.addSentence(controller)
                    elif command[0].lower() == 'x':
                        return 0
                    elif command[0].lower() == 'a':
                         for sent in controller._repo.getAll():
                             print(sent.senr())
                    else:
                        raise ValueError('Invalid command')
                else:
                    raise  ValueError('Invalid command')
            except ValueError as error:
                print(error)
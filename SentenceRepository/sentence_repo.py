
from ClassSentence.sentence_class import *

class repostitory_sentence:

    def __init__(self):
        '''
        Repository used to store sentences
        during game play.
        '''
        self._sentences = []
        self.__loadFile()

    def __saveFile(self):
        try:
            file = open('sentences.txt','w')
            for sentence in self._sentences:
                words = sentence._sentence.split(' ')
                for index in range(len(words)):
                    if index == len(words)-1:
                        file.write(words[index]+'\n')
                    else:
                        file.write(words[index]+',')
            file.close()
        except IOError:
            raise ValueError('Can not save file')
        except EOFError:
            raise  ValueError('Can not save file')

    def __loadFile(self):
        '''
        Loads some prepared sentences from a text
        file and adds them to the list of av. sent.
        '''
        try:
            file = open('sentences.txt','r')
            row = file.readline().strip()
            while len(row) != 0:
                row = row.split(',')
                prop = ''
                for index in range(len(row)):
                    if '\n' in row[index]:
                        r = row[index]
                        r = r[:-1]
                        prop += ' '+r
                    else:
                        prop += row[index]+' '
                prop = prop[:-1]

                self._sentences.append(Sentence(prop))
                row = file.readline().strip()
            file.close()
        except IOError:
            raise ValueError('Can not load sentences')
        except EOFError:
            raise ValueError('Can not load file')


    def validateSentence(self,prop):
        '''
        Function which validates a possible
        sentence.
        Checks if :
             o it has at least one word
             o each word has at least 3
             letters
             o the sentence is unique
             (it is stored only once)
        Returns 1 if valid and 0 oth.
        '''
        words = prop.split(' ')
        if len(words) <= 1:
            return 0

        for word in words:
            if len(word) < 3:
                return 0

        for element in self._sentences:
            if element._sentence.lower() == prop.lower():
                return 0
        return 1

    def addSentence(self,prop):
        '''
        Return 1 if sentence was added
        , 0 otherwise
        '''
        if self.validateSentence(prop) == 0:
            return 0

        self._sentences.append(Sentence(prop))
        self.__saveFile()
        return 1

    def getAll(self):
        return self._sentences
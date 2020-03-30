
from random import choice
from SentenceRepository.sentence_repo import *

class SentenceController:
    def __init__(self,repository):
        self._repo = repository

    def RandomSentence(self):
        lenn = len(self._repo.getAll())
        lenn -= 1
        lst = []
        for i in range(lenn+1):
            lst.append(i)
        sentence_number = choice(lst)
        return self._repo._sentences[sentence_number]

    def addSentence(self,sentence):
        if self._repo.addSentence(sentence) == 0:
            raise ValueError('Make sure the sentence is valid and that \n it is unique')


    def isInSentence(self,sentence,letter):
        '''
        This function checks if a letter is
        in a given sentence, it returns 1 if
        it does and 0 otherwise.
        '''
        for el in sentence._sentence:
            if el.lower() == letter.lower():
                return 1

        return 0

    def modifyShow(self,sentence,letter):
        '''
        This function makes a letter from
        the sentence visible
        '''
        for index in range(len(sentence._sentence)):
            if sentence._sentence[index].lower() == letter.lower():
                sentence._reveal[index] = 1

    def isWon(self,sentence):
        '''
        Checks if the length of the sentence
        is equal to the sum of the elements
        of the _reveal param from sentence cls.
        '''
        for index in range(len(sentence._sentence)):
            if sentence._reveal[index] == 0:
                return 0
        return 1
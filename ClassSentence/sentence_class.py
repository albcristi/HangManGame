


class Sentence:
    def __init__(self,sentence):
        self._sentence = sentence
        self._reveal = []
        for i in range(len(sentence)):
            if self._sentence[i] == ' ':
                self._reveal.append(1)
            else:
                self._reveal.append(0)


        sent = self._sentence.split(' ')
        for word in sent:
            first_letter = word[0]
            last_letter = word[-1]
            for i in range(len(self._sentence)):
                if self._sentence[i].lower() == first_letter.lower():
                    self._reveal[i] = 1
                if self._sentence[i].lower() == last_letter.lower():
                    self._reveal[i] = 1


    def __str__(self):
        hangman_style = ''
        for index in range(len(self._sentence)):
            if self._reveal[index] != 0:
                hangman_style = hangman_style + self._sentence[index]
            else:
                hangman_style += '|_|'

        return hangman_style


    def senr(self):
        return self._sentence
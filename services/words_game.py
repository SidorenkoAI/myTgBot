import requests
from googletrans import Translator
class wordGame:
    def __init__(self):
        self.word: str
        self.answer: list()
        self.counter = 0
    def getWord(self):
        word = requests.get('https://random-word-api.herokuapp.com/word').json()[0]
        translator = Translator()
        tr = translator.translate(text=word, dest='ru')
        self.word = tr.text
        self.answer = list('_' * len(self.word))
        return ' '.join(self.answer)

    def checkSymb(self, symb: str) -> str:
        indexes = [i for i in range(len(self.word)) if self.word[i] == symb]
        if indexes:
            for i in indexes:
               self.answer[i] = symb
            if '_' not in self.answer:
                return 'win'
            return ' '.join(self.answer)
        else:
            self.counter += 1
            if self.counter > len(HANGMAN) - 1:
                return False
            return HANGMAN[self.counter]
    def stop(self):
        self.counter = 0
        return self.word


HANGMAN = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |    |
         | 
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   
         |   
         |     
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |   
         |   
        ----------
        """
    )
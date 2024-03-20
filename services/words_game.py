import requests
from googletrans import Translator
import time
class wordGame:
    def __init__(self):
        self.word: str
        self.answer: list()
        self.counter = -1
        self.status = False
        self.usedSymbols = set()
    async def getWord(self):
        while True:
            word = requests.get('https://random-word-api.herokuapp.com/word').json()[0]
            translator = Translator()
            tr = translator.translate(text=word, dest='ru').text
            res = False
            for char in tr.lower():
                if char > 'а' and char < 'я':
                    res = True
            if res:
                break
            time.sleep(1)
        self.word = tr.lower()
        self.answer = list('_' * len(self.word))
        self.status = True
        self.usedSymbols = set()
        return ' '.join(self.answer)

    def checkSymb(self, symb: str) -> str:
        self.usedSymbols.add(symb)
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
    def getUsedSymbols(self)-> str:
        return ''.join(self.usedSymbols)
    def stop(self):
        self.counter = -1
        self.status = False
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
import requests

class Game():
    def __init__(self):
        self.deck_id: str
    async def shuffle(self, deck_count = 1):
        endPoint = f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}'
        res = requests.get(endPoint).json()
        self.deck_id = res['deck_id']

    async def getCard(self, count: int = 1) -> tuple[str, str]:
        endPoint = f'https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count={count}'
        res = requests.get(endPoint).json()
        return (res['cards'][0]['image'], res['cards'][0]['value'])
    def whoWin(self, userValue: str, botValue: str)-> str:
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
        if values.index(userValue) > values.index(botValue):
            return 'user'
        elif values.index(userValue) == values.index(botValue):
            return 'draw'
        else:
            return 'bot'
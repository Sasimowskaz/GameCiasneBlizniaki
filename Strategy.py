import random

class Strategy:

    def __init__(self, alphabet, strategy_place=None, strategy_letter=None):
        self.strategy_place = strategy_place
        self.strategy_letter = strategy_letter
        self.alphabet = alphabet
        self.places = 1
        self.chosen_letters = 0

    def choose_place(self):
        place = 0
        if self.strategy_place == 1: #losowy wybór miejsca z rozkładu jednostajnego
            place = random.randint(0, self.places)
        if self.strategy_place == 2: #wybór środkowego miejsca
            place = self.places // 2 +1
        if self.strategy_place == 3: #wybór zawsze tego samego miejsca
            place = 1
        self.places = self.places+1
        return place

    def choose_letter(self):
        pos = 0
        if self.strategy_letter == 1: #losowy wybór litery
            pos = random.randint(0, len(self.alphabet)-1)
        elif self.strategy_letter == 2: #wybór liter po kolei
            pos = self.chosen_letters % len(self.alphabet)
            self.chosen_letters = self.chosen_letters + 1
        letter = self.alphabet[pos]
        return letter

import random
import 

class Strategy:

    def __init__(self, alphabet, strategy_place=None, strategy_letter=None):
        self.strategy_place = strategy_place
        self.strategy_letter = strategy_letter
        self.alphabet = alphabet
        self.places = 1
        self.chosen_letters = 0

    def choose_place(self, twin_list):
        place = 0
        if self.strategy_place == 1: #losowy wybór miejsca z rozkładu jednostajnego
            place = random.randint(0, self.places)
        if self.strategy_place == 2: #wybór środkowego miejsca
            place = self.places // 2 +1
        if self.strategy_place == 3: #wybór miejsca tego samego miejsca, tzn. przedostatniego miejsca
            place = self.places - 1
        if self.strategy_place == 4: #wybór miejsca zmniejszajacego alfabet o 2 litery
            if twin_list[2] == twin_list[0] or twin_list[2]==twin_list[1]:
                place = 3
            else:
                place = 2
        self.places = self.places+1
        if self.strategy_place == 5: #wybieramy losowo spośród miejsc w które można wpisać najmniej liter nie tworząc ciasnego bliźniaka
            n = length(twin_list)
            n_l = [] #tablica gdzie wpisujemy pod indeksem i liczbę liters, których nie można wpisać w i-tą lukę
            max_index = [] #tu wpisujemy indeksy z dla których wartość n_l[i] jest równa max(n_l)
            for i in range(n+1):
                a = 0
                for j in self.alphabet:
                    twin_list[i] = j
                    is_twin = self.search_for_twins(twin_list, i)
                    if is_twin:
                        a = a + 1
                n_l.append(a)
            for i in n+1:
                if n_l[i] == max(n_l):
                    max_index.append(i)
            place = random.choice(max_index)
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

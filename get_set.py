class Card:
    def __init__(self, count, color, shape, fill):
        self.__count = count
        self.__color = color
        self.__shape = shape
        self.__fill = fill

    @property
    def count(self):
        return self.__count
    @property
    def color(self):
        return self.__color
    @property
    def shape(self):
        return self.__shape
    @property
    def fill(self):
        return self.__fill
    @property
    def value(self):
        return [self.__count, self.__color, self.__shape, self.__fill]

f = open("test", "r").read().split("}")
cards = []

for i in range(len(f)-2):
    token = 0
    value = []
    for j in range(len(f[i])):
        try:
            char = int(f[i][j])
            value.append(char)
        except:
            continue
    cards.append(Card(value[0], value[1], value[2], value[3]))


right_sets = []
currant_set =[]
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for c in range(j + 1, len(cards)):
            currant_set = [i, j, c]

            if (cards[i].count == cards[j].count and cards[i].count == cards[c].count) or (6 - cards[i].count - cards[j].count == cards[c].count):
                if (cards[i].color == cards[j].color and cards[i].color == cards[c].color) or (6 - cards[i].color - cards[j].color == cards[c].color):
                    if (cards[i].shape == cards[j].shape and cards[i].shape == cards[c].shape) or (6 - cards[i].shape - cards[j].shape == cards[c].shape):
                        if (cards[i].fill == cards[j].fill and cards[i].fill == cards[c].fill) or (6 - cards[i].fill - cards[j].fill == cards[c].fill):
                            right_sets.append(currant_set)
                continue

print(right_sets)
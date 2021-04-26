import random
cards = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
         "Kız":10,"Joker":10,"Papaz":10,
         "As":[1,11]}
deck= [x for x in cards]*4
random.shuffle(deck)
class Player():
    
    def __init__(self):
        self.sum = 0
        self.as_count = 0
        self.dont_count = 0
        self.cards = []
    
    def get_card(self, card):
        for i in cards:
            if i == card:
                value = cards[card]
        if str(value).isnumeric(): self.sum += value
        else: 
            self.as_count +=1
            self.dont_count +=1
        self.cards.append(card)
    def deal(self):
        if self.as_count>1:
            self.sum+= self.as_count-1
            self.as_count = 1
            self.deal()
        elif self.as_count == 1:
            if self.sum >10:
                self.sum+=1
            else: self.sum +=11
    def show(self):
        self.deneme()
        return self.sum
    def check(self):
        if self.show()>21: return False
        else: return True
    def deneme(self):
        self.sum = 0
        if self.dont_count!= self.as_count:
            self.as_count = self.dont_count
        if "As" in self.cards:
            temp = []
            for i in self.cards:
                if i != "As":
                    temp.append(i)
            for i in self.cards:
                if i == "As":
                    temp.append(i)
            self.cards.clear()
            for i in temp:
                self.cards.append(i)
                
        for i in self.cards:
            value = cards[i]
            if i != "As":
                self.sum += value
            else:
                self.deal()
winner = False
print("*"*10+"Blakcjack Oyununa Hoşgeldiniz"+"*"*10)
threshold = int(input("Kaç oyuncu oynayacak: "))
numberOfPlayers = 1 # oynayacak oyuncuları saymak için
winners = {}
while(threshold >= numberOfPlayers and not winner):
    oyuncu = Player()
    print("{}. oyuncu oynuyor".format(numberOfPlayers))
    cards_gamer = []
    while(True):
        choice = random.choice(deck)
        print("[1] ver")
        print("[2] pas")
        option = input("Lütfen bir seçenek giriniz: ")
        if option == "1":
            oyuncu.get_card(choice)
            cards_gamer.append(choice)
            print(cards_gamer)
            if not oyuncu.check():
                print(oyuncu.show())
                print("{}. oyuncu oyunu kaybetti".format(numberOfPlayers))
                numberOfPlayers+=1
                break
            elif oyuncu.show()== 21:
                winner = True
                print(oyuncu.show())
                print("{}. oyuncu oyunu kazandı".format(numberOfPlayers))
                break
        elif option == "2":
            print("{}. oyuncu {} puan yaptı".format(numberOfPlayers, oyuncu.show()))
            winners["{}. oyuncu".format(numberOfPlayers)] = oyuncu.show()
            numberOfPlayers+=1
            break
        else:
            print("***Geçersiz seçenek girdiniz***")

list_win = [winners[x] for x in winners]
last_win = []

def print_winners():
    for i in range(len(last_win)):
        if i == len(last_win)-1:
            print("{} {} puanla 1.liği paylaştı".format(last_win[-1],winners[last_win[-1]]))
        else:
            print(i+1, end=" ve ")

if len(list_win)>0:
    if not winner:
        if list_win.count(max(list_win))>1:
            for i in winners:
                if winners[i] == max(list_win):
                    last_win.append(i)
            print_winners()
        elif list_win.count(max(list_win)) == 1:
            for i in winners:
                if winners[i] == max(list_win):
                    last_win.append(i)
            print("{}. oyuncu {} puanla kazandı".format(last_win[0],winners[last_win[0]]))
elif not winner:
    print("Kazanan yok")
            
            


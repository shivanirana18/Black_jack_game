import random
suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,"Ten": 10,"Jack": 10,"Queen":10,"King":10, "Ace": 11}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        print(self.rank+" of "+self.suit)

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop() 

class Hand:
    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0
    def add_value(self,card):
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            if self.value > 21:
                self.value -= 10
                print("Ace card value adjusted to 1")
    
class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def show_some(player,dealer):
    print("Player cards are: ")
    print(" ")
    for i in player.card:
        print(i.rank+" of "+i.suit)
        
    print(f"Player cards total value is: {player.value}") 
    print(" ")   
    print("Dealer cards are: ")
    print(" ")
    print(dealer.card[0].rank+" of "+dealer.card[0].suit)
    
    print("One card hidden")
def show_full(player,dealer):
    print("Player cards are: ")  
    print(" ") 
    for i in player.card:
        print(i.rank+" of "+i.suit) 
        
    print(f"Player card total value is:{player.value}")   
    print(" ") 
    print("Dealer cards are: ")
    print(" ")
    for x in dealer.card:
        print(x.rank+" of "+x.suit)
        
    print(f"Dealer card total value is: {dealer.value}")   

def hit(deck,hand):
    hand.add_value(deck.deal())
                      

def hit_or_stand(deck,hand):
    global flag
    while True:
        option = input("Choose you want to hit or stand: ")
        if option.lower() == "hit" or option.lower() == "h":
            hit(deck,hand)
            show_some(player_hand,dealer_hand)
            return hand.value
            break
        elif option.lower() == "stand" or option.lower() == "s":
            flag += 1
            break
        else:
            continue
def take_bet(chip):
    while True:
        try:
            chip.bet = int(input("Enter amount you want to bet: "))  
        except ValueError:
            print("Please enter valid amount") 
            continue
        else:
            if chip.bet <= chip.total:
                return chip.bet
                break
            else:
                print(f"You have to bet amount less than or equal to your avaliable amountthat is {chip.total}")
                continue

                

flag1 = 0
while flag1 == 0:
    print("Initial amount to play game is 100 rs")
    chip = Chip()
    flag2 = 0
    while flag2 == 0:
        print(f"Amount with you is Rs {chip.total}")
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        deck.shuffle()
        
        take_bet(chip)

        player_hand.add_value(deck.deal())
        player_hand.add_value(deck.deal())
        dealer_hand.add_value(deck.deal())
        dealer_hand.add_value(deck.deal())

        
        show_some(player_hand,dealer_hand)

        flag = 0
        while flag == 0:
            while flag == 0:
                if player_hand.value == 21:
                    print(" ")
                    print("Black Jack")
                    print(" ")
                    chip.win_bet()
                    flag += 1
                elif player_hand.value > 21:
                    for x in player_hand.card:
                        if "Ace" in x.rank:
                            player_hand.value -= 10
                            print(" ")
                            print("Ace card value adjusted to 1")
                            print(" ")
                            flag += 1  
                        
                else:              
                    hit_or_stand(deck,player_hand)
                    if player_hand.value == 21:
                        print(" ")
                        print("Black Jack")
                        print(" ")
                        chip.win_bet()
                        flag += 1
                    elif player_hand.value > 21:
                        print(" ")
                        print("Player Bust")
                        print(" ")
                        chip.lose_bet()
                        flag += 1    

            if player_hand.value > 21:
                break
            elif player_hand.value == 21:
                break    
            else:
                while dealer_hand.value < 17:
                    hit(deck,dealer_hand)

            show_full(player_hand,dealer_hand)
            if dealer_hand.value > 21:
                print(" ")
                print("Dealer bust")
                print(" ")
                chip.win_bet()
                break
            elif dealer_hand.value < player_hand.value:
                print(" ")
                print("Player Won")
                print(" ")
                chip.win_bet()
                break
            elif dealer_hand.value > player_hand.value:
                print(" ")
                print("Dealer Won")
                print(" ")
                chip.lose_bet()
                break
            else:
                print(" ")
                print("Game Draw")
                print(" ")
                break
        print(f"Your chip value is: {chip.total}") 
        if chip.total > 0:
            while True:
                play_again = input("Do you want to play again? Enter yes or no: ")
                print(" ")  
                if play_again.lower() == "yes":
                    break    
                elif play_again.lower() == "no":
                    flag2 += 1
                    break
                else:
                    print("Please enter valid input")
                    continue
        else:
            print("You dont have chips to play") 
            break  
    while True:         
        restart_game = input("Do you want to restart game? Enter yes or no: ")
        if restart_game.lower() == "yes":
            break
        elif restart_game.lower() == "no":
            flag1 += 1
            break    
        else:
            print("Please enter valid input")
            continue                 





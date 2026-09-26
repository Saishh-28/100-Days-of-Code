import random

class Card:
    def __init__(self, Suit, FaceValue, ScoreValue):
        self.__Suit = Suit
        self.__FaceValue = FaceValue
        self.__ScoreValue = ScoreValue

    def getSuit(self):
        return self.__Suit

    def getFaceValue(self):
        return self.__FaceValue

    def getScoreValue(self):
        return self.__ScoreValue


class CardDeck:
    def __init__(self):
        self.__Deck = []
        self.__NextCardPointer = 0

        Suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        Faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in Suits:
            for face in Faces:

                if face in ["Jack", "Queen", "King"]:
                    Score = 10

                elif face in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    Score = int(face)
                else:
                    Score = 11

                self.__Deck.append(Card(suit, face, Score))

    def Shuffle(self):
        random.shuffle(self.__Deck)
        self.__NextCardPointer = 0

    def DealCard(self):
        if self.__NextCardPointer >= 52:
            return None

        card = self.__Deck[self.__NextCardPointer]
        self.__NextCardPointer += 1
        return card
    


class Hand:
    def __init__(self):
        self.__CardsInHand = []

    def AddCard(self, CardP):
        self.__CardsInHand.append(CardP)

    def CalculateScore(self):
        score = 0
        aceCount = 0

        for card in self.__CardsInHand:
            score += card.getScoreValue()

            if card.getScoreValue() == 11:
                aceCount += 1

        while score > 21 and aceCount > 0:
            score -= 10
            aceCount -= 1

        return score

    def DisplayHand(self, HideFirstCard):
        OutputString = ""

        for i in range(len(self.__CardsInHand)):

            if i == 0 and HideFirstCard:
                OutputString += "[Hidden Card] "

            else:
                OutputString += "[" + \
                self.__CardsInHand[i].getFaceValue() + \
                " of " + \
                self.__CardsInHand[i].getSuit() + "] "

        print(OutputString)


def Main():

    Deck = CardDeck()
    Deck.Shuffle()

    PlayerHand = Hand()
    DealerHand = Hand()

    # Initial cards
    PlayerHand.AddCard(Deck.DealCard())
    DealerHand.AddCard(Deck.DealCard())

    PlayerHand.AddCard(Deck.DealCard())
    DealerHand.AddCard(Deck.DealCard())

    PlayerBust = False
    PlayerStanding = False

    # PLAYER TURN
    while not PlayerBust and not PlayerStanding:

        print("\n--- PLAYER'S TURN ---")

        print("Your hand:")
        PlayerHand.DisplayHand(False)

        print("Your score:", PlayerHand.CalculateScore())

        print("\nDealer shows:")
        DealerHand.DisplayHand(True)

        Choice = input("Do you want to HIT or STAND?: ").upper()

        if Choice == "HIT":

            PlayerHand.AddCard(Deck.DealCard())

            if PlayerHand.CalculateScore() > 21:

                print("\nYour final hand:")
                PlayerHand.DisplayHand(False)

                print("Your score:", PlayerHand.CalculateScore())

                print("Bust! You lose.")
                PlayerBust = True

        elif Choice == "STAND":
            PlayerStanding = True

        else:
            print("Invalid choice.")

    # DEALER TURN
    if not PlayerBust:

        print("\n--- DEALER'S TURN ---")

        while DealerHand.CalculateScore() < 17:

            print("Dealer hits...")
            DealerHand.AddCard(Deck.DealCard())

        print("\nDealer's hand:")
        DealerHand.DisplayHand(False)

        DealerScore = DealerHand.CalculateScore()
        PlayerScore = PlayerHand.CalculateScore()

        print("Dealer score:", DealerScore)

        if DealerScore > 21:
            print("Dealer busts! You win.")

        else:

            print("Your score:", PlayerScore)

            if PlayerScore > DealerScore:
                print("You win!")

            elif DealerScore > PlayerScore:
                print("Dealer wins.")

            else:
                print("It is a draw.")

for i in range(5):
    Main()
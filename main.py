import tkinter
from PIL import Image, ImageTk
import random
#citations
#card images- https://code.google.com/archive/p/vector-playing-cards/
blackjack = tkinter.Tk()
xGeo = 300
yGeo = 300
blackjack.geometry(str(xGeo) + "x" + str(yGeo))
blackjack.title("Blackjack")
initialX = xGeo / 2
initialY = yGeo / 2
#y axis the players cards are going to be on
playerCardYPos = 20
#y axis the computers cards are going to be on
computerCardYPos = 40
#heart card variables
imgCardH1 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/ace_of_hearts.png")))
imgCardH2 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/2_of_hearts.png")))
imgCardH3 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/3_of_hearts.png")))
imgCardH4 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/4_of_hearts.png")))
imgCardH5 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/5_of_hearts.png")))
imgCardH6 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/6_of_hearts.png")))
imgCardH7 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/7_of_hearts.png")))
imgCardH8 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/8_of_hearts.png")))
imgCardH9 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/9_of_hearts.png")))
imgCardH10 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/10_of_hearts.png")))
imgCardH11 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/jack_of_hearts.png")))
imgCardH12 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/queen_of_hearts.png")))
imgCardH13 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/king_of_hearts.png")))
#spade card variables
imgCardS1 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/ace_of_spades.png")))
imgCardS2 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/2_of_spades.png")))
imgCardS3 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/3_of_spades.png")))
imgCardS4 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/4_of_spades.png")))
imgCardS5 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/5_of_spades.png")))
imgCardS6 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/6_of_spades.png")))
imgCardS7 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/7_of_spades.png")))
imgCardS8 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/8_of_spades.png")))
imgCardS9 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/9_of_spades.png")))
imgCardS10 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/10_of_spades.png")))
imgCardS11 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/jack_of_spades.png")))
imgCardS12 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/queen_of_spades.png")))
imgCardS13 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/queen_of_spades.png")))
#club card variables
imgCardC1 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/ace_of_clubs.png")))
imgCardC2 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/2_of_clubs.png")))
imgCardC3 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/3_of_clubs.png")))
imgCardC4 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/4_of_clubs.png")))
imgCardC5 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/5_of_clubs.png")))
imgCardC6 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/6_of_clubs.png")))
imgCardC7 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/7_of_clubs.png")))
imgCardC8 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/8_of_clubs.png")))
imgCardC9 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/9_of_clubs.png")))
imgCardC10 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/10_of_clubs.png")))
imgCardC11 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/jack_of_clubs.png")))
imgCardC12 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/queen_of_clubs.png")))
imgCardC13 =  tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/king_of_clubs.png")))
#diamond card variables
imgCardD1 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/ace_of_diamonds.png")))
imgCardD2 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/2_of_diamonds.png")))
imgCardD3 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/3_of_diamonds.png")))
imgCardD4 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/4_of_diamonds.png")))
imgCardD5 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/5_of_diamonds.png")))
imgCardD6 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/6_of_diamonds.png")))
imgCardD7 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/7_of_diamonds.png")))
imgCardD8 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/8_of_diamonds.png")))
imgCardD9 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/9_of_diamonds.png")))
imgCardD10 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/10_of_diamonds.png")))
imgCardD11 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/jack_of_diamonds.png")))
imgCardD12 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/queen_of_diamonds.png")))
imgCardD13 = tkinter.Label(blackjack, image = ImageTk.PhotoImage(Image.open("images/king_of_diamonds.png")))
#array containing all the cards in order of hearts, clubs, diamonds, and spaces(Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King)
#[card image, value 0 = 1 or 11, x position, y position]
cardArray = []
playerCards = []
computerCards = []
playerTotal = 0
computerTotal = 0
def resizeImages(newHeight):
  newWidth = (500 / 726) * newHeight
  for i in range(len(cardArray)):
    cardArray[i][0] = cardArray[i][0].resize((newWidth, newHeight))
def initialCardPlacement(xInt, yInt):
  for i in range(len(cardArray)):
    cardArray[i][0].place(x = xInt, y = yInt)
    cardArray[i][2] = xInt
    cardArray[i][3] = yInt
resizeImages((yGeo / 5))
#resets all values
def resetCards():
  cardArray = [[imgCardH1, 0, 0, 0], [imgCardH2, 2, 0, 0], [imgCardH3, 3, 0, 0], [imgCardH4, 4, 0, 0], [imgCardH5, 5, 0, 0], [imgCardH6, 6, 0, 0], [imgCardH7, 7, 0, 0], [imgCardH8, 8, 0, 0], [imgCardH9, 9, 0, 0], [imgCardH10, 10, 0, 0], [imgCardH11, 10, 0, 0], [imgCardH12, 10, 0, 0], [imgCardH13, 10, 0, 0], [imgCardC1, 0, 0, 0], [imgCardC2, 2, 0, 0], [imgCardC3, 3, 0, 0], [imgCardC4, 4, 0, 0], [imgCardC5, 5, 0, 0], [imgCardC6, 6, 0, 0], [imgCardC7, 7, 0, 0], [imgCardC8, 8, 0, 0], [imgCardC9, 9, 0, 0], [imgCardC10, 10, 0, 0], [imgCardC11, 10, 0, 0], [imgCardC12, 10, 0, 0], [imgCardC13, 10, 0, 0], [imgCardD1, 0, 0, 0], [imgCardD2, 2, 0, 0], [imgCardD3, 3, 0, 0], [imgCardD4, 4, 0, 0], [imgCardD5, 5, 0, 0], [imgCardD6, 6, 0, 0], [imgCardD7, 7, 0, 0], [imgCardD8, 8, 0, 0], [imgCardD9, 9, 0,0], [imgCardD10, 10, 0, 0], [imgCardD11, 10, 0, 0], [imgCardD12, 10, 0, 0], [imgCardD13, 10, 0, 0], [imgCardS1, 0, 0, 0], [imgCardS2, 2, 0, 0], [imgCardS3, 3, 0, 0], [imgCardS4, 4, 0, 0], [imgCardS5, 5, 0, 0], [imgCardS6, 6, 0, 0], [imgCardS7, 7, 0, 0], [imgCardS8, 8, 0, 0], [imgCardS9, 9, 0, 0], [imgCardS10, 10, 0, 0], [imgCardS11, 10, 0, 0], [imgCardS12, 10, 0, 0], [imgCardS13, 10, 0, 0]]
  playerCards = []
  computerCards = []
  playerTotal = 0
  computerTotal = 0

  initialCardPlacement(initialX, initialY)
resetCards()
#playCards are the cards of the person in turn
#yPos is the y position of the cards of the person in turn
#cardWidth is the width of the cards (TBD)
def cardPlay(playCards, yPos, cardWidth):
  cardCount = 0
  for i in playCards:
    cardCount = cardCount + 1
  halfCard = cardWidth / 2
  randomNum = random.randrange(len(cardArray))
  tempCard = cardArray[randomNum]
  cardArray.pop(randomNum)
  playCards.append(tempCard)
  xPos = (xGeo / 2) + (cardCount * halfCard)
  playCards[-1][2] = xPos
  playCards[-1].place(x = xPos, y = yPos)
  for i in range(len(playCards)):
    playCards[i][0].place(x = playCards[i][2] - halfCard, y = playCards[i][3])
    playCards[i][2] = playCards[i][2] - halfCard
blackjack.mainloop()
import math
import random

play = True
score = 0


while play:
  
    count = 1
    nummer = int(input("welke tafel wil je oefenen?"))
    
    for i in range (1,10):
          randomkeuz = random.randint(1,10)
          print(nummer, 'x', randomkeuz, '=')
          antwoord = nummer*randomkeuz
          mantwoord = int(input('antwoord'))
          if antwoord == mantwoord:
            print('goed')
            score = + 1
            print(score)
            else:
            print('fout')
            print(score)
            count = 1
    again = str(input('volgende vraag? ja/nee'))
    if again == 'no':
        play = False
        if count == 10:
            print(score)
        if score == 10:
            print('goed gedaan')
        else:
            print('kan beter')


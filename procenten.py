import math
from unittest import case


print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y?")
print("[2] Hoeveel % is x van y")

choice = input("Welke optie kies je?")

match choice:
    case "1":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))

        answer = x / 100 * y

        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "% = " + str(x/100) + " en " + str(x/100) + " x " + str(y) + " = " + str(answer) )

    case "2":
        print("optie 2 is gekozen")
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))

        answer2 = x / y * 100
        
        print('het antwoord is:', str(answer2))

    case '3':
        print('optie 3 is gekozen')
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        
        answer3 = (y / 100 + 1) * x  
        print('de vraag is hoeveel neemt het bedrag toe door', str(y), 'procent toe te voegen.')
        print('het antwoord is', str(answer3))


    case '4':
        print('optie 4 is gekozen')
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))

        answer4 = (y / 100 - 100 + 1) * x
        print('de vraag is hoeveel neemt het bedrag af door', str(y), 'procent eraf te halen.')
        print('het antwoord is', str(answer4))

    case '5':
        print('optie 5 is gekozen')
    
    case _:
        print("je hebt een ongeldige optie gekozen")
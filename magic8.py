import random


while True:
    pregunta = input("Por favor, introduce tu pregunta (debe contener al menos 5 caracteres y no puede estar vacía): ")
    if len(pregunta) >= 5 and pregunta.strip() != "":
        break
    else:
        print("Error: La pregunta no cumple con los requisitos. Inténtalo de nuevo.")

quest = input()

answ = random.randint(1,8)
if answ == 1:
    print('It is decidedly so.')
if answ == 2:
    print('Yes - definitely.')
if answ == 3:
    print('Reply hazy, try again.')
if answ == 4:
    print('Ask again later.')
if answ == 5:
    print('Better not tell you now.')
if answ == 6:
    print('My sources say no.')
if answ == 7:
    print('Outlook not so good.')
if answ == 8:
    print('Very doubtful')


#It is decidedly so.
#Yes - definitely.
#Reply hazy, try again.
#Ask again later.
#Better not tell you now.
#My sources say no.
#Outlook not so good.
#Very doubtful
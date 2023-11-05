#the_ciclone2.0.py
print('How much credits u have?')
credits = int(input())
print('How tall are you? (introduce a value in cm)')
height = int(input())
if credits >=10:
    if height >= 135:
        print ('Enjoy ur ride!')
    elif height< 135:
        print('You re not tall enough')
    else:
        print('Your are not tall enough and do  not have enough credits')
elif credits <10 and height >135 :
    print ('You do not have enough credits')
elif credits <10 and height <135: 
    print ('not credits not tall enough')


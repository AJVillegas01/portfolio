#the_cyclone.py
#this version of the_cyclone include a loop, the terminal gonna ask u 'till u giive the right answer

while True:
    credits = int(input('How much credits you have?'))
    if credits >= 10:
        break
    else:
         print('Error: You need at least 10 credits to ride')

while True:
    print(('How tall are you? (Introduce height in metres)'))
    height = float(input())
    if height < 1.37:
            print('Error: You are not tall enought')
    else:
            break    



print('You are allowed to continue, Enjoy your ride!')

print("Whats the pH value?")

phpre = float(input())
if 0<= phpre <=14: 
    ph = phpre
else:
    print ("error")

if ph>7:
    print('Basic')
elif ph ==7:
    print('Neutral')
else :
    print('Acid')
#sorting_hat.py
print ('The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry.',
        'The hat decides which of the four "Houses" each first-year student goes to:''🦁 Gryffindor,'' ''🦅 Ravenclaw,'' ''🦡 Hufflepuff'' 'or'🐍 Slytherin')
print ('Now you can answer some question, and the Sorting Hat gonna place u in a house')

G = 0
R = 0
H = 0
S = 0


print("\In the following questions, just type the number of the option as answer")

#in this file im gonna change the while loop into a again loop

q1 = int(input("Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk\n"))


while q1 not in [1,2]:
       q1 = int(input("Wrong answer. Repeat please\n"))
if q1 == 1:
        G = G+1 
        R = R+1
elif q1 ==2:
        H = H+1
        S = S+1      
else:
        print("Wrong input")
                

########

q2 = int(input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nYour answer:"))
while q2 not in [1,2,3,4]:
       q2 = int(input("Wrong answer. Repeat please\n"))
if q2 ==1:
        H = H+2       
elif q2 ==2:
        S = S+2                
elif q2 ==3:
        R = R+2              
elif q2 ==4:
        G = G+2               
else:
       print("Wrong input")
                

########

q3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
while q3 not in [1,2,3,4]:
       q3 = int(input("Wrong answer. Repeat please\n"))
if q3 ==1:
        S = S+4                
elif q3 ==2:
        H = S+4              
elif q3 ==3:
        R = R+4               
elif q3 ==4:
        G = G+4              
else:
        print("Wrong input")


print("\n\nRESULTS")
if G>S and G>H and G>R:
        print("You are a...GRYFFINDOR")
elif S>G and S>H and S>R:
    print("You are a...SLYTHERIN")
elif H>G and H>S and H>R:
    print("You are a...HUFFLEPUFF")
elif R>G and R>H and R>S:
    print("You are a...RAVENCLAW") 
else:
        print("You answer wrong, please repeat the questions")   


print("\n\nInternal Results")
print(G, "Gryffindor points'")
print(R, "Ravenclaw points'")
print(H, "Hafflepuff points'")
print(S, "Slytherin points'")

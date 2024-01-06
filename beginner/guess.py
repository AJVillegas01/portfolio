# Write code below 💖

guess = 0
tries=0
while guess != 6 and tries <8:
  guess = int(input("Guess the number:  "))
  tries += 1
  print('Number of tries:', tries)
if tries == 8:
    print('You have exceeded the number of tries')
else: 
   print("You got it!")

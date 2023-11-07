# String concatenation: is a useful method to join phrases 

for i in range(5):
  print('The square of ' + str(i) + ' is ' + str(i*i))

# String interpolation: is faster

for i in range(5):
  print(f'The square of {i} is {i*i}')

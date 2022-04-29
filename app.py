# print('Hello World')

#Create appropriate Variables for Item name, the price 
#and how many you have in stock

from ast import Add
from operator import truediv


item_name = str('widget')
price = float(1.89)
in_stock = int(100)
is_in_inventory = True
# print(item_name, price, in_stock, is_in_inventory)

# a=10
# b=3
# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float) : ', a / b)
# print('Division (floor) : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)

# msg='welcome to Python 101: Strings'
# print(msg)
# print(len(msg))
# print(msg.count('o'))
# print(msg.upper())
# print(msg.lower())
# print(msg.title())
# print(msg.capitalize())

# print(msg[0:17])

# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8] + ' '+ msg[-5:-1] + ' ' + msg[8:10] + ' ' + 'Tyler'
# print(msg1.title())
# print(msg1.title()[::-1])

# msg="""Dear Terry,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3"""
# print(msg)

# print(msg.find('Python'))
# immutable, need to save to new var
# print(msg.replace('Python', 'Rust'))
# msg1 = msg.replace('Python', 'Golang')
# print(msg1)


#  ~~~~~~~~~~~ MEMBERSHIP ~~~~~~~~~~~~~~~
# print('Python' not in msg)
# print('Python' in msg)


# ~~~~ Str Formatting ~~~~~

# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color}!'

# print(msg, msg1)

# ~~~~~ Capture User Input ~~~~~~~~~

# name = input('What is your name?: ')
# age = input(f'How old are you {name.title()}?')

# print(f'{name.title()} you are {age} years old? That is very old... You old bastard! lol')

# ~~~~~~~~~~~~~~~ CALCULATOR ~~~~~~~~~~~~~~~~~~~

# a = input('Enter a number: ')
# b = input('And one more number for fuck sake: ')
# add = float(a) + float(b)

# subtraction = float(a) - float(b)
# multiplication = float(a) * float(b)
# division_float = float(a) / float(b)
# division_floor = float(a) // float(b)
# modulus = float(a) % float(b)
# exponent = float(a) ** float(b)

# print(f'If you add them: {add}, or subtract: {subtraction}, but if you multiply: {multiplication}, also divide: {division_float}, or round the division: {division_floor}, remainder would be : {modulus}, then there is this big add number for the exponent: {exponent}')


#  ~~~~~Convert K's to Miles ~~~~~~~~

# name = input('Hey, what is your name? ')
# kilos = input('Give me a number to convert from k to miles?: ')

# miles = float(kilos) * 0.6214

# print(f'So {name.capitalize()}, for every {kilos} kilometers, that is {round(miles, 1)} miles!') 


# ~~~~~~~~~~~~~ LISTS ~~~~~~~~~~~~~~~~

# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]


# print(friends[1],friends[4])
# print(len(friends))
# print(friends.count('Eric'))
# print(friends.index('Terry'))


# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []

# sales_w2.append(int(input('How many lemonades did we sell today?: ')))
# sales = sales_w1 + sales_w2
# sales_high = max(sales) * 1.5
# sales_low = min(sales) * 1.5
# sales_total = sum(sales) *1.5

# print(f'Our best day, we made ${sales_high}. On our worst day, we only did ${sales_low} in sales. Overall, we did ${sales_total} for the 2 week period!')

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'


# friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
# print(friends_list)
# print('replace', csv.replace(';',',').replace(':',',').split(','))

#Tuples - faster Lists you can't change
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2:4])
print(friends_tuple[2:4])

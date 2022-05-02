# print('Hello World')

# Create appropriate Variables for Item name, the price
# and how many you have in stock

# from ast import Add
# from operator import truediv


# item_name = str('widget')
# price = float(1.89)
# in_stock = int(100)
# is_in_inventory = True
# print(item_name, price, in_stock, is_in_inventory)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  MATHS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  FunctioMEMBERSHIPS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# print('Python' not in msg)
# print('Python' in msg)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  STRING FORMATTING
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  LISTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  TUPLES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Tuples - faster Lists you can't change
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# print(friends_set.difference(my_friends_set))
# print(friends_set.intersection(my_friends_set))
# print(friends_set.union(my_friends_set))


# #Sets - blazingly fast unordered Lists
# #empty Lists
# empty_list = []
# empyt_list = list()

# #empty Tuple
# empty_tuple = ()
# empty_tuple = tuple()

# #empty Set
# empty_set = {} # this is wrong, this is a dictionary
# empty_set = set()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  SETS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']

# print('Eric' in friends and 'John' in friends)


# print(my_friends.union(friends))
# print(my_friends | friends)


# print(friends.intersection(my_friends))
# print(friends & my_friends)


# print(friends.difference(my_friends))
# print(friends - my_friends)

# print(my_friends.symmetric_difference(friends))
# print(my_friends ^ friends)

# cars_no_dupl = set(cars)
# print(cars_no_dupl)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# def greeting(name):
#     print(f'Hello {name}, you old bastard.')


# name = input('Whats your dumb name?: ')
# greeting(name)


# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return f"{amount}, {tax}, {total_amount}"
# ^^ string ^^
# or {amount, tax, total_amount} ~~ set
# or (amount, tax, total_amount) ~~ tuple
# or [amount, tax, total_amount] ~~ list

# price = value_added_tax(100)
# print(price, type(price))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Comparisons
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a = [3,7,42]
# b = [3,7,42]
# b = a proves true and true. They occupy the same memory in cpu
# print(a == b)
# print(a is b)
# print(id(a), id(b))


# a=7
# b=3
# print('a == b is', a == b)
# print('a != b is', a != b)
# print('a > b is', a > b)
# print('a < b is', a < b)
# print('a >= b is', a >= b)
# print('a <= b is', a <= b)
# print('o in John is ','o' in 'John') #membership
# print('o in John is ','o' not in 'John') #non membership
# print('John is John ','John' is 'John') #identity
# print('John is not John is ','John' is not 'John') # negative identity


# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

mode = input('Enter maths operation(+, -, /, *, convert): ')
num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))

if mode == '+':
    print(f'{num1 + num2}')
elif mode == '-':
    print(f'{num1 - num2}')
elif mode == '/':
    print(f'{num1 / num2}')
elif mode == '*':
    print(f'{num1 * num2}')
elif mode == 'convert':
    print(f'{(num1 * 1.8) + 32}')    
else:
    print('Something is wrong, go fuck yaself.')

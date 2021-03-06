
import numpy as np
import math


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

# mode = input('Enter maths operation(+, -, /, *, convert): ')
# num1 = float(input('Enter your first number: '))
# if mode.lower() == 'convert':
#     print(f'{num1}Cº is {(num1 * 1.8) + 32}Fº after converting!')
# else:
#     num2 = float(input('Enter your second number: '))

#     if mode == '+':
#         print(f'The answer is: {num1 + num2}')
#     elif mode == '-':
#         print(f'The answer is: {num1 - num2}')
#     elif mode == '/':
#         print(f'The answer is: {num1 / num2}')
#     elif mode == '*':
#         print(f'The answer is: {num1 * num2}')

#     else:
#         print('Something is wrong, go fuck yaself.')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  LOOPS - while loop
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# i = 0

# while i < 5:
#     i+=1
#     # multiply the stars by 'i' and they will add on each iteration. Then concat everything for formatting.
#     print(f' {i}. ' + '*' * i  + 'Loops are dope' +  '*' * i)


# Three Loop Questions:
# 1. What do I want to repeat?
#  ->
# 2. What do I want to change each time?
#  ->
# 3. How long should we repeat?
#  ->

# i = 0

# while i < 10:
#     i += 1
#     print(f'~' * i + 'D' * i + 'O' * i  + 'P' * i + 'E' * i + '~' * i)


# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
# 1. What do I want to repeat?
#  ->
# 2. What do I want to change each time?
#  ->
# 3. How long should we repeat?
#  ->

# import random
# rand_num = random.randint(1, 100)
# print(rand_num)

# guesses = 0

# user_guess = int(input('You have 5 tries. Guess a number from 1 to 100: '))


# while guesses < 5:

#     guesses += 1

#     if user_guess == rand_num:
#         print(f'You got it! {user_guess} is correct!')
#         break

#     elif user_guess < rand_num:
#         user_guess = int(input(f'{user_guess} is too low, guess higher: '))

#     elif user_guess > rand_num:
#         user_guess = int(input(f'{user_guess} is too high, guess lower: '))

# if user_guess != rand_num:
#     print(f'Ran out of turns, the correct number was {rand_num}')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  LOOPS - for loop
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']

# new_name = input('Enter a person to invite to the party! ')
# new_name1 = input('Enter another person to invite to the party! ')
# names.append(new_name)
# names1.append(new_name1)
# names.extend(names1)

# for name in names:
#     print(f'{name.title()}! You are invited to the party on Saturday!')




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Enumeration - Enumerate
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# print('python101 - Enumerate')
# friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
# efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]

# #i = 51
# #for friend in friends:
# #    print(i, friend)
# #    i = i +1 # += 1
# for num, friend in enumerate(friends,51):
#     print(num, friend)
# for friend in enumerate(friends,51):
#     print(friend)
# for friend in enumerate(enumerate(friends,51),-100):
#     print(friend)   
# for num, letter in enumerate('python',start = 5):
#     print(num, letter)
# print(type(enumerate(friends)))
# print(list(enumerate(friends)))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Dictionaries
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# super similar to js objects

# movie = {
#     'title' : 'Life of Brian',
#     'year' : 1979,
#     'cast' : ['John','Eric','Michael','George','Terry']
# }
# for key, value in movie.items():
#     print(key, value)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!MERGING DICKS IN THREE WAYS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
# holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
# life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}
#membership test
# print('Arthur' in holy_grail)
# if 'Arthur' not in python:
#     print('He\'s not here!')

# people = {}
# people1 = {}
# people2 = {}

# #method 1 update
# #best used if you have only 2 dictionaries to merge


# people.update(python)
# people.update(holy_grail)
# people.update(life_of_brian)
# print(people)

# #method 2 comprhension 
# #best used if you have older version and need to merge more than 2 dictionaries


# for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
# print(f'This is the comprehension method: {people1}')

# #method 3 unpacking 3.5 or later only!!
# #best used if you have recent version and need to merge more than 2 dictionaries

# people2 = {**python, **holy_grail, **life_of_brian}
# print(f' This is the unpacking version: {people2}')

# #sum of the ages of all the actors ages combined
# print('The sum of the ages is: ', sum(people.values()))



#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
# freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
# antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
# pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

# #create an dempty shopping cart
# cart = {}
# #loop through stores/dicts
# for shop in (freelancers,antiques,pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     buy_items = ", ".join(list(cart.keys()))
# print(f'You Purchased {buy_items}. Today it is all free. Have a nice day of mayhem!')




# freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
# antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
# pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

# #create an dempty shopping cart
# cart = {}
# #loop through stores/dicts

# for shop in  (freelancers, antiques, pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     #set the string to variable to clean it up
#     buy_items = ", ".join(list(cart.keys()))
# print(f'You Purchased {buy_items} Today it is all free. Have a nice day of mayhem!')



# The difference between explicit and reference-based copies is subtle, but can be really important. Try to keep in mind how a list is stored in the computer's memory.
# Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# # Create areas_copy
# areas_copy = list(areas)

# # Change areas_copy
# areas_copy[0] = 5.0

# # Print areas
# print(areas)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Packages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# print(np.array([1, 2, 3, 4]))


# # Definition of radius
# r = 0.43

# # Import the math package


# # Calculate C
# C = 2*math.pi*r

# # Calculate A
# A = math.pi*r**2

# Build printout
# print("Circumference: " + str(C))
# print("Area: " + str(A))

# # Definition of radius
# r = 192500

# # Import radians function of math package
# from math import radians

# # Travel distance of Moon over 12 degrees. Store in dist.
# dist = r * radians(12)

# # Print out dist
# print(dist)

# print(117.934 / 1.8796000000000002 ** 2)
# height_in and weight_lb are available as a regular lists

# Import numpy

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DOESNT WORK CUS THE LISTS ARE FROM DATACAMP ONLINE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Calculate the BMI: bmi
# np_height_m = np.array(height_in) * 0.0254
# np_weight_kg = np.array(weight_lb) * 0.453592
# bmi = np_weight_kg / np_height_m ** 2

# # Create the light array
# light = np.array(bmi < 21)

# # Print out light
# print(light)

# # Print out BMIs of all baseball players whose BMI is below 21
# print(bmi[light])

def energy_mass():
    num = input('Enter a number for mass and ill give you the energy ')
    print(f'E: {int(num) * (300000000 ** 2)}')

energy_mass()
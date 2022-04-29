# print('Hello World')

#Create appropriate Variables for Item name, the price 
#and how many you have in stock

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

msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8] + ' '+ msg[-5:-1] + ' ' + msg[8:10] + ' ' + 'Tyler'
# print(msg1.title())
# print(msg1.title()[::-1])

# msg="""Dear Terry,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3"""
# print(msg)

print(msg.find('Python'))
# immutable, need to save to new var
print(msg.replace('Python', 'Rust'))
msg1 = msg.replace('Python', 'Golang')
print(msg1)
#This is a password generation program 
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''
#create no, of unknown symbols 

""" if __name__ == "__main__":
    for i in range(1, nr_symbols+1,1):
        symbol = random.choice(symbols)
        #print(symbol)
        password = password + symbol
    for i in range(1, nr_numbers+1,1):
        symbol = random.choice(numbers)
        #print(symbol)
        password = password + symbol
    for i in range(1, nr_letters+1,1):
        symbol = random.choice(letters)
        #print(symbol)
        password = password + symbol

    print(password) """

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#first Solution
""" if __name__ == "__main__":
    randStuff = []
    for i in range(1, nr_symbols+1,1):
        symbol = random.choice(symbols)
        #print(symbol)
        randStuff.append(symbol)
    for i in range(1, nr_numbers+1,1):
        symbol = random.choice(numbers)
        #print(symbol)
        randStuff.append(symbol)
    for i in range(1, nr_letters+1,1):
        symbol = random.choice(letters)
        #print(symbol)
        randStuff.append(symbol)
    for i in range(1,nr_letters+nr_numbers+nr_symbols+1):
        password = password + random.choice(randStuff)
    print(password)
"""
#second solution 
password = ''
if __name__ == "__main__":
    for i in range(1, nr_symbols+1,1):
        symbol = random.choice(symbols)
        #print(symbol)
        password = password + symbol
    for i in range(1, nr_numbers+1,1):
        symbol = random.choice(numbers)
        #print(symbol)
        password = password + symbol
    for i in range(1, nr_letters+1,1):
        symbol = random.choice(letters)
        #print(symbol)
        password = password + symbol
    password = list(password)
    #print(password)
    random.shuffle(password)
    #print(password)
    password = ''.join(password)
    print(password)
'''Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, conoscendo quelle dell’ipotenusa a e dell’altro cateto b.'''
import math 
user_input = input("Enter a number to find its square root: ")
user_input2 = input("Enter a second number to find its square root: ")
a = int(user_input)
b = int(user_input2)
result = math.sqrt(a**2 - b**2)
print(f"The square root of {a}**2 - {b}**2 is {result}")
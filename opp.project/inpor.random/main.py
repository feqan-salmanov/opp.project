import random
from os import system as clear
clear("cls")
a = random.randint(5, 10)
print("Bir reqem tutdum bi gorek necedi.")
x=input("Tutulan reqem :")
if x==a:
    clear("cls")
    print("Tebrikler :)")
else:
    clear("cls")
    print("Tessuf ki sehvdir :)")

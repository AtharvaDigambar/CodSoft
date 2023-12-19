import random

print("\n****The Password Generator****\n")

letters=['a','b','c','d','e','f','g''h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['@','#','$','%','&','*','!']

no_letters=int(input("Enter the number of letters required for passward\n->"))

no_numbers=int(input("\nEnter the number of numbers required for password\n->"))

no_symbols=int(input("\nEnter the number of symbols required for password\n->"))

password=""

for char in range (1,no_letters+1):
    password=password+random.choice(letters)
    
for char in range (1,no_numbers+1):
    password=password+random.choice(numbers)
    
for char in range (1,no_symbols+1):
    password=password+random.choice(symbols)

print("\nYour genereted password is\n->",password)
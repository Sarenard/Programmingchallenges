import random

texte = input()
for lettre in texte:
    if random.randint(0, 1) == 0:
        print(lettre.upper(), end="")
    else:
        print(lettre.lower(), end="")
print()
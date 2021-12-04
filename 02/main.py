traductions = {
    "en" : {
        "choose_unit1" : "Hello, please enter an input unit (K, F or C) >>> ",
        "choose_unit2" : "Hello, please enter an output unit (K, F or C) >>> ",
        "nb" : "Please enter a number >>> ",
        "output" : "The converted value is: ",
        },
    "fr" : {
        "choose_unit1" : "Bienvenue, veuillez entrer une unité d'entrée (K, F ou C) >>> ",
        "choose_unit2" : "Bienvenue, veuillez entrer une unité de sortie (K, F ou C) >>> ",
        "nb" : "Veuillez entrer un nombre >>> ",
        "output" : "La valeur convertie est: ",
    },
}

def get_trad(language, texte):
    if language in traductions:
        if texte in traductions[language]:
            return traductions[language][texte]
    return get_trad("en", texte)

#get the language of the person
language = input(f"What is your language? {[x for x in traductions.keys()]} >>> ")
print(get_trad(language, "choose_unit1"), end = "")
unit1 = str(input().lower())
print(get_trad(language, "choose_unit2"), end = "")
unit2 = str(input().lower())
print(get_trad(language, "nb"), end = "")
number = int(input().lower())
print(get_trad(language, "output"), end = "")
match unit1, unit2:
    case "f", "c":
        print((number - 32)*5/9)
    case "c", "f":
        print((number*9/5)+32)
    case "k", "c":
        print(number-273.15)
    case "c", "k":
        print(number+273.15)
    case "k", "f":
        print((number*9/5)-459.67)
    case "f", "k":
        print((number-32)*5/9+273.15)
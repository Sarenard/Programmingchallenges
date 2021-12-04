import random
import json

config = json.load(open('config.json'))
class Person:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
    @staticmethod
    def generate_person():
        first_name = random.choice(open(config['first_names']).readlines()).replace("\n", "")
        last_name = random.choice(open(config['first_names']).readlines()).replace("\n", "")
        phone = f"+{random.randint(10, 99)}{random.randint(100000000, 999999999)}"
        return Person(first_name, last_name, phone)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"
    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"
    
person = Person.generate_person()
print(person)
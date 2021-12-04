from dataclasses import dataclass
import sys

@dataclass
class Player:
    name: str
    score: int = 0
    def get_choice(self):
        return input(f'{self.name}, tu joues quoi? (r, p or c): ')
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
    @staticmethod
    def create(name1, name2):
        return Game(Player(name1), Player(name2))
    def run(self):
        while True:
            a = self.player1.get_choice()
            b = self.player2.get_choice()
            if a == b:
                print('égalité')
            elif a == 'r' and b == 'p':
                print('gg', self.player2.name, "tu as gagné !")
                self.player2.score += 1
            elif a == 'r' and b == 'c':
                print('gg', self.player1.name, "tu as gagné !")
                self.player1.score += 1
            elif a == 'p' and b == 'r':
                print('gg', self.player1.name, "tu as gagné !")
                self.player1.score += 1
            elif a == 'p' and b == 'c':
                print('gg', self.player2.name, "tu as gagné !")
                self.player2.score += 1
            elif a == 'c' and b == 'r':
                print('gg', self.player2.name, "tu as gagné !")
                self.player2.score += 1
            elif a == 'c' and b == 'p':
                print('gg', self.player1.name, "tu as gagné !")
                self.player1.score += 1
            else:
                sys.exit()
            #print score
            print("Les scores sont :")
            print(f'{self.player1.name} : {self.player1.score}')
            print(f'{self.player2.name} : {self.player2.score}')
            if input('Veut tu rejouer? (o/n)') == 'o':
                break
            
        
game = Game.create(input("Entrez le prénom 1 >>> "), input("Entrez le prénom 2 >>> "))
game.run()
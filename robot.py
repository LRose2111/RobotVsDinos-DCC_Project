from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 225
        self.robotweapon = None

    def bot_weapon(self):
        robo_weapon = self.choose_weapon
        self.robotweapon = Weapon(robo_weapon)

    def choose_weapon(self):
        weapons_options = ['laser beam', 'freeze ray']
        while True:
            user_input = input(f'What weapon do you want to use?')
            if user_input == 'laser beam':
                print('Nice, Great choice!')
            elif user_input == 'freeze ray':
                print('Wow, Cold as Ice!')
            else:
                return user_input

    def robot_attack(self, dino):
        dino.health -= 25
        print(f'{self.name} attacks {dino.name} with a {self.bot_weapon}')   

        
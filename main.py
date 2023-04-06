import random

key = "Hello world"

class Item:
    def __init__(self, weigth, worth):
        self.weight = weigth
        self.worth = worth


class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)


class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health


class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name


    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()

    def die(self):
        print('Character died!!!')


class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, 'Goblin')

class Ork(Character):
    def __init__(self):
        Character.__init__(self, 200, 30, 'Ork')


class Player(Character):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        self.max_hp = hp

    def die(self):
        exit('WASTED BROO')

    def rest(self):
        self.hp = self.max_hp


class Field:
    def __init__(self, enemies):
        self.enemies = []
        self.loot = []

    def print_state(self):
        print('You look arround and see')
        for i in self.enemies:
            print(i.name)

    @staticmethod
    def gen_random():
        rand = random.randint(0, 2)
        if rand == 0:
            return Field([])
        if rand == 1:
            return Field([Ork()])
        if rand == 2:
            return Field([Goblin()])



class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(height):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def forward(self):
        if self.x == len(self.state) - 1:
            print('you see huge montaints, which you cant pass')
        else:
            self.x = self.x + 1

    def backwards(self):
        if self.x == 0:
            print('you see cliffs bro, sorry')
        else:
            self.x = self.x - 1

    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print('you see huge montaints, which you cant pass')
        else:
            self.y = self.y + 1

    def left(self):
        if self.y == 0:
            print('you see cliffs bro, sorry')
        else:
            self.y = self.y - 1


def forward(p, m):
    m.forward()


def left(p, m):
    m.left()


def right(p, m):
    m.right()


def backwards(p, m):
    m.backwards()


def save(p, m):
    pass


def quit_game(p, m):
    print('You comit suicide, bye!')
    exit(0)


def print_help(p, m):
    print(Commands.keys())


def pickup(p, m):
    pass


def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies > 0):
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(enemies[i].ad)

def rest(p, m):
    p.rest()

Commands = {
    'help': print_help,
    'quit': quit_game,
    'pickup': pickup,
    'forward': forward,
    'right': right,
    'left': left,
    'fight': fight,
    'save': save,
}

if __name__ == '__main__':
    name = input('enter your name')
    p = Player(name, 1000, 100)
    m = Map(5, 5)
    print('(type help to list the commands available')
    while True:
        command = input('>').lower().split(' ')
        command[0]
        if command[0] in Commands:
            Commands[command[0]](p, map)
        else:
            print('Your run arround in circles and dont know what to do')
        map.print_state()

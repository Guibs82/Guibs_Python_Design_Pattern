
# FrogWorld

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eat it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '---- Frog World ----'

    def make_character(self):
        """创建 Frog 对象"""
        return Frog(name=self.player_name)

    def make_obstacle(self):
        """创建 Bug 对象"""
        return Bug()



# WizardWorld

class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}'.format(self, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '---- Wizard World ----'

    def make_character(self):
        """创建 Wizard 对象"""
        return Wizard(name=self.player_name)

    def make_obstacle(self):
        """创建 Ork 对象"""
        return Ork()


# GameEnvironment 游戏入口
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    """验证年龄为数字"""
    try:
        age = input('Welcome {}. 你多大了?\n'.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, please try again...".format(age))
        return (False, age)
    else:
        return (True, age)

def main():
    name = input("你叫什么名字?\n")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name=name)
    game = FrogWorld if age < 18 else WizardWorld # 根据年龄选择相应的工厂方法
    environment = GameEnvironment(game(name)) # 根据不同的工厂方法, 创建不同的对象
    environment.play()

if __name__ == '__main__':
    main()
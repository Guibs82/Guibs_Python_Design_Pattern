class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'execute a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('ALIENWARE')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play))) # 通过适配器，指定synth 对象的execute 方法
    human = Human('Guibs')
    objects.append(Adapter(human, dict(execute=human.speak)))# 通过适配器，指定human 对象的execute 方法

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))

if __name__ == '__main__':
    main()
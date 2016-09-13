class worker():
    """工人"""
    def __init__(self, name):
        self.name = name
        self.skill = None

    def __str__(self):
        return self.name

    def set_skill(self, skill):
        self.skill = skill


class python_worker_builder():
    """Python 工人建造者"""
    def __init__(self):
        self.worker = worker(name='Python_worker')

    def setSkill(self):
        self.worker.set_skill('Python')


class swift_worker_builder():
    """Swift 工人建造者"""
    def __init__(self):
        self.worker = worker(name='Swift_worker')

    def setSkill(self):
        self.worker.set_skill('Swift')

class Hr():
    """指挥者"""
    def __init__(self):
        self.builder = None

    def construct_worker(self, builder):
        self.builder = builder
        self.builder.setSkill()

    @property
    def worker(self):
        return self.builder.worker

def validate_style(builders):
    """判定所需的builders"""
    try:
        worke_language = input("你需要那种语言的员工(Swift/Python)？\n")
        builder = builders[worke_language]()
        valid_input = True
    except KeyError as err:
        print('抱歉，资源库没有你要的人才')
        return (False, None)
    return (valid_input, builder)

def main():
    builders = dict(p=python_worker_builder, s=swift_worker_builder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders=builders)

    hr = Hr()
    hr.construct_worker(builder=builder)

    worker = hr.worker
    print("已找到你要的{}".format(worker))

if __name__ == '__main__':
    main()
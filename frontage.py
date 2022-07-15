# Pattern (шаблон) фасад
# интерфейс более высокого уровня к сложной системе.
# В отличии от адаптера, используется новый интерфейс.

# тип: структурный

# Используется:


class Paper(object):
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
        print(text)

class Printer(object):
    def error(self, msg):
        print('Ошибка!')

    def print_(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error('Бумага закончилась')

class Facade(object):
    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(1)

    def write(self, text):
        self._printer.print_(self._paper, text)

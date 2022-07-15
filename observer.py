# Pattern (шаблон) обзервер
# Реализует у класса механизм, который позволяет объекту этого класса получать оповещения об изменении состояния других объектов
# и тем самым наблюдать за ними.

# тип: поведенческий

# Используется:


from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    """
    Абстрактный наблюдатель
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Получение нового сообщения
        """
        pass

class Observable(metaclass=ABCMeta):
    """
    Абстрактный наблюдаемый
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.observers = []     # инициализация списка наблюдателей

    def register(self, observer: Observer) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        """
        Передача сообщения всем наблюдателям, подписанным на события
        данного объекта наблюдаемого класса
        """
        for observer in self.observers:
            observer.update(message)

class Newspaper(Observable):
    """
    Газета, за новостями в которой следят тысячи людей
    """

    def add_news(self, news: str) -> None:
        """
        Выпуск очередной новости
        """
        self.notify_observers(news)

class Citizen(Observer):
    """
    Обычный гражданин, который любит читнуть с утра любимую газетку
    """

    def __init__(self, name: str) -> None:
        """
        Constructor.

        :param name: имя гражданина, чтоб не спутать его с кем-то другим
        """
        self.name = name

    def update(self, message: str) -> None:
        """
        Получение очередной новости
        """
        print(f'{self.name} узнал следующее: {message}')

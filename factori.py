# Pattern (шаблон) фабрика
# Фабричный метод - Общий интерфейс для создания разных объектов, позволяющий подклассам определять тип создаваемого объекта.

# тип: Порождающий

# Используется:
# библиотека factory-boy, для генерации фабрик экземпляров для тестирования
# https://egorovegor.ru/testing-django-app/

from abc import ABC, abstractmethod

class Worker:
    pass
class Unemployed:
    pass

class PersonFactory(ABC):
    """
    Worker – рабочий
    Unemployed – безработный
    они указываются в type_of_person
    """
    def get_person(self, type_of_person):
        if type_of_person == "worker":
            return Worker()
        if type_of_person == "unemployed":
            return Unemployed()

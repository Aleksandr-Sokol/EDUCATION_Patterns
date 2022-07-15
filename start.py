from singleton import Singleton  # синглтон
from factori import PersonFactory  # фабрика
from decotator import time_text  # Декоратор
from command import Resolver  # команды
from frontage import Facade  # Фасад
from observer import Newspaper, Citizen  # Наблюдатель

print('синглтон:')
ex1 = Singleton()
ex2 = Singleton()
ex2.a = 123
print(ex1.a)

print('фабрика:')
person1 = PersonFactory().get_person('worker')
person2 = PersonFactory().get_person('unemployed')
print(f'types. person1 {type(person1)}, person2: {type(person2)}')

print('Декоратор:')
@time_text('working fun: ')
def fun():
    return 1
print(fun())

print('команды:')
r = Resolver()
data = {}
r.dispatch("COMMAND-1", data=data)

print('Фасад:')
f = Facade()
f.write('Hello world!')  # Hello world!
f.write('Hello world!')  # Ошибка: Бумага закончилась

print('Наблюдатель:')
newspaper = Newspaper()  # создаем небольшую газету
newspaper.register(Citizen('Иван'))  # добавляем двух человек, которые
newspaper.register(Citizen('Василий'))  # ... ее регулярно выписывают
newspaper.add_news('Наблюдатель - поведенческий шаблон проектирования')

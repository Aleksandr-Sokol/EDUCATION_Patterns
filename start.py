from singleton import Singleton  # синглтон

# синглтон
ex1 = Singleton()
ex2 = Singleton()
ex2.a = 123
print(ex1.a)


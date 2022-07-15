# Pattern (шаблон) синглтон
# порождающий паттерн, который гарантирует существование только одного экземпляра определённого класса

# Используется:

class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

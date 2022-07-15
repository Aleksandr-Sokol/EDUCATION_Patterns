# Pattern (шаблон) синглтон
# гарантирует существование только одного экземпляра определённого класса

# тип: порождающий

# Используется:

class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

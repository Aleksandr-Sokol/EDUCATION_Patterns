# Pattern (шаблон) Декоратор
#  убирает или изменяет поведение декорированного объекта.

# тип: Структурный

# Используется:
# для добавления новых функций, без изменения объекта
# 1. Для распределенных задач в cellery
# 2. для создания фикстур в тестировании

# Декоратор без параметра
import time

def time_work(func):
    def wrapper(*args, **kwargs):
        t0 = time.process_time()
        f = func(*args, **kwargs)
        print(f"time work: {time.process_time()-t0}")
        return f
    return wrapper

# Декоратор с параметром
def time_text(some_text: str = ''):
    def time_work(func):
        def wrapper(*args, **kwargs):
            t0 = time.process_time()
            f = func(*args, **kwargs)
            print(f"{some_text}: {time.process_time() - t0}")
            return f
        return wrapper
    return time_work

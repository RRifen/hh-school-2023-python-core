from datetime import datetime
from time import time


def decorator_time(func):
    def decorator(*args, **kwargs):
        print(f'Method {func.__qualname__} invoked at: {datetime.now()}')

        start = time()
        result = func(*args, **kwargs)
        elapsed_time = time() - start

        print('Время выполнения: ' + str(elapsed_time))
        return result
    return decorator

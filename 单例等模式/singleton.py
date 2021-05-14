
class Singleton:
    _instance = None


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

import threading


class Singleton2:
    lock = threading.Lock

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton2, '_instance'):
            with Singleton2.lock():
                if not hasattr(Singleton2, '_instance'):
                    Singleton2._instance = object.__new__(cls)
        return Singleton2._instance

a = Singleton2()
b = Singleton2()

print(id(a), id(b))


from functools import wraps


def singleton(cls):
    _instance = {}

    @wraps(cls)
    def func(*args, **kwargs):
        if not _instance.get(cls):
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return func

@singleton
class T:
    pass


def task(arg):
    obj = T()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

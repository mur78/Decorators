import time

from collections import OrderedDict
# def fabric_decorator(arg1):
#     print("Аргумент фабрики декораторов")
#
#     def decorator (fn):
#         print("Я вызываюсь при декорировании с аргументом")
#
#         def wrapper(*args, **kwargs):
#             print("Я вызываюсь в декорированной функции")
#             return fn(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
#     @decorator("ping")
#     def test(): # test = decorator(test)
#
#     @fabric_decorator(123)
#     def test2():
#         ...

def cache(size=3):
    def decorator_cache(fn):
        cash_dict = OrderedDict()
        def wrapper(*args):
            if args not in cash_dict:
                if len(cash_dict) == size:
                    cash_dict.popitem(last=False)
                result = fn(*args)
                cash_dict[args] = result

            return cash_dict[args]
        return wrapper
    return decorator_cache

@cache()
def my_sleep():
    time.sleep(3)

if __name__ == "__main__":
    #test2()
    t0 = time.time()

    my_sleep()
    my_sleep()

    print(time.time() - t0)
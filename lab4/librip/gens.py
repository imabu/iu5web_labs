import random


# Генератор вычленения полей из массива словарей
def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for it in items:
            for key in args:
                elem = it.get(key)                
                if elem is not None:
                    yield elem
    else:                
        for it in items:
            res_dict = {}
            for key in args:
                elem = it.get(key)
                if elem is not None:
                    res_dict[key] = elem
            if len(res_dict)>0:
                yield res_dict     


# Генератор списка случайных чисел
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin, end)

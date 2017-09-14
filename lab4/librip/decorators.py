# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно

def print_result(func):
    def decor():
        collect = func()
        if(isinstance(collect, list)):
            print('\n'.join(map(str, collect)))
        elif(isinstance(collect, dict)):
            print('\n'.join(map(lambda k: str(k) + ' = ' + str(collect[k]),
                                collect)))
        else: print(collect)
        return collect
            
    return decor
    

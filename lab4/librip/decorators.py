def print_result(func):
    def decor(*args):
        print("******", func.__name__, sep='\n')
        collect = func(*args)
        if isinstance(collect, list):
            print('\n'.join(map(str, collect)))
        elif isinstance(collect, dict):
            print('\n'.join(map(lambda k: str(k) + ' = ' + str(collect[k]),
                                collect)))
        else:
            print(collect)
        print("******")
        return collect
            
    return decor
    

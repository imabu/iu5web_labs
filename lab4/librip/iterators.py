# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):        
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # По-умолчанию ignore_case = False
        self.ig_case = kwargs.get('ignore_case', False)
        if isinstance(items, list):
           self.items = (x for x in items)
        else:
            self.items = items
        self._s = set()

    def __next__(self):
        for i in self.items:
            is_str = isinstance(i,str) 
            if (not is_str) and (i not in self._s):
                self._s.add(i)               
                return i
            elif is_str:
                if self.ig_case and (i.lower() not in self._s):
                    self._s.add(i.lower())
                    return i
                elif (not self.ig_case) and (i not in self._s):
                    self._s.add(i)
                    return i                     
        else: raise StopIteration()        

    def __iter__(self):
        return self
    


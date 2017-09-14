#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

un = Unique(data1)
un2 = Unique(data2)

print('list:', ' '.join(map(str,un)),'generator:', ' '.join(map(str, un2)), sep='\n')

# coding: utf-8
get_ipython().run_line_magic('paste', '')
get_ipython().run_line_magic('cpaste', '')
get_ipython().run_line_magic('run', 'myfile.py')
get_ipython().run_line_magic('pinfo', '%run')
get_ipython().run_line_magic('timeit', 'L = [n ** 2 for n in range(1000)]')
get_ipython().run_cell_magic('timeit', '', 'L = []\nfor n in range(1000):\n    L.append(n**2)')
get_ipython().run_line_magic('magic', '')
get_ipython().run_line_magic('magicls', '')
get_ipython().run_line_magic('lsmagic', '')
get_ipython().run_line_magic('timeit', 'print(1)')
timeit min(range(1000))
timeit max(range(1000))
get_ipython().run_line_magic('timeit', 'min(range(1000))')
get_ipython().run_line_magic('timeit', 'max(range(1000))')
timeit min(range(1000))
timeit max(range(1000))
get_ipython().run_line_magic('timeit', 'min(range(1000))')
get_ipython().run_line_magic('timeit', 'min(range(1000))')
import math
math.sin(2)
math.cos(2)
_
print(In)
In[20]
In[16]
Out[16]
Out[17]
In[17]
Out[100] = 2
Out
Out[100]
print(Out)
Out
Out[17] ** 2 + Out[18] ** 2
Out[24] = 3
Out
1

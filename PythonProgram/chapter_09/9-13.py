from collections import OrderedDict


py_dict = OrderedDict()
py_dict['dict'] = 'dictionary'
py_dict['list'] = 'list'
py_dict['tuple'] = 'tuple'
py_dict['str'] = 'string'
py_dict['class'] = 'class'

for key, value in py_dict.items():
    print("%s's funtion is %s." % (key, value))

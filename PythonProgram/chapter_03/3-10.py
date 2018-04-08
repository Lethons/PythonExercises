lists = ['baicai', 'huanggua', 'qincai', 'sigua', 'xihongshi']
lists[0] = 'luobo'
lists.insert(0, 'qiezi')
lists.append('lajiao')
print(lists)
del lists[0]
lists.pop()
lists.remove('huanggua')
print(lists)
print(sorted(lists))
lists.reverse()
print(lists)
lists.sort(reverse=True)
print(lists)
print(len(lists))

num_list = [x for x in range(1, 10)]
for num in num_list:
    print(num)
for num in num_list:
    if num == 1:
        print("%dst" % num)
    elif num == 2:
        print("%dnd" % num)
    elif num == 3:
        print("%drd" % num)
    else:
        print("%dth" % num)

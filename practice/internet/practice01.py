nums = [1, 2, 3, 4]
for i in nums:
    for j in nums:
        for k in nums:
            if i != j and j != k and i != k:
                num = i * 100 + j * 10 + k
                print(num)

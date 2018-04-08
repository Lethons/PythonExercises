favorite_num = {
    'leo': [2, 5, 8],
    'susan': [6, 9],
    'lethons': [7, 8, 9],
    'tom': [4, 6, 7],
    'alice': [8],
}
for name, nums in favorite_num.items():
    print("%s's favorite number is: " % name)
    for num in nums:
        print(num)

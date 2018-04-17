mouth_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0
year = int(input("year: "))
mouth = int(input("mouth: "))
day = int(input("day: "))
for i in range(mouth-1):
    result += mouth_days[i]
result = result + day 
if year % 4 == 0:
    result += 1
print(result)


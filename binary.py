

data = [1, 5, 4, 9, 7, 6, 3, 11, 14, 2, 8, 10, 15, 18,]

target = int(input("Bir son o'ylang: "))

l = len(data) -1
data.sort()
low = 0
i = 0
while True:
    midlle = (low + l) // 2
    if data[midlle] == target:
        print(f"Bu son {midlle} indexga tegishli.")
        i += 1
        break
    elif data[midlle] < target:
        low = midlle + 1

    elif data[midlle] > target:
        l = midlle - 1

    i += 1

print(data)
print(f"Kambinatsiyalar soni: {i}")

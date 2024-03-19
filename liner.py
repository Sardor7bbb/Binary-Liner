
data = [1, 5, 4, 9, 7, 6, 3, 11, 14, 2, 8, 10, 15, 18]

target = int(input("Bir son o'ylang: "))
step_by = 0

for i in data:
    if i == target:
        print(f"Siz o'ylagan son:{i} ga teng.")
        break
    elif i != target:
        step_by += 1

print(f"Kambinatsiyalar soni: {step_by}")

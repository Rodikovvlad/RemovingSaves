import os

path = "C:/Users/Влад\Documents/The Witcher/saves"
saves = os.listdir(path)

checks = []
perf = []

for save in saves:
    checks.append(save[3:6])

for num in checks:
    perf.append(int(num[::-1]))

maximum = max(perf)
index = perf.index(maximum)

for save in saves:
    if saves.index(save) != index:
        os.remove(path+"/"+save)

print(os.listdir(path))

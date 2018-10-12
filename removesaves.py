import os

path = "C:/Users/Влад/Documents/The Witcher/saves"
saves = os.listdir(path)

checks = []


for save in saves:
    if save[4] == '0':
        checks.append(int(save[5]))
    else:
        checks.append(int(save[4:6]))

for save in saves:
    if saves.index(save) != checks.index(max(checks)):
        os.remove(path+"/"+save)

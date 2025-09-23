import os

from math import *

all_rolls = []
all_rolls_pr = []
final = []
bad_numbers = 0

print("Введите Blade Roll в процентах в следующем формате")
print("Пример: 7.277 7.280 7.260")
blade_roll = input("- ")

blade_roll = blade_roll.replace(", ", " ").replace(",", ".")

all_rolls = list(map(float, blade_roll.split()))

for i in range(len(all_rolls)):
    all_rolls_pr.append(
        round(tan(radians(all_rolls[i])) * 100, 1)
    )

for i in range(len(all_rolls_pr)-1):
    c = abs(round(all_rolls_pr[0] - all_rolls_pr[i+1], 1))
    
    if c == 0.0 or c == 0.1:
        final.append(c)
    else:
        final.append(f"! {c} !")
        bad_numbers += 1

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

print("Blade Roll в Градусах", all_rolls, sep="\n", end="\n\n")
print("Blade Roll в Процентах", all_rolls_pr, sep="\n", end="\n\n")
print(f"Разница Blade Roll по сравнению с первым числом ({all_rolls[0]}°) ({all_rolls_pr[0]}%) в Процентах", final, sep="\n", end="\n\n")
print("Количество отклонений на 0.2 и больше:", bad_numbers)
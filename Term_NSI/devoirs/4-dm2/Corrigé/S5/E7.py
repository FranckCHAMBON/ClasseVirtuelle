"""
Prologin: Entraînement 2003
Exercice: 7 - Table de multiplication
https://prologin.org/train/2003/semifinal/table_de_multiplications
"""
multiple = int(input())

for x in range(1,10):
    print(f"{multiple}x{x}={multiple*x}")
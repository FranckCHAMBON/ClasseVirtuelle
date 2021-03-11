"""
auteur : Franck CHAMBON
https://prologin.org/train/2003/semifinal/puzzle
"""

# constantes
L_Pièce = 4
L_Puzzle = 10

pièce = [input() for _ in range(L_Pièce)]
puzzle = [input() for _ in range(L_Puzzle)]

def est_valide(i: int, j: int) -> bool:
    "Renvoie : peut-on mettre la pièce en partant de (i, j) ?"
    for di in range(L_Pièce):
        idi = i + di
        for dj in range(L_Pièce):
            jdj = j+dj
            if pièce[di][dj] == "1":
                if (idi >= L_Puzzle) or (jdj >= L_Puzzle):
                    return False
                if puzzle[idi][jdj] == "1":
                    return False
    return True

def plaçable() -> bool:
    "Renvoie : peut-on placer la pièce quelque part ?"
    for i in range(L_Puzzle):
        for j in range(L_Puzzle):
            if est_valide(i, j):
                return True
    return False

print("1" if plaçable() else "0")

"""
TEST
entrée :

0110
0110
1111
0011
1111111111
1110111111
1100111001
1100111001
1000011101
1100011111
1111011111
1100100111
1110110011
1110111111

sortie :
1

"""

"""
Prologin:  Entraînement  2003
Exercice: 10 - Solitaire
https://prologin.org/train/2003/semifinal/solitaire
"""
def coup_posible(plateau, y: int, nb_coup: int):
    """ trouve le nombre de bille qui peuvent etre jouer
    """
    for ligne in range(7):
        if plateau[y][ligne] == '1':
            if ligne < 5 : 
                if plateau[y][ligne + 1] == '1':
                    if plateau[y][ligne + 2] == '0':
                        nb_coup += 1       
                    if plateau[y][ligne - 1] == '0':
                        nb_coup +=1
            if ligne == 5 :
                if plateau[y][ligne + 1] == '1' and plateau[y][ligne - 1] == '0':
                    nb_coup += 1
            if y <= 4:
                if plateau[y + 1][ligne] == '1' and plateau[y + 2][ligne] == '0':
                    nb_coup += 1
            
            if y >= 2:
                if plateau[y - 1][ligne] == '1' and plateau[y - 2][ligne] == '0':
                    nb_coup += 1
                
    if y < 6:
        return coup_posible(plateau, y + 1, nb_coup)
    else :
        return nb_coup


plateau = [input() for _ in range(7)]
nb_coup = 0
y = 0
print(coup_posible(plateau, y, nb_coup))

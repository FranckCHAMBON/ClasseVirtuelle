"""
Prologin:  Entraînement  2003
Exercice: 9 - Puzzle 
https://prologin.org/train/2003/semifinal/puzzle
"""
def trouve_enplacement_piece(piece_puzzle,  puzzle_entier,x: int, x2: int):
    """ cherche un endroit où la piece de puzzle peut entrer si elle entre affiche 1 sinon 0
    """
    piece_rentre = 0
    conteur_piece_vide = 0
    conte_nb_rentre = 0
    def cherche_peut_rentrer(piece_puzzle, puzzle_entier, x: int, x2:int, ligne: int, piece_rentre: int, conte_nb_rentre: int):
        "analise si la piece pourait rentrer dans le puzzle "
        sauvegarde_ligne = ligne 
        if ligne == 0:
            ligne -= 1
            for y in range(0, len(piece_puzzle)):
                ligne += 1
                if piece_puzzle[x2][y] != puzzle_entier[x][ligne] or piece_puzzle[x2][y] == '0':
                    conte_nb_rentre +=1
            ligne = sauvegarde_ligne
            if x2 < 3 :
                cherche_peut_rentrer(piece_puzzle, puzzle_entier, x + 1, x2 + 1, ligne, piece_rentre, conte_nb_rentre)
                
            if conte_nb_rentre == 12:
                piece_rentre = 1
                   
        else:
            if piece_puzzle[x2][0] == '0' or piece_puzzle[x2][0] != puzzle_entier[x][ligne - 1]:
                ligne -= 1
                for y in range(0, 4):
                    if piece_puzzle[x2][y] != puzzle_entier[x][ligne] or piece_puzzle[x2][y] == '0':
                        conte_nb_rentre +=1
                    ligne += 1
                ligne = sauvegarde_ligne
                if x2 < 3 :
                    cherche_peut_rentrer(piece_puzzle, puzzle_entier, x + 1, x2 + 1, ligne, piece_rentre, conte_nb_rentre)
                if conte_nb_rentre == 12:
                    piece_rentre = 1
                   
            else:
                for y in range(0, 4):
                    if piece_puzzle[x2][y] != puzzle_entier[x][ligne] or piece_puzzle[x2][y] == '0':
                        conte_nb_rentre +=1
                    ligne += 1
                ligne = sauvegarde_ligne
                if x2 < 3 :
                    cherche_peut_rentrer(piece_puzzle, puzzle_entier, x + 1, x2 + 1, ligne, piece_rentre, conte_nb_rentre)
                if conte_nb_rentre == 12:
                    piece_rentre = 1      

              
            

    for vérif in piece_puzzle:
        if vérif == '0000':
            conteur_piece_vide += 1
    if conteur_piece_vide == 4:
        return '1'
    else:
        sauvegarde_x = x
        for ligne in range(0, len(puzzle_entier)):
            if puzzle_entier[x][ligne] != '1':
                cherche_peut_rentrer(piece_puzzle, puzzle_entier, x, x2, ligne, piece_rentre, conte_nb_rentre)
            x2 = 0
            x = sauvegarde_x
            conte_nb_rentre = 0
        if x < 9 and piece_rentre == 0:
            return trouve_enplacement_piece(piece_puzzle, puzzle_entier, x + 1, x2)
        else:
            return piece_rentre
            
         

piece_puzzle = [input() for _ in range(4)]
puzzle_entier = [input() for _ in range(10)]
x = 0
x2 = 0
print(trouve_enplacement_piece(piece_puzzle, puzzle_entier, x, x2))
""" problème out of range ligne 34, 45 alors qu'il ne drvrait pas 
et aussi il y a un problème si la primière ligne de la piece de puzzle ressemble à ça 0001 alors j'ai pas de code pour savoir ça"""

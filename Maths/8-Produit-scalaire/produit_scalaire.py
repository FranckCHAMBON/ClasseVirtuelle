from math import sqrt, cos

def norme(x, y):
	"""Retourne la norme du vecteur (x, y)
	>>> norme(3, 4)
	5.0
	"""
	return sqrt(x*x + y*y)

# un test
assert norme(3, 4) == 5.0

def produit_scalaire(x1, y1, x2, y2):
	"""
	Retourne le produit scalaire de deux vecteurs
	* (x1, y1), 
	* (x2, y2)
	dans un répère orthonormé
	"""
	return x1*x2 + y1*y2
	#return norme(x1, y1) * norme(x2, y2) * cos(???)
	#return 1/4 * ( norme(x1+x2, y1+y2)**2 - norme(x1-x2, y1-y2)**2 )
	
# deux tests
assert produit_scalaire(13, 17, 0, 1) == 17
assert produit_scalaire(13, 17, 1, 0) == 13

def angle_entre_deux_vecteurs(x1, y1, x2, y2):
    """
    Renvoie l'angle formé par les vecteurs (x1, y1) et (x2, y2),
    angle en degré
    """
    produit_scalaire = x1*x2 + y1*y2
    norme1 = norme(x1, y1)
    norme2 = norme(x2, y2)
    cos_angle = produit_scalaire / (norme1 * norme2)
    angle_rad = acos(cos_angle) # en radians
    return angle_rad * 180 / pi

assert round(angle_entre_deux_vecteurs(4, -3, 1, 5)) == 116
   
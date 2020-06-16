from math import sqrt, cos

def norme(x, y):
	"Retourne la norme du vecteur (x, y)"
	return sqrt(x*x + y*y)

# un test
assert norme(3, 4) == 5

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


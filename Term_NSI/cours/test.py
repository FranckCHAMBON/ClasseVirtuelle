class Fraction:
    def __init__(self, a, b):
        self._numérateur = a
        self._dénominateur = b

    def __str__(self):
        return f"Fraction : {f.donne_numérateur()} sur {f.donne_dénominateur()}"

    def __repr__(self):
        return f"({f.donne_numérateur()}/{f.donne_dénominateur()})"

    def donne_numérateur(self):
        return self._numérateur

    def donne_dénominateur(self):
        return self._dénominateur

    def modifie_numérateur(self, a):
        self._numérateur = a

    def modifie_dénominateur(self, b):
        self._dénominateur = b
    
    def multiplie_par(self, fraction):
        self._numérateur *= fraction.donne_numérateur()
        self._dénominateur *= fraction.donne_dénominateur()


f = Fraction(2, 3)
g = Fraction(5, 7)
f.multiplie_par(g)
print("f ->", repr(f))

L = int(input())
l = int(input())

c = L
somme = c * c
for i in range(L - l):
    c = c - 1
    somme = somme  +  c * c

print(somme)

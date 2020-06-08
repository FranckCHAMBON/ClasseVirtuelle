def note(poids, age, l_corne, h_garrot):
    "Retourne la note du karva"
    return l_corne * h_garrot + poids


nb_karva = int(input())

for index in range(nb_karva):
    poids = int(input())
    age = int(input())
    l_corne = int(input())
    h_garrot = int(input())


    print(note(poids, age, l_corne, h_garrot))

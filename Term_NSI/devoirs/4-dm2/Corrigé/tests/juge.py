import subprocess

def get_exo():
    for i in range(1, 14):
        yield f"E{i}"
    for i in range(1, 5):
        yield f"Q{i}"

for id_élève in range(9):
    print("On juge l'élève", id_élève)
    score = 0
    for exo in get_exo():
        try:
            with open(f"../Term/S{id_élève}/{exo}.py", 'r') as prog_py:
                pass
        except FileNotFoundError:
            continue
        print("Pour le problème", exo, end=" : ")
        score_exo = 0
        num_test = -1
        juge = False
        while True:
            num_test += 1
            
            #print(id_élève, exo, num_test)
            try:
                #print("OK0", f"{exo}/in{num_test}")
                with open(f"{exo}/in{num_test}", 'r') as entrée:
                    #print("OK1", f"{exo}/OUT{num_test}")
                    with open(f"{exo}/OUT{num_test}", 'r') as sortie:
                        try:
                            réponse = subprocess.run(
                                ["python3", f"../Term/S{id_élève}/{exo}.py"],
                                stdin=entrée,
                                capture_output=True,
                                timeout=2,
                                text=True)
                            réponse = réponse.stdout.strip()
                        except:
                            réponse = ""
                        RÉPONSE = sortie.read().strip()
                        if réponse == RÉPONSE:
                            score_exo += 1
                        else:
                            if not juge:
                                print("Échec au test", num_test)
                            juge = True
                        
            except FileNotFoundError:
                break
        if score_exo == num_test:
            score += 1
            print("Succès")
    print(f"Score total de l'élève {id_élève} : {score}")
    print("\n"*2)
    #python3 ../Term/PROF/{exo}.py <{exo}/{in_file} >{exo}/{outfile}
import subprocess

def get_exo():
    for i in range(1, 14):
        yield f"E{i}"
    for i in range(1, 5):
        yield f"Q{i}"

for exo in get_exo():
    num_test = -1
    while True:
        num_test += 1
        try:
            print(exo, num_test)
            with open(f"{exo}/in{num_test}", 'r') as entrée:
                with open(f"{exo}/OUT{num_test}", 'w') as sortie:
                    subprocess.call(f"python3 ../Term/PROF/{exo}.py",
                                    stdin = entrée,
                                    stdout = sortie,
                                    shell = True)
        except FileNotFoundError:
            break
#python3 ../Term/PROF/{exo}.py <{exo}/{in_file} >{exo}/{outfile}
from math import exp

def f(t):
    return 20 * exp(-0.1 * t)

t = 0
C = f(t)
while C > 0.2 :
  t = t + 0.1
  C = f(t)
print("Au bout de", t, "heures, le médicament est considéré éliminé")

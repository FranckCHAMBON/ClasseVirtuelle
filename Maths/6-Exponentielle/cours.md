# Fonction exponentielle

```python {cmd="python3" matplotlib=true}
import matplotlib.pyplot as plt
from math import exp

def xrange(a, b, n):
    " Retourne n points de [a..b[ "
    return [a + (b-a)/n * i for i in range(n)]

X = xrange(-2, +2, 20) # 20 points entre -2 et +2
Y = [exp(x) for x in X] # images de X par exponentielle
plt.plot(X, Y) # le graphique associé

# décoration
plt.xlabel("Axe des abscisses")
plt.ylabel("Axe des ordonnées")
plt.title(r"Fonction $x\mapsto \exp(x)$")
plt.annotate(r"$\exp(0) = 1$", xy=(0, 1), xytext=(0.5, 0.5), arrowprops=dict(facecolor='black'), )


# affichage
plt.show()
```
> Représentation graphique de la fonction exponentielle.

## Avant de commencer
###  Formules sur les fractions

Pour $a, b\in \mathbb R^*$, et $n, m \in \mathbb Z$
* $a^n \times a^m = a^{n+m}$
* $(a^n)^m = a^{n\times m}$
* $a^n \times b^n = (a\times b)^n$
* $\dfrac{a^n}{a^m} = a^{n-m}$ , et aussi $\dfrac{1}{a^n} = a^{-n}$
* $a^0 = 1$, $a^1 = a$, $a^2 = a\times a$, ...
* $\dfrac{a^n}{b^n} = \left(\dfrac{a}{b}\right)^n$ 

#### Exercice 1 p156
1.  $2^4 \times 2^7 \times 2^3 = 2^{4+7+3} = 2^{14}$
2. $6^4 \times 6^{-9} = 6^{4+(-9)} = 6^{-5}$
3. $3^2 \times 9^4$, deux pistes
    * $9\times 9^4 = 9^1\times 9^4 = 9^5$
    * $3^2 \times (3^2)^4 = 3^2 \times 3^8 = 3^{10}$
    * $3^2 \times (3^2)^4 = (3^2)^5 = 3^{10}$
4. $2^5\times3^5 = (2\times3)^5 = 6^5$
5. $\dfrac{2^8\times2^{-4}}{2^{-1}\times2^3} = 2^{(8+(-4)) - ((-1)+3)} = 2^2$
(variante) $\dfrac{2^8\times2^{-4}}{2^{-1}\times2^3} = 2^8\times2^{-4}\times2^1\times2^{-3} = 2^2$

## Formules sur les dérivées

Soit $f$, $g$ des fonctions dérivables.
* Si $f(x) = ax+b$, alors $f'(x)=a$
* Avec $n\in\mathbb N^*$, si $f(x) = x^n$, alors $f'(x)=n\times x^{n-1}$
* $(f+g)'= f'+g'$
* $(fg)' = f'g + fg'$
* si $g$ ne s'annulle pas, $\left(\dfrac f g\right)' =
\dfrac{f'g - fg'}{g^2}$
* $(\sqrt x)' = \dfrac 1 {2\sqrt x}$
* (Hors programme) $f(g(x))' = f'(g(x))\times g'(x)$
* (Au programme, $g$ affine) $f(ax+b)'= a\times f'(ax+b)$



### Exercice (exponentielle) A p 158

On admet que $f(0)=1$, et $f'(x)=f(x)$ pour tout $x\in\mathbb R$.

On pose $g(x) = f(x)\times f(-x)$, calculons $g'$.

Calculons d'abord, avec $b=0$ et $a=-1$ :
* $(f(-x))' = (-1) \times f'(-x) = - f(-x)$

Dérivons $g$ :
* $g'(x) = f'(x)\times f(-x) + f(x)\times -f(-x)$
* $g'(x) = f(x)\times f(-x) - f(x)\times f(-x)$
* $g'(x)= 0$, pour tout $x\in\mathbb R$
* Donc $g(x)$ est constante, égale à $g(0) = f(0)\times f(-0) = 1^2 =1$

> Conclusions
>* $g(x)=1$, pour tout $x\in\mathbb R$
>* $f(x)\times f(-x) = 1$, pour tout $x\in\mathbb R$
>* Et donc $f(-x) = \dfrac 1 {f(x)}$, pour tout $x\in\mathbb R$
>* $f$ ne s'annule pas sur $\mathbb R$.






## La fonction exponentielle
### Notation
La fonction exponentielle se note :
* $\exp$
*  (ou $x\mapsto \mathrm e ^x$)

C'est l'unique fonction $f$ réelle telle que :
* $f(0) = 1$
* $f'(x) = f(x)$, pour tout $x\in\mathbb R$

### Propriétés

$\exp$ est définie et dérivable sur $\mathbb R$, avec :
* L'image de zéro :
    * $\exp(0)=1$
    * $\mathrm e^0 = 1$

* la dynamique :
    * $\exp'(x) = \exp(x)$
    * $(\mathrm e^x)' =\mathrm e^x$

### Produit d'exponentielles
>Pour tout $x\in\mathbb R$, on a :
>
>* $\exp(-x)=\dfrac 1 {\exp x}$
>   * ou bien $\mathrm e^{-x} = \dfrac 1 {\mathrm e^x}$
>* $\exp(x+y) = \exp(x) \times \exp(y)$
>   * ou bien $\mathrm e^{x+y} = \mathrm e^x \times \mathrm e^y $

On a déjà prouvé le premier point.

Preuve du deuxième point :

On fixe $y\in\mathbb R$ 
Soit $f(x) = \dfrac{\exp(x+y)}{\exp(x)}$,

on a $f=\dfrac uv$, $f'=\dfrac{u'v-uv'}{v^2}$

 avec
* $u= \exp(x+y)$ ; $u'=1 \times \exp(x+y)$
* $v=\exp(x)$ ; $v'=\exp(x)$


> $(g(ax+b) )' = a\times g'(ax+b)$
>Avec $b=y$, $a=1$, $g=\exp$, $g'=\exp$

Ainsi $f'(x) = \dfrac{\exp(x+y)\times \exp(x) - \exp(x+y)\times \exp(x)}{\exp(x)\times \exp(x)}$
Ainsi $f'(x) = \dfrac{\left[\exp(x+y) - \exp(x+y)\right]\times \exp(x)}{\exp(x)\times \exp(x)}$
Ainsi $f'(x) = \dfrac{\exp(x+y) - \exp(x+y)}{ \exp(x)}$
D'où $f'(x) = 0$, pour $x\in \mathbb R$

Ainsi $f$ est constante sur $\mathbb R$, et 
$f(x) = f(0) = \dfrac{\exp(0+y)}{\exp(0)}=\dfrac{\exp(y)}{1} = \exp(y)$

> Conclusion : 
>* $\dfrac{\exp(x+y)}{\exp(x)} = \exp(y)$
>* $\exp(x+y) = \exp(x) \times \exp(y)$

Avec $y=-x$, on retrouve,
* $\dfrac{\exp(x+(-x))}{\exp(x)} = \exp(-x)$

* $\dfrac{\exp(0)}{\exp(x)} = \exp(-x)$
> * $\exp(-x) = \dfrac{1}{\exp(x)}$
> * $\mathrm e^{-x} = \dfrac{1}{\mathrm e^x}$

### Quotient d'exponentielles

* $\dfrac{\exp(x+(-y))}{\exp(x)} = \exp(-y)$
* $\dfrac{\exp(x-y)}{\exp(x)} = \dfrac{1}{\exp(y)}$
>* $\exp(x-y) = \dfrac{\exp(x)}{\exp(y)}$
>* $\mathrm e^{x-y} = \dfrac{\mathrm e^x}{\mathrm e^y}$

Rappel : $a^{n-m}=\dfrac{a^n}{a^m}$, une autre formule sur les puissances qui montre que la fonction exponentielle se comporte comme une puissance d'un certain nombre $\mathrm e$.

### Puissance d'exponentielle
Propriété :
Pour tout $n\in\mathbb N$, $[\exp(x)]^n = \exp(nx)$
* Avec $n=0$, $[\exp(x)]^0=1=\exp(0) = \exp(0\times x)$
* Avec $n=1$, $[\exp(x)]^1=\exp(x) = \exp(1\times x)$
* Avec $n=2$, $[\exp(x)]^2=\exp(x)\times \exp(x) = \exp(x + x)=\exp(2\times x)$
* Avec $n=3$,
 $[\exp(x)]^3=[\exp(x)]^2\times \exp(x) = \exp(2x) \times\exp(x)=\exp(2x + x) = \exp(3x)$

...
On fixe $n\in \mathbb N$.
On suppose que $[\exp(x)]^n = \exp(nx)$, on montre $[\exp(x)]^{n+1} = \exp((n+1)x)$

$[\exp(x)]^{n+1} = [\exp(x)]^n \times \exp(x) = \exp(nx)\times \exp(x)= \exp(nx + x) = \exp((n+1)x)$

* $a^{n+1}=a^n\times a^1=a^n\times a$
* $nx+x = (n+1)x$

> On corrige l'exercice [24 p 171](ex24.html)




**Remarque** : $\exp(n) = \mathrm e^n$ pour $n\in \mathbb N$, exemple $\exp(2)=\mathrm e^2$


### Dérivée de $\mathrm e^{ax+b}$
En appliquant la formule : $(f(ax+b))' = a\times f(ax+b)$, on déduit :

> $(\mathrm e^{ax+b})' = a \times \mathrm e^{ax+b}$

Exemple : $h(x) = -3\mathrm e^{2x-5} + 1$
* $h'(x)=-3 (\mathrm e^{2x-5})' + 0$
* $h'(x)=-3 \times 2\mathrm e^{2x-5}$
* $h'(x)=-6\mathrm e^{2x-5}$

### Égalité d'exponentielle
On suppose $\mathrm e^a = \mathrm e^b$, avec $a, b\in \mathbb R$: 
* $\mathrm e^a - \mathrm e^b =\mathrm e^a - \mathrm e^{a+(-a+b)}$
* $\mathrm e^a - \mathrm e^b =\mathrm e^a\times 1 - \mathrm e^{a}\times\mathrm e^{+(-a+b)}$
* $\mathrm e^a - \mathrm e^b =\mathrm e^a\times( 1 - \mathrm e^{+(-a+b)})$
* donc $\mathrm e^a\times( 1 - \mathrm e^{+(-a+b)})=0$
* Or $\mathrm e^a\neq 0$, ainsi
* $1 - \mathrm e^{+(-a+b)} = 0$, donc
* $\mathrm e^{-a+b} = 1$, or sur $\mathbb R$, $\exp$ est strictement croissante, et $1$ n'a qu'un antécédent, c'est zéro.
* Ainsi $-a+b = 0$, et finalement $a=b$.

**Attention** , en terminale, on pourrait apprendre que :
* $\mathrm e^{i\pi}+1=0$, donc
* $\mathrm e^{i\pi}=-1$
* $(\mathrm e^{i\pi})^2=+1$
* $\mathrm e^{2i\pi}=+1=\mathrm e^{0}$
* mais $2i\pi\neq 0$

Et donc, la condition sur $a$ et $b$ qui sont réels est essentielle.

On a aussi, pour tous nombres réels $a$ et $b$ :
* $\mathrm e^a = \mathrm e^b \iff a = b$
* $\mathrm e^a < \mathrm e^b \iff a < b$
* $\mathrm e^a > \mathrm e^b \iff a > b$

> La fonction exponentielle est strictement croissante sur $\mathbb R$.

---

Exercice B p 165

$\exp\left(\dfrac x b\right) = \exp\left(\dfrac 1 b x + 0\right)$
donc 
$\left(\exp\left(\dfrac x b\right)\right)' = \dfrac 1 b \exp\left(\dfrac 1 b x + 0\right)$


---

### Approximation du nombre $\mathrm e$

$f'(x)=f(x)$, avec $f(0)=1$, cette équation (différentielle) a pour unique solution la fonction qu'on nomme **exponentielle**.

Pour $h$ petit, et $f$ dérivable,
* $f(x) \approx f(a) + f'(a)\times(x-a)$
* $f(x+h) \approx f(x) + f'(x)\times h$

$f(0)=1$, donc $f'(0)=1$, donc
* $f(0+\dfrac 1 n)\approx f(0) + f'(0)\times \dfrac 1 n$
* $f(0+\dfrac 1 n)\approx 1 +  \dfrac 1 n$, donc 
* $f(\dfrac 1 n)\approx 1 +  \dfrac 1 n$ et $f'(\dfrac 1 n)\approx 1 +  \dfrac 1 n$
* Avec $\dfrac 2 n = \dfrac 1 n +\dfrac 1 n$

* $f(\dfrac 1 n+\dfrac 1 n)\approx f(\dfrac 1 n) + f'(\dfrac 1 n)\times \dfrac 1 n$
* $f(\dfrac 1 n+\dfrac 1 n)\approx f(\dfrac 1 n)\times 1 + f(\dfrac 1 n)\times \dfrac 1 n$
* $f(\dfrac 2 n) \approx f(\dfrac 1 n) \times (1+\dfrac 1 n)$
* $f(\dfrac 2 n) \approx (1+\dfrac 1 n)^2$

...
* $f(\dfrac k n) \approx (1+\dfrac 1 n)^k$, où $k$ est entier.
* donc avec $k=n$, 
$f(1) \approx \left(1+\dfrac 1 n\right)^n$
> Ainsi $\mathrm e \approx \left(1+\dfrac 1 n\right)^n$

Cette première méthode converge très lentement **et mal**.

Voici un script Python pour tester $n$ de $1$ à $30$.

```py {cmd="python3"}
for n in range(1, 31):
    e_n = (1 + 1/n) ** n
    print("Avec n =", n, "on a l'approximation :", e_n)
```

Voici un autre script pour tester avec $n$ plus grand.

```py {cmd="python3"}
for i in range(1, 21):
    n = 10 ** i
    e_n = (1 + 1/n) ** n
    print("Avec n = 10 ^", i, "on a l'approximation :", e_n)
```

On voit que pour $n>10^{12}$ l'approximation devient de plus en plus mauvaise. Et elle n'était pas très bonne avant non plus !!! 
> L'explication vient du fait que, quand $n$ est grand, $1+\frac 1 n$ perd énormément en précision, à tel point même, qu'à un moment, la machine l'arrondit à $1.0$

### Meilleure approxmation de $\mathrm e$
Une autre méthode d'approximation utilise la formule $\mathrm e = \displaystyle\sum_{n=0}^{+\infty}\dfrac 1 {n!}$, où $n! = 1\times 2 \times 3 \cdots \times n$

```py{cmd="python3"}
from math import factorial
for n_sup in range(20):
    e_approx = sum(1 / factorial(n) for n in range(n_sup))
    print("Avec n_sup =", n_sup, ", on a l'approximation :", e_approx)
```

On constate une excellente approximation, et très rapide.

Obtenu avec VSCodium.
# Introduction à l'exponentielle

D'abord quelques rappels
##  Formules sur les fractions

Pour $a, b\in \mathbb R^*$, et $n, m \in \mathbb Z$
* $a^n \times a^m = a^{n+m}$
* $(a^n)^m = a^{n\times m}$
* $a^n \times b^n = (a\times b)^n$
* $\dfrac{a^n}{a^m} = a^{n-m}$ , et aussi $\dfrac{1}{a^n} = a^{-n}$
* $a^0 = 1$, $a^1 = a$, $a^2 = a\times a$, ...
* $\dfrac{a^n}{b^n} = \left(\dfrac{a}{b}\right)^n$ 

### Correction, exercice du livre
1.  $2^4 \times 2^7 \times 2^3 = 2^{4+7+3} = 2^{14}$
2. $6^4 \times 6^{-9} = 6^{4+(-9)} = 6^{-5}$
3. $3^2 \times 9^4$, deux pistes
    * $9\times 9^4 = 9^1\times 9^4 = 9^5$
    * $3^2 \times (3^2)^4 = 3^2 \times 3^8 = 3^{10}$
    * $3^2 \times (3^2)^4 = (3^2)^5 = 3^{10}$
4. $2^5\times3^5 = (2\times3)^5 = 6^5$
5. $\dfrac{2^8\times2^{-4}}{2^{-1}\times2^3} = 2^{(8+(-4)) - ((-1)+3)} = 2^2$
5. $\dfrac{2^8\times2^{-4}}{2^{-1}\times2^3} = 2^8\times2^{-4}\times2^1\times2^{-3} = 2^2$

## Sur les dérivées

Soit $f$, $g$ sont des fonctions dérivables.
* Si $f(x) = ax+b$, alors $f'(x)=a$
* Avec $n\in\mathbb N^*$, si $f(x) = x^n$, alors $f'(x)=n\times x^{n-1}$
* $(f+g)'= f'+g'$
* $(fg)' = f'g + fg'$
* si $g$ ne s'annule pas, $\left(\dfrac f g\right)' =
\dfrac{f'g - fg'}{g^2}$
* (Hors programme) $f(g(x))' = f'(g(x))\times g'(x)$
* (Au programme, $g$ affine) $f(ax+b)'= a\times f'(ax+b)$



### Exercice (exponentielle)

On admet que $f(0)=1$, et $f'(x)=f(x)$ pour tout $x\in\mathbb R$.

On pose $g(x) = f(x)\times f(-x)$, calculons $g'$.

Calculons d'abord, avec $b=0$ et $a=-1$ :
* $(f(-x))' = (-1) \times f'(-x) = - f(-x)$

Dérivons $g$ :
* $g'(x) = f'(x)\times f(-x) + f(x)\times -f(-x)$
* $g'(x) = f(x)\times f(-x) - f(x)\times f(-x)$
* $g'(x)= 0$, pour tout $x\in\mathbb R$
* Donc $g(x)$ est constante, égale à $g(0) = f(0)\times f(-0) = 1^2 =1$

> Conclusion
>* $g(x)=1$, pour tout $x\in\mathbb R$
>* $f(x)\times f(-x) = 1$, pour tout $x\in\mathbb R$
>* Et donc $f(-x) = \dfrac 1 {f(x)}$, pour tout $x\in\mathbb R$







## Cours
### Définition
La fonction exponentielle s'écrit :
* $x\mapsto \exp(x)$
*  ou $x\mapsto \mathrm e ^x$

$\exp$ est définie et dérivable sur $\mathbb R$, avec :
* L'image de zéro :
    * $\exp(0)=1$
    * $\mathrm e^0 = 1$

* la dynamique :
    * $\exp'(x) = \exp(x)$
    * $(\mathrm e^x)' =\mathrm e^x$

### Des formules
Pour tout $x\in\mathbb R$, on a :
* $\exp(-x)=\dfrac 1 
{\exp(x)}$

---

Devoirs (maths) : Lire la suite du cours p 160 et 161
Ex 24, 25 p 171

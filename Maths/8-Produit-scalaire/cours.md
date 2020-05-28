# Produit scalaire

## Définition

Le produit scalaire de deux vecteurs indique le défaut d'orthogonalité entre deux vecteurs, avec :
* $\vec u = \binom{x}{y}$
* $\vec v = \binom{x'}{y'}$

On définit le produit scalaire de $\vec u$ par $\vec v$ :
$$\vec u \cdot \vec v = xx'+yy'$$

## Propriétés

### Commutativité

Si $\vec u = \binom x y$ et $\vec v = \binom{x'}{y'}$ sont deux vecteurs, alors leur **produit scalaire est commutatif** :
$$\vec u \cdot \vec v = \vec v \cdot \vec u$$

> Preuve :
> * $\vec u \cdot \vec v = xx'+yy'$
> * $\vec v \cdot \vec u = x'x+y'y$
* Or les multiplications **réelles** $xx'$ et $yy'$ sont **commutatives**, et donc égales à $x'x$ et $y'y$. Ainsi **le produit scalaire est commutatif**.

### Distributivité

On rappelle **la distributivité de la multiplication des réels par rapport à l'addition des réels**.
$$k(a+b) = ka+kb$$

On a de même, **la distributivité du produit scalaire par rapport à l'addition des vecteurs** :
$$\vec u \cdot (\vec v + \vec w) = \vec u \cdot \vec v + \vec u \cdot \vec w$$

> Preuve, avec :
> * $\vec u = \binom x y$
> * $\vec v = \binom {x'} {y'}$
> * $\vec w = \binom {x''} {y''}$
> * On a d'une part :
>   * $\vec v + \vec w = \binom{x'+x''}{y'+y''}$
>    * ainsi $\vec u \cdot (\vec v + \vec w) =x(x'+x'') + y(y'+y'')$
>    * d'où $\vec u \cdot (\vec v + \vec w) = (xx'+yy') + (xx''+yy'')$, par simple distributivité *de la multiplication par rapport à l'addition* **avec les nombres réels**.
>* d'autre part :
>    * $\vec u \cdot \vec v + \vec u \cdot \vec w = (xx'+yy') + (xx''+yy'')$
>* D'où l'égalité. $\square$

### Autre définition équivalente

$$\vec u \cdot \vec v = ||u|| × ||v|| × \cos(\vec u, \vec v)$$

### À retenir

Le produit scalaire indique un défaut d'orthogonalité, et $\vec u \cdot \vec v = 0$ signifie que $\vec u$ et $\vec v$ sont orthogonaux.

Au passage, si $\vec u = \vec 0 = \binom 0 0$, alors $\vec u$ est orthogonal à tout vecteur $\vec v$.


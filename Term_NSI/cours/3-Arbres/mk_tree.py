def mk_peigne(h):
    ans = """
```dot
digraph expression
{
"""
    ans += f'    label = "Arbre peigne gauche de hauteur {h}"'

    if h > 0:
        ans += """
    "0" [label=""];
"""

        for i in range(h-1):
            ans += f"""
    "{i+1}" [label=""];
    "{i+1}d" [label="",shape=plaintext];
    "{i}" -> "{i+1}";
    "{i}" -> "{i+1}d" [style=dashed, arrowhead=none];
"""
        ans += f"""
    "{h}" [label="",shape=plaintext];
    "{h}d" [label="",shape=plaintext];
    "{h-1}" -> "{h}" [style=dashed, arrowhead=none];
    "{h-1}" -> "{h}d" [style=dashed, arrowhead=none];
"""
        ans += """
}
```
"""
    return ans

#print(mk_peigne(4))

def mk_parfait(h):
    ans = """
```dot
digraph expression
{
"""
    ans += f'    label = "Arbre parfait de hauteur {h}"'

    if h > 0:
        ans += """
    "1" [label=""];
"""

        for i in range(h-1):
            for x in range(2**i, 2*2**i):
                ans += f"""
    "{2*x+0}" [label=""];
    "{2*x+1}" [label=""];
    "{x}" -> "{2*x+0}" ;
    "{x}" -> "{2*x+1}" ;
"""

        ans1 = ""
        for x in range(2**(h-1), 2**h):
            ans1 += f"""
"{2*x+0}" [label="",shape=plaintext];
"{2*x+1}" [label="",shape=plaintext];
"{x}" -> "{2*x+0}" [style=dashed, arrowhead=none];
"{x}" -> "{2*x+1}" [style=dashed, arrowhead=none];
"""
        ans += """
}
```
"""
    return ans

#print(mk_parfait(4))


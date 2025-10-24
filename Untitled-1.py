# Cellule 1: définition d'outils de base
from itertools import product

def implique(p, q):
    """Renvoie la valeur logique de (p ⇒ q)."""
    return (not p) or q

# Test rapide
print('implique(True, False) ->', implique(True, False))  # doit afficher False
print('implique(False, True) ->', implique(False, True))  # doit afficher True
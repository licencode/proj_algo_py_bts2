s = "alphabet"
liste = ["H","e","l","l","o"]
"""
Mais attention, l'objet "l" est générateur qui ne peut être traversé qu'une fois
(et le transformer en ligne le travese)
"""

l = enumerate(l)
print(l) # adresse la variable "l"
print(list(l))

"""
Pour à nouveau accéder aux valeurs, il suffit de créer un nouveau générateur:
"""

l = enumerate(s)
print(l) # adresse la variable "l"
print(list(l))


a = int(input("ddd: "))

try:
    if a < 5:
        print("la v")
except TypeError:
    print("zzzz")
    
a = int(input("ddd: "))
b = int(input("ddd: "))
try:
    print(a/b)
except TypeError:
    print("Vous avez ajouté des valeurs de types incompatibles")
except ZeroDivisionError:
    print("Division par 0")
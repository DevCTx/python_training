""" Label Break/Goto are not allowed in Python """

# externe_label:
for i in range(3):
    for j in range(3):
        if i == j:
            break # externe_label         # Not allowed in Python
        print(i, j)
    print("Fin de la boucle interne")
print("Fin du programme")

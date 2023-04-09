import math

# fonction pour convertir des degrés en radians
def deg_to_rad(degrees):
    return degrees * math.pi / 180.0

# fonction pour convertir des radians en degrés
def rad_to_deg(radians):
    return radians * 180.0 / math.pi

# fonction pour convertir des degrés en millièmes
def deg_to_mil(degrees):
    return degrees * 6400 / 360

# fonction pour convertir des millièmes en degrés
def mil_to_deg(mil):
    return mil * 360 / 6400

# fonction pour convertir des radians en millièmes
def rad_to_mil(radians):
    return radians * 6400 / (2 * math.pi)

# fonction pour convertir des millièmes en radians
def mil_to_rad(mil):
    return mil * 2 * math.pi / 6400

# afficher l'interface utilisateur pour choisir la conversion
print("Conversion d'angles:")
print("1. Convertir des degrés en radians")
print("2. Convertir des radians en degrés")
print("3. Convertir des degrés en millièmes")
print("4. Convertir des millièmes en degrés")
print("5. Convertir des radians en millièmes")
print("6. Convertir des millièmes en radians")

# demander à l'utilisateur de choisir une option
option = input("Entrez votre choix (1 à 6): ")

# traiter l'option sélectionnée
if option == "1":
    # conversion de degrés en radians
    degrees = float(input("Entrez l'angle en degrés: "))
    radians = deg_to_rad(degrees)
    print(f"{degrees} degrés équivalent à {radians} radians.")
elif option == "2":
    # conversion de radians en degrés
    radians = float(input("Entrez l'angle en radians: "))
    degrees = rad_to_deg(radians)
    print(f"{radians} radians équivalent à {degrees} degrés.")
elif option == "3":
    # conversion de degrés en millièmes
    degrees = float(input("Entrez l'angle en degrés: "))
    mil = deg_to_mil(degrees)
    print(f"{degrees} degrés équivalent à {mil} millièmes.")
elif option == "4":
    # conversion de millièmes en degrés
    mil = float(input("Entrez l'angle en millièmes: "))
    degrees = mil_to_deg(mil)
    print(f"{mil} millièmes équivalent à {degrees} degrés.")
elif option == "5":
    # conversion de radians en millièmes
    radians = float(input("Entrez l'angle en radians: "))
    mil = rad_to_mil(radians)
    print(f"{radians} radians équivalent à {mil} millièmes.")
elif option == "6":
    # conversion de millièmes en radians
    mil = float(input("Entrez l'angle en millièmes: "))
    radians = mil_to_rad(mil)
    print(f"{mil} millièmes équivalent à {radians} radians.")
else:
    # option invalide
    print("Option invalide. Veuillez sélectionner une option entre 1 et 6.")

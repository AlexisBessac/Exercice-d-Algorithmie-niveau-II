#Trier des nombres par ordre croissant ou non

nombre_a = float(input("Veuiller saisr un nombre : "))
nombre_b = float(input("Veuiller sasir un nombre : "))
nombre_c = float(input("Veuiller sasir un nomnre : "))

if nombre_a < nombre_b and nombre_b < nombre_c:
    print("C'est croissant")
elif nombre_a > nombre_b > nombre_c:
    print("Les nombres sont décroissants")
else:
    print("Ce n'est pas trié")
#Calculer la moyenne d'un élève avec des coefficients

note_fr= float(input("Veuiller sasir la note de français sur 20 : "))
coeff_fr= int(input("Veuiller saisir le coefficient de français sur 10 : "))

note_math= float(input("Veuiller saisir la note de maths sur 20 : "))
coeff_math= int(input("Veuiller saisir le coefficient de maths sur 10 : "))

note_geom= float(input("Veuiller saisir la note de géomètrie sur 20 : "))
coeff_geom= int(input("Veuiller saisir le coefficient de géométrie sur 10 : "))

note_info= float(input("Veuiller saisir la note d'informatique sur 20 : "))
coeff_info= int(input("Veuiller saisir le coefficient d'informatique sur 10 : "))

moyenne= ((note_fr*coeff_fr) + (note_math*coeff_math) + (note_geom*coeff_geom) + (note_info*coeff_info))/(coeff_fr + coeff_math + coeff_geom + coeff_info)

#Arrondie de la moyenne de l'élève 
moyenne=round(moyenne,1)

print(f"La moyenne de l'élève est de {moyenne} sur 20")
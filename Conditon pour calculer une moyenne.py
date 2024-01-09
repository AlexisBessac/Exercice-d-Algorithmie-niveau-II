#Calculer la moyenne d'un élève

note_fr= float(input('Veuiller sasir la note de français sur 20 : '))
note_maths= float(input("Veuiller sasir la note de maths sur 20 : "))
note_geo= float(input("Veuiller sasir la note de géographie sur 20 :"))
note_info= float(input("Veuiller sasir la note d'informatique sur 20 : "))

moyenne= (note_fr+note_maths+note_geo+note_info)/4

if moyenne >= 16 and moyenne <= 20:
    print("Très bien")
elif moyenne >= 12 and moyenne < 16:
    print("Bien")
elif moyenne >= 8 and moyenne < 12:
    print("Assez Bien")
elif moyenne >= 4 and moyenne < 8:
    print("Insuffisant")
elif moyenne > 0 and moyenne < 4:
    print("Nul")
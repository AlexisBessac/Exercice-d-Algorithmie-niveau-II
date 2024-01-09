#Connaître la température d'une centrale nucléaire

temperature_ambiante= float(input("Veuiller sasir une température en degré celsius: "))
temperature_bassin= float(input("Veuiller sasir une teù^érature en degré celsius : "))

temperature= abs(temperature_ambiante-temperature_bassin)

if temperature < 20 or temperature > 40:
    print("Alarme")
mass_str= input("Gebe bitte dein Gewicht ein")
height_str = input("Gebe bitte deine KoerperGroesse in m ein")

mass=  float(mass_str.replace(",", "."))
height=  float(height_str.replace(",", "."))
#Falls kein Komma eingegeben wurde, passiert nichts!

bmi= mass/(height**2)
print(f"Dein BMI betraegt: {bmi:.2f}")

print("Dein BMI betraegt: " +str(round(bmi, 3)))
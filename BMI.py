height = float(input("Enter the Height: "))
weight = float(input("Enter the Weight: "))

bmi = weight / (height/100)**2
print("Your BMI is -" , bmi)

if bmi <= 18.5:
    print(" You are Under Weight")
    
elif bmi >= 24.5:
    print("You are Healthy")

elif bmi >= 29.9:
    print("You are Over Weight")

elif bmi >= 34.5:
    print("You are Severely Over Weight")

elif bmi >= 39.5:
    print("Obese")

else:
    print("Consult a Doctor")

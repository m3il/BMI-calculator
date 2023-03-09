wInput = int(input("Choose weight measurement:\n 1)KG\n 2)Lbs: "))
hInput = int(input("Choose height measurement:\n 1)Meters\n 2)cm\n 3)Feet"))

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if (wInput == 2):
    weight = weight * 0.45
else:
    weight = weight

if(hInput == 2):
    height = height * 0.01
elif(hInput == 3):
    height = height * 0.30
else:
    height = height


calculatedBMI = weight / (height ** 2)

if calculatedBMI < 18.5:
    print("Underweight")
elif calculatedBMI >= 18.5 and calculatedBMI < 25:
    print("Normal")
elif calculatedBMI >= 25 and calculatedBMI < 30:
    print("Overweight")
elif calculatedBMI >= 30:
    print("Obesity")
else:
    print("ERROR")

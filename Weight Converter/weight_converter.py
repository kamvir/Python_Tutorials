title = "============================== Weight Converter =============================="

print(title)

weight = int(input("Weight: "))

weight_entered_in = input("(L)bs or (K)g: ")

if weight_entered_in.lower() == "l":
    converted = weight * 0.45
    print("You are " + str(converted) + " kilos")
else:
    converted = weight / 0.45
    print("You are " + str(converted) + " pounds")

print(title)

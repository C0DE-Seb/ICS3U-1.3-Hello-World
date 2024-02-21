print("Restaurat Bill Splitter")

people=int(input("\nHow many people in your group? "))
bill=float(input("What was the total bill after tax? "))
tip=int(input("How much do you want to tip (standard is 15%)? "))

pay=(bill+(bill/1.13)*(tip/100))/people

print("\nEach person should pay $"+str(format(pay, ".2f")))
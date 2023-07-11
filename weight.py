weight = int(input("Enter the weight: "))
unit = input("(K)g or (L)bs? ")
if unit.lower() == "l":
  result = weight * 0.45
  print("Your weight in Kg is: " + str(result))
	
elif unit.lower() == "k":
		result = weight / 0.45
		print("Your weight in Lbs is: " + str(result))
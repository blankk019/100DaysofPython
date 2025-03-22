#tip calculator program
#this program calculates the tip for a given bill
print("welcome to the tip calculator program")
bill = int(input("what was the total of the bill?? "))
tip  = int(input("how much bill would you like to give 10, 12 or 15?"))
NumberOfPeople = int(input("what is the number of people?"))
print(f"Each person should pay ${round((bill*(tip / 100))/5)}")
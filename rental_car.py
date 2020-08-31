import sys

#Collect Customer Rental Data

#set rate variables for types of rental charges
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

#Request Rental code
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

#Calculate rental code charges

# Check for code type D or B (since they are both similar charge types)
if (rentalCode == 'D' or rentalCode == 'B'):
  #Input from user for the amount of days rented
  rentalPeriod = input("Number of Days Rented:\n")
  #Check to see if rentalCode is D
  if(rentalCode == 'D'):
    #Calculate rate based on daily type of rental
    baseCharge = float(rentalPeriod) * daily_charge
#Otherwise rentalCode is B
  else:
    #Calculate rate based on budget type of rental
    baseCharge = float(rentalPeriod) * budget_charge

#if rental code is W
elif (rentalCode == 'W'):
  #Get input for number of weeks rented
  rentalPeriod = input("Number of Weeks Rented:\n")
  #Calculate rate based on weekly type of rental
  baseCharge = float(rentalPeriod) * weekly_charge

#Collect Mileage Rental Data

#Getting user input for the starting odometer reading; saving value as variable odoStart
odoStart = input("Starting Odometer Reading:\n")

#Getting user input for ending odometer reading; saving value as variable odoEnd
odoEnd = input("Ending Odometer Reading:\n")

#Calculating total miles traveled and saving value as totalMiles variable
totalMiles = int(odoEnd) - int(odoStart)

#Calculate mileage charges

#If rental code is B or budget, mile charge is total miles * 0.25
if (rentalCode == 'B'):
  mileCharge = float(totalMiles) * 0.25
#If rental code is D or daily, average miles is totalMiles/rentalPeriod
elif(rentalCode == "D"):
  averageDayMiles = totalMiles/int(rentalPeriod)
  #If the average miles are <= 100, extra miles is 0
  if(averageDayMiles <= 100):
    extraMiles = 0
  #Else if the average miles is > 100, subtract 100 from average daily miles
  elif(averageDayMiles > 100):
    extraMiles = averageDayMiles - 100
  #Charge 0.25 for each extra miles
  mileCharge = extraMiles * 0.25

#If rental code is W or weekly, average miles is totalMiles/rentalPeriod
elif(rentalCode == 'W'):
  averageWeekMiles = totalMiles/int(rentalPeriod)
  #If averageMiles exceeds 900 miles, multiply 100.00 * rentalPeriod
  if(averageWeekMiles > 900):
    mileCharge = float(rentalPeriod) * 100.00
  #If averageMiles does not exceed 900 miles, mile charge is 0.00
  else:
    mileCharge = 0.00

#Print out results
amtDue = baseCharge + mileCharge
print("Rental Summary")
print("Rental Code: " + rentalCode)
print("Rental Period: " + rentalPeriod)
print("Starting Odometer: " + odoStart)
print("Ending Odometer: " + odoEnd)
print("Miles Driven: " + str(totalMiles))
print("Amount Due: $%.2f" %amtDue)
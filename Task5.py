#Task5
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month = input("Input the name of Month: ")

if month == "February":
	print("No. of days: 28/29 days")
elif month in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 days")
else:
	print("Wrong month") 
 
def generateNumberString(vel, length, maxVal):
	number = vel
	if number > maxVal:
		number = maxVal
	if number < 0:
		number = 0
	stringified = str(vel).zill(length)
	return stringified






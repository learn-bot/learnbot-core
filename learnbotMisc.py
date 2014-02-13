 
def generateMotorVelString(vel):
	number = vel
	if number > 255:
		number = 255
	if number < 0:
		number = 0

	stringified = str(vel).zill(3)
	
	return stringified





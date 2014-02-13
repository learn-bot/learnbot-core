 
def generateNumberString(vel, length, maxVal):
	number = vel
	if number > maxVal:
		number = maxVal
	if number < 0:
		number = 0
	stringified = str(vel).zfill(length)
	return stringified



def estimateMotorsFromVelocity(advance, steer):
	if advance > 0.001:
		return 0, 0, 0, 0
	elif advance < -0.001:
		return 0, 1, 0, 1
	else:
		return 255, 0, 255, 0




 
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

def nativeVelocity(rightvel, rightdir, leftvel, leftdir):
  if rightvel < 0:
    rightvel = 0
  if leftvel < 0:
    leftvel = 0
  if rightvel > 255:
    rightvel = 255
  if leftvel > 255:
    leftvel = 255
  if rightdir < 0:
    rightdir = 0
  if leftdir < 0:
    leftdir = 0
  if rightdir > 1:
    rightdir = 1
  if leftdir > 1:
    leftdir = 1
  convrightvel = 255 - rightvel
  convleftvel = 255 - leftvel
  return convrightvel, rightdir, convleftvel, leftdir

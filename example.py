import sys, time
import LearnBotClient

class MiClase(LearnBotClient.Client):
	def __init__(self):
		pass
	def code(self):
		while True:
			sonars = self.getSonars()
			#print sonars.SFRONT.VALUES[0]
			if sonars.SFRONT.VALUES[0] > 10:
				self.setVel(1., 0.)
			else:
				self.setVel(0., 0.)
			time.sleep(0.001)



miclase = MiClase()
miclase.main(sys.argv)



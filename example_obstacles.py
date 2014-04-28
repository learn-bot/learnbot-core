import sys, time
import LearnBotClient

# El robot se mueve hasta llegar a menos de 10 cm de un objeto
class MiClase(LearnBotClient.Client):
	def __init__(self):
		pass
	def code(self):
		while True:
			sonars = self.getSonars()
			if sonars['FRONT'].distance > 0.1:
				self.setVel(255,1,255,1)
			else:
				self.setVel(0,0,0,0)
			time.sleep(0.001)



miclase = MiClase()
miclase.main(sys.argv)



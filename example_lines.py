import sys, time
import LearnBotClient

# El robot se mueve hasta llegar a menos de 10 cm de un objeto
class MiClase(LearnBotClient.Client):
	def __init__(self):
		pass

	def code(self):
		self.setVel(0,1,0,1)

		while True:
			lines = self.getLines()

			izq = lines['LEFT1'].value
			der = lines['RIGHT1'].value
			cen = (lines['LEFT2'].value + lines['RIGHT2'].value) / 2
			
			
			velg = 50
			velf = 100
			print cen
			if cen < 400:
				self.setSpeeds(velf, 0)
				print 'frente'
			else:
				if izq > der:
					print 'der'
					self.setSpeeds(velg, 0.5)
				else:
					print 'izq'
					self.setSpeeds(velg, -0.5)


miclase = MiClase()
miclase.main(sys.argv)



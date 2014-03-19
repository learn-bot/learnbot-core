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
			

			if cen < 700:
				self.setVel(70,1,70,1)
				#print 'frente'
			else:
				if izq > der:
					#print 'der'
					self.setVel(0,1,70,1)
				else:
					#print 'izq'
					self.setVel(70,1,0,1)
			
			#print izq, cen, der
			time.sleep(0.1)


miclase = MiClase()
miclase.main(sys.argv)



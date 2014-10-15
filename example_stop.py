import sys, time
import LearnBotClient

# El robot se mueve hasta llegar a menos de 10 cm de un objeto
class MiClase(LearnBotClient.Client):
	def __init__(self):
		pass

	def code(self):
		self.setVel(0,1,0,1)


miclase = MiClase()
miclase.main(sys.argv)



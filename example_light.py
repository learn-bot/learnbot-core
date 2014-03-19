import sys, time
import LearnBotClient

# El robot se mueve hasta llegar a menos de 10 cm de un objeto
class MiClase(LearnBotClient.Client):
	def __init__(self):
		pass
	def code(self):
		self.setVel(0,1,0,1)
		while True:
			light = self.getLDR()

			#print light
			valores = [ light['FRONT'].value, light['BACK'].value, light['LEFT'].value, light['RIGHT'].value ]
			print valores
			maximum = max(valores)
			
			if maximum > 200:
				print maximum
				if light['FRONT'].value == maximum:
					self.setVel(200,1,200,1)
					print 'frente'
				elif light['LEFT'].value == maximum:
					self.setVel(200,1,200,-1)
					print 'izq'
				elif light['RIGHT'].value == maximum:
					self.setVel(200,-1,200,1)
					print 'der'
				else:
					self.setVel(200,1,200,-1)
					print 'b'
			else:
				self.setVel(0,1,0,1)
			

			time.sleep(0.1)


miclase = MiClase()
miclase.main(sys.argv)



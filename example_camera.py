import sys, time
import LearnBotClient

# Ctrl+c handling
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Grabamos una imagen a un fichero "camara.jpeg"
class MiClase(LearnBotClient.Client):
	def __init__(self):
		pass

	def code(self):
		while True:
			imagen = self.getImage(80,60)
			suma = 0
			for p in imagen:
				suma += p
			suma /= len(imagen)
			print suma
			time.sleep(1)

miclase = MiClase()
miclase.main(sys.argv)



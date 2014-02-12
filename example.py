import sys, time
import LearnBotClient

class MiClase(LearnBotClient.Client):
	def code(self):
		while True:
			print self.getSonars()
			time.sleep(1)


miclase = MiClase()
miclase.main(sys.argv)

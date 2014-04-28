#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, traceback, Ice, threading
import serial
import time
import json
from collections import namedtuple

import os
os.chdir("/home/pi/learnbot-core/")

Ice.loadSlice("LearnBot.ice")
import LearnBotModule

class LearnBotHandler (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		#Apertura del puerto serie donde está conectada la placa arduino
		self.arduino = serial.Serial('/dev/ttyAMA0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
		self.arduino.close()
		self.arduino.open()
		#Espera 3 segundos
		print("Preparing port ...")
		time.sleep(1)
		if self.arduino.isOpen():
			print("COM Port is open.")
		else:
			raise 'pene'
		self.output = None
		self.command("?-1?")
	def run(self):
		while 1:
			time.sleep(1)
	def command(self, command):
		if self.arduino.isOpen():
			self.arduino.write(command.encode("us-ascii"))
			while True:
				response = self.arduino.readline()
				if response != str('').encode("us-ascii"):
					return response.decode("UTF-8")
		else:
			return ''
	def shutdown(self):
		self.command("?-2?")
		import subprocess
		subprocess.call(["shutdown", "-h", "now"])


class LearnBotI (LearnBotModule.LearnBot):
	def __init__(self, _handler):
		self.handler = _handler
	def command(self, c, current=None):
		return self.handler.command(c)
	def shutdown(self, current=None):
		self.handler.shutdown()



class Server(Ice.Application):
	def run(self, argv):
		status = 0
		try:
			self.shutdownOnInterrupt()
			print 'Run handler'
			handler = LearnBotHandler()
			print 'handler activated'
			handler.start()
			adapter = self.communicator().createObjectAdapter('LearnBot')
			print adapter
			adapter.add(LearnBotI(handler), self.communicator().stringToIdentity('learnbot'))
			print self.communicator().stringToIdentity('learnbot')
			adapter.activate()
			self.communicator().waitForShutdown()
		except:
			traceback.print_exc()
			status = 1

		print 'aaaa'

		if self.communicator():
			try:
				self.communicator().destroy()
			except:
				traceback.print_exc()
				status = 1

Server().main(sys.argv)

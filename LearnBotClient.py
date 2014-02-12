#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, traceback, Ice, os
import json
from collections import namedtuple

Ice.loadSlice("LearnBot.ice")
import LearnBotModule

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

ic = None

class Client(Ice.Application):
	def __init__(self, clase):
		self.clase = clase
	def run(self, argv):
		global ic
		status = 0
		self.shutdownOnInterrupt()
		ic = self.communicator()

		# Get connection config
		try:
			proxyString = ic.getProperties().getProperty('LearnBotProxy')
		except:
			print 'Cannot get LearnBotProxy property.'
			return

		# Remote object connection
		try:
			baseStr = self.communicator().stringToProxy(proxyString)
			self.learnbotPrx = LearnBotModule.LearnBotPrx.checkedCast(baseStr)
		except:
			print 'Cannot connect to the remote object.'
			return

		self.code()

	def json2obj(self, response):
		return json.loads(response.decode("utf-8"), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

	def getSonars(self):
		sonarReq = str("?0?").encode("us-ascii")
		return self.json2obj(self.learnbotPrx.command(sonarReq))
	
	def getLines(self):
		lineReq = str("?1?").encode("us-ascii")
		return self.json2obj(self.learnbotPrx.command(lineReq))
		
	def getLDR(self):
		ldrReq = str("?2?").encode("us-ascii")
		return self.json2obj(self.learnbotPrx.command(ldrReq))



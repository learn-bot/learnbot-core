#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, traceback, Ice, os
import json
from collections import namedtuple

Ice.loadSlice("LearnBot.ice")

import LearnBotModule

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from learnbotMisc import *


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
			sys.exit(1)

		# Remote object connection
		try:
			baseStr = self.communicator().stringToProxy(proxyString)
			print baseStr
			self.learnbotPrx = LearnBotModule.LearnBotPrx.checkedCast(baseStr)
		except:
			print 'Cannot connect to the remote object.'
			sys.exit(1)

		self.code()
		
	def sendCommand(self, command):
		string = self.learnbotPrx.command(command.encode("us-ascii"))
		print string
		return self.json2obj(string)

	def json2obj(self, response):
		return json.loads(response.decode("utf-8"), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

	###
	### API
	###
	def getSonars(self):
		return self.sendCommand("?0?")
	
	def getLines(self):
		return self.sendCommand("?1?")
		
	def getLDR(self):
		return self.sendCommand("?2?")

	def setVel(self, advance, steer):
		leftVel, leftDir, rightVel, rightDir = estimateMotorsFromVelocity(advance, steer)
		speedReq = ''
		speedReq += 'M'
		speedReq += generateNumberString(rightVel, 3, 255)
		speedReq += ':'
		speedReq += generateNumberString(rightDir, 1, 1)
		speedReq += ':'
		speedReq += generateNumberString(leftVel, 3, 255)
		speedReq += ':'
		speedReq += generateNumberString(leftDir, 1, 1)
		speedReq += 'M'
		return self.sendCommand(speedReq)
		
		
		
		










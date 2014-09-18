#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, traceback, Ice, os
import json
from collections import namedtuple

Ice.loadSlice("LearnBot.ice")
Ice.loadSlice("DifferentialRobot.ice")

import LearnBotModule
import RoboCompDifferentialRobot


import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from learnbotMisc import *

ic = None

class SonarData(object):
	def __init__(self):
		self.distance = 0
		self.height = 0
		self.angle = 0

class LineData(object):
	def __init__(self):
		self.value = 0

class LightData(object):
	def __init__(self):
		self.value = 0

class Client(Ice.Application):
	def __init__(self, clase):
		self.clase = clase
	def run(self, argv):
		global ic
		status = 0
		self.shutdownOnInterrupt()
		ic = self.communicator()

		self.realLearnbot = True
		# Get connection config
		try:
			proxyString = ic.getProperties().getProperty('LearnBotProxy')
			if len(proxyString)<4: self.realLearnbot = False
		except:
			print 'Cannot get LearnBotProxy property.'
			self.realLearnbot = False

		if self.realLearnbot:
			print 'real'
			try:
				baseStr = self.communicator().stringToProxy(proxyString)
				self.learnbotPrx = LearnBotModule.LearnBotPrx.checkedCast(baseStr)
			except:
				print 'Cannot connect to the remote object.'
				sys.exit(1)
		else:
			print 'simulado'
			# CONNECT TO SIMULATED DIFFERENTIAL ROBOT
			try:
				proxyString = ic.getProperties().getProperty('DifferentialRobotProxy')
				print 'DifferentialRobotProxy:', proxyString
				try:
					baseStr = self.communicator().stringToProxy(proxyString)
					self.differentialrobotPrx = RoboCompDifferentialRobot.DifferentialRobotPrx.checkedCast(baseStr)
				except:
					print 'Cannot connect to the remote object.'
					sys.exit(1)
			except:
				print 'Cannot get DifferentialRobotProxy property.'
				sys.exit(1)
			# CONNECT TO SIMULATED ULTRASOUNDS
			#
			#
			#
		self.code()
		
	def sendCommand(self, command):
		string = self.learnbotPrx.command(command.encode("us-ascii"))
		#print string
		return self.json2obj(string)

	def json2obj(self, response):
		return json.loads(response.decode("utf-8"), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

	###
	### API
	###
	def getSonars(self):
		r = self.sendCommand("?0?")
		ret = dict()
		
		left = SonarData()
		left.distance = 0.01 * r.SLEFT.VALUES[0]
		left.height = 0.05
		left.angle = r.SLEFT.DEGREES
		ret['LEFT'] = left
		ret['IZQ'] = left

		right = SonarData()
		right.distance = 0.01 * r.SRIGHT.VALUES[0]
		right.height = 0.05
		right.angle = r.SRIGHT.DEGREES
		ret['RIGHT'] = right
		ret['DER'] = right

		back = SonarData()
		back.distance = 0.01 * r.SBACK.VALUES[0]
		back.height = 0.05
		back.angle = r.SBACK.DEGREES
		ret['BACK'] = back
		ret['TRA'] = back

		front = SonarData()
		front.distance = 0.01 * r.SFRONT.VALUES[0]
		front.height = 0.05
		front.angle = r.SFRONT.DEGREES
		ret['FRONT'] = front
		ret['DEL'] = front

		return ret
	
	def getLines(self):
		r =  self.sendCommand("?1?")
		ret = dict()

		left1 = LineData()
		left1.value = r.LINE_LEFT_2.VAL
		ret['LEFT1'] = left1
		ret['IZQ1'] = left1

		right1 = LineData()
		right1.value = r.LINE_RIGHT_2.VAL
		ret['RIGHT1'] = right1
		ret['DER1'] = right1

		left2 = LineData()
		left2.value = r.LINE_LEFT_1.VAL
		ret['LEFT2'] = left2
		ret['IZQ2'] = left2

		right2 = LineData()
		right2.value = r.LINE_RIGHT_1.VAL
		ret['RIGHT2'] = right2
		ret['DER2'] = right2

		return ret

	def getLDR(self):
		r = self.sendCommand("?2?")
		ret = dict()

		front = LightData()
		front.value = r.LDR_FRONT.VAL
		ret['FRONT'] = front
		ret['DEL'] = front

		back = LightData()
		back.value = r.LDR_BACK.VAL
		ret['BACK'] = back
		ret['TRA'] = back

		left = LightData()
		left.value = r.LDR_LEFT.VAL
		ret['LEFT'] = left
		ret['IZQ'] = left

		right = LightData()
		right.value = r.LDR_RIGHT.VAL
		ret['RIGHT'] = right
		ret['DER'] = right

		return ret

	def setVel(self, rightVel, rightDir, leftVel, leftDir):
		if self.realLearnbot:
			rV, rD, lV, lD = nativeVelocity(rightVel, rightDir, leftVel, leftDir)
			speedReq = ''
			speedReq += 'M'
			speedReq += generateNumberString(rV, 3, 255)
			speedReq += ':'
			speedReq += generateNumberString(rD, 1, 1)
			speedReq += ':'
			speedReq += generateNumberString(lV, 3, 255)
			speedReq += ':'
			speedReq += generateNumberString(lD, 1, 1)
			speedReq += 'M'
			return self.sendCommand(speedReq)
		else:
			R = float(rightVel)
			if rightDir < 0: R *= 1
			L = float(leftVel)
			if leftDir < 0: L *= 1
			avance = (L+R)/2
			giro = (L-R)/((L+R)/2)
			self.differentialrobotPrx.setSpeedBase(avance, giro)
		
	def getImage(self, width=80, height=60):
		return map(ord, self.learnbotPrx.getImageFromRobot(width, height))
		
		










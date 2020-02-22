# -*- coding: UTF-8 -*-



import api
import appModuleHandler
from scriptHandler import script
from logHandler import log
import tones
import controlTypes


class AppModule(appModuleHandler.AppModule):
	def event_nameChange(self, object, nextHandler):
		self.sayIsTyping(object)
		nextHandler()
	
	def sayIsTyping(self, object):
		status = self.getObjectName(object)
		log.info(status)
		if status is None:
			return
		if self.isUserTyping(status):
			self.playSound()

	def playSound(self):
		tones.beep(256, 100)

	def isUserTyping(self, status):
		return 'печатает...' in status

	def getObjectName(self, object):
		return object.name.encode('UTF-8')
		
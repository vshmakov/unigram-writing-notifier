# -*- coding: UTF-8 -*-


from typing import Callable

import appModuleHandler
import tones
from NVDAObjects.UIA import UIA


class AppModule(appModuleHandler.AppModule):
	def event_nameChange(self, object: UIA, nextHandler: Callable) -> None:
		self.sayIsTyping(object)
		nextHandler()

	def sayIsTyping(self, object: UIA) -> None:
		status = self.getObjectName(object)
		if status is None:
			return
		if self.isUserTyping(status):
			self.playSound()

	def playSound(self) -> None:
		tones.beep(256, 100)

	def isUserTyping(self, status: str) -> bool:
		return 'печатает...' in status

	def getObjectName(self, object: UIA) -> str:
		return object.name

"""
Trigger nexus
"""

import logging

def ImportTrigger(params):
	if params["triggerController"] == "Arduino" or params["triggerController"] == "arduino":
		import campy.trigger.arduino as trigger
	elif params["triggerController"] is None:
		import campy.trigger.arduino as trigger
	else:
		print('The microcontroller you have selected is not supported.')
	return trigger


def StartTriggers(systems, params):
	if params["startArduino"]:
		if params["triggerController"] is not None:
			trigger = ImportTrigger(params)
			systems = trigger.StartTriggers(systems, params)
	return systems


def StopTriggers(systems, params):
	if params["startArduino"]:
		if params["triggerController"] is not None:
			trigger = ImportTrigger(params)
			trigger.StopTriggers(systems)
import sys

def setup(core, object):

	object = core.objectService.createObject('object/tangible/wearables/helmet/shared_helmet_fighter_imperial_ace.iff', object.getPlanet())
	object.setStringAttribute('condition', '100/100')
	object.setStringAttribute('volume', '1')
	
	inventory.add(object)
	

	return
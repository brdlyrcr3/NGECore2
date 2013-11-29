import sys

def setup(core, object):

	object = core.objectService.createObject('object/tangible/wearables/gloves/shared_appearance_invisible_s01.iff', object.getPlanet())
	object.setStringAttribute('condition', '100/100')
	object.setStringAttribute('volume', '1')
	inventory.add(object)
	
	return
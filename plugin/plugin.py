from Plugins.Plugin import PluginDescriptor

def autostart(reason, **kwargs):
	import servicemp3epl

def Plugins(**kwargs):
	return [
		PluginDescriptor(where = PluginDescriptor.WHERE_AUTOSTART, needsRestart = True, fnc = autostart)
	]

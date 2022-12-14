from itertools import zip_longest

def plug_connect(n_cable, n_socket, n_plug):
	return str("plug " + n_cable + " into " + n_socket + " using " + n_plug)

def welding_connect(n_cable, n_socket):
	return str("weld " + n_cable + " to " + n_socket + " without plug")

def ft_generator(g_plugs, g_sockets, g_cables):
	for pl, sc, cb in zip_longest(g_plugs, g_sockets, g_cables):
		if ((cb != None and sc != None and pl != None) 
				or (cb != None and sc != None)) == False:
			break
		yield plug_connect(cb, sc, pl) if cb and sc and pl else welding_connect(cb, sc)

def fix_wiring(cables, sockets, plugs):
	g_plugs = (filter(lambda elem: "plug" in str(elem), plugs))
	g_sockets = (filter(lambda elem: "socket" in str(elem), sockets))
	g_cables = (filter(lambda elem: "cable" in str(elem), cables))

	return ft_generator(g_plugs, g_sockets, g_cables)

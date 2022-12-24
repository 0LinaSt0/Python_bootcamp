from itertools import chain


def plug_connect(n_cable, n_socket, n_plug):
	return f"plug {n_cable} into {n_socket} using {n_plug}"


def welding_connect(n_cable, n_socket):
	return f"weld {n_cable} to {n_socket} without plug"


def tools_generator(tool, subname):
	return (filter(lambda elem: str(elem).startswith(subname), tool))


def fix_wiring(cables, sockets, plugs):
	g_plugs = tools_generator(plugs, "plug")
	g_sockets = tools_generator(sockets, "socket")
	g_cables = tools_generator(cables, "cable")

	return (plug_connect(tools[1], tools[2], tools[0])
		if len(tools) == 3 else welding_connect(tools[0], tools[1])
		for tools in chain(zip(g_plugs, g_cables, g_sockets), zip(g_cables, g_sockets)))

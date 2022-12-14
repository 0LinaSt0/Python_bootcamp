from energy import fix_wiring

def printing(cables, sockets, plugs):
	print("Coming:")
	print(plugs)
	print(sockets)
	print(cables)
	print("\n")
	print("Result:")

def test00():
	plugs = ['plug1', 'plug2', 'plug3']
	sockets = ['socket1', 'socket2', 'socket3', 'socket4']
	cables = ['cable1', 'cable2', 'cable3', 'cable4']
	printing(cables, sockets, plugs)
	return fix_wiring(cables, sockets, plugs)

def test01():
	plugs = ['plugZ', None, 'plugY', 'plugX']
	sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
	cables = ['cable2', 'cable1', False]
	printing(cables, sockets, plugs)
	return fix_wiring(cables, sockets, plugs)

def test02():
	plugs = []
	sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
	cables = ['cable2', 'cable1', False]
	printing(cables, sockets, plugs)
	return fix_wiring(cables, sockets, plugs)

def test03():
	plugs = ['plugZ', None, 'plugY', 'plugX']
	sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
	cables = []
	printing(cables, sockets, plugs)
	return fix_wiring(cables, sockets, plugs)

def test04():
	plugs = ['papa', 'pluww', 'PLU4']
	sockets = [1, 'socket1', ]
	cables = ['cable2', 'cable1', False]
	printing(cables, sockets, plugs)
	return fix_wiring(cables, sockets, plugs)


print("\n\t~~~~~TEST00~~~~\n")
for c in test00():
	print(c)

print("\n\t~~~~~TEST01~~~~\n")

for c in test01():
	print(c)

print("\n\t~~~~~TEST02~~~~\n")

for c in test02():
	print(c)
print("\n\t~~~~~TEST03~~~~\n")

for c in test03():
	print(c)

print("\n\t~~~~~TEST04~~~~\n")

for c in test04():
	print(c)
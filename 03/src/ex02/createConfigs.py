import yaml
from yaml.loader import SafeLoader
from configsClass import configs


YAML_PATH = "../../materials/todo.yml"
SRCS_PARH_REMOTE = "/home/msalena/Desktop/src"


def takeData():
	with open(YAML_PATH) as file:
		data = yaml.load(file, Loader=SafeLoader) # Safe subsets safely
	return data


def generateCommands(accounts):
	start_server_cmd = f"cd {SRCS_PARH_REMOTE} ; python3 -m http.server"
	generate_html_cmd = f"python3 {SRCS_PARH_REMOTE}/exploit.py"
	start_consumer_cmd = f"python3 {SRCS_PARH_REMOTE}/consumer.py -e {accounts[0]},{accounts[1]}"
	cmds = {
		"start service": start_server_cmd,
		"generate new html page" : generate_html_cmd,
		"start consumer with agruments" : start_consumer_cmd
	}
	return cmds


def createConfigs():
	data = takeData()
	cmds = generateCommands(data['bad_guys'])
	data['server']['exploit_files'].append("evilcorp.html")
	confs = configs("Deploy", "all", 5, "msalena",
					data['server']['install_packages'],
					data['server']['exploit_files'], cmds)
	return confs

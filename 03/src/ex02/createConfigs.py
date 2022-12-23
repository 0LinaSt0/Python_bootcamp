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
	bs4_install_cmd = f"pip3 install beautifulsoup4"
	redis_install_cmd = f"pip3 install redis"
	argparse_install_cmd = f"pip3 install argparse"
	start_server_cmd = f"{SRCS_PARH_REMOTE}/runserver.sh"
	generate_html_cmd = f"python3 {SRCS_PARH_REMOTE}/exploit.py"
	start_consumer_cmd = f"{SRCS_PARH_REMOTE}/runconsumer.sh"
	cmds = {
		"install beautifulsoup4": bs4_install_cmd,
		"install redis": redis_install_cmd,
		"install argparser": argparse_install_cmd,
		"start server": start_server_cmd,
		"generate new html page" : generate_html_cmd,
		"start consumer with agruments" : start_consumer_cmd
	}
	return cmds


def createConfigs():
	data = takeData()
	cmds = generateCommands(data['bad_guys'])
	data['server']['exploit_files'].append("evilcorp.html")
	data['server']['exploit_files'].append("runserver.sh")
	data['server']['exploit_files'].append("runconsumer.sh")
	data['server']['install_packages'].append("python3-pip")
	data['server']['install_packages'].append("redis-server")
	confs = configs("Deploy", "all", "true", 5, "msalena",
					data['server']['install_packages'],
					data['server']['exploit_files'], cmds)
	return confs

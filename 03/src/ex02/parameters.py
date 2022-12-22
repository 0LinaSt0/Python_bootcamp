
def aptModuleParameters(installable_name):
	param_dict = {
		"name": installable_name, #installable name
		"state": "latest" # installable vertion
	}
	return param_dict


def copyModuleParameters(localpath, destpath):
	param_dict = {
		"src": localpath, # local from
		"dest": destpath, # remote to
		"owner": "msalena", # user name
		"group": "msalena", # group name
		"mode": "777", # file permissions on remote server
	}
	return param_dict


def commandModuleParameters(cmd):
	param_dict = {
		"cmd": cmd
	}
	return param_dict


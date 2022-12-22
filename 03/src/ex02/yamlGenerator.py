import yaml


class yamlGenerator:
	def __init__(self, configs):
		self.yaml_dict = self.yamlStructure(configs)


	def yamlStructure(self, configs):
		members = [
			{
				"name": configs.project_name,
				"hosts": configs.hosts_configuration,
				"serial": configs.threads_max_count,
				"remote_user": configs.remote_user,
				"tasks": []
			}
		]
		return members


	def createModuleDescriprion(self, module_name, descriprion, parameters_dict):
		module = {
			"name": descriprion,
			module_name: {}
		}

		for key in parameters_dict:
			module[module_name][key] = parameters_dict[key]

		return module


	def addModule(self, descriprion, module_name, parameters_dict):
		module = self.createModuleDescriprion(module_name, descriprion,
												parameters_dict)
		self.yaml_dict[0]["tasks"].append(module)


	def dumpYaml(self, filepath):
		with open(filepath, 'w') as file:
			data = yaml.dump(self.yaml_dict, file, sort_keys=False) # don't sort the keys in alphabetical order
		return data





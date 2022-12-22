from createConfigs import createConfigs, SRCS_PARH_REMOTE
from yamlGenerator import *
from parameters import *


DEPLOY_PATH = "../../materials/deploy.yml"
SRCS_PATH = "srcs/"


def addInstallPackagesModes(gen_yaml, install_packages):
	mode = "ansible.builtin.apt"
	for package in install_packages:
		params = aptModuleParameters(package)
		gen_yaml.addModule(f"install {package}", mode, params)


def addCopyFilesModes(gen_yaml, exploit_files):
	mode = "ansible.builtin.copy"
	for file in exploit_files:
		params = copyModuleParameters(f"{SRCS_PATH}{file}",
										f"{SRCS_PARH_REMOTE}/{file}")
		gen_yaml.addModule(f"exploit {file}", mode, params)


def addCommandsModes(gen_yaml, cmds):
	mode = "ansible.builtin.command"
	for key in cmds:
		params = commandModuleParameters(cmds[key])
		gen_yaml.addModule(f"{key}", mode, params)


def createYamlFile(conf):
	gen_yaml = yamlGenerator(conf)
	addInstallPackagesModes(gen_yaml, conf.install_packages)
	addCopyFilesModes(gen_yaml, conf.exploit_files)
	addCommandsModes(gen_yaml, conf.cmds)
	return gen_yaml.dumpYaml(DEPLOY_PATH)



if __name__ == "__main__":
	conf = createConfigs()
	createYamlFile(conf)
	print("SUCCESS: ansible deploy list was created in \"../../materials/deploy.yml\"")

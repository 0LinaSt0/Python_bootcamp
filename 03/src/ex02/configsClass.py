
class configs:
	def __init__(self, project_name, hosts_configuration,
				sudo_rules, threads_max_count, remote_user_name,
				packages, files, cmds):
		self.project_name = project_name
		self.hosts_configuration = hosts_configuration
		self.sudo_rules = sudo_rules
		self.threads_max_count = threads_max_count
		self.remote_user = remote_user_name
		self.install_packages = packages
		self.exploit_files = files
		self.cmds = cmds



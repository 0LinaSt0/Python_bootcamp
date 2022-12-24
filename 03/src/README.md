Activate env:
```shell
. venv/bin/activate
```

Install requirement:
```shell
pip install -r requirements.txt
```

Intall needing utils:
```shell
pip3 install beautifulsoup4
pip3 install redis
pip3 install argparse
pip3 install ansible
```

EXECUTE EX00:
1. Start server in folder "materials/":
		```shell
		python3 -m http.server
		```
2. Execute script in folder "src/ex00/":
		```shell
		python3 main.py
		```
3. Go to http://127.0.0.1:8000/evilcorp_hacked.html for checking


EXECUTE EX01:
1. Start redis-server:
		```shell
		redis-server
		```
2. Start consumer:
		```shell
		python3 consumer.py -e 7134456234,3476371234
		```
3. Start producer:
		```shell
		python3 producer.py
		```


EXECUTE EX02:
1. Generate config "deploy.yml":
		```shell
		python3 gen_ansible.py
		```
2. Run playbook on remote server [privat-key][]
		```shell
		ansible-playbook -i srcs/inventory.ini ../../materials/deploy.yml
		```
		It's possible to add '-vvv' flag for printing more information



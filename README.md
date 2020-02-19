# COCK ANSIBLE

## Dependencias

Primera ejecución:

```bash
sudo apt install python3-virtualenv
mkdir -p $WORKON_HOME/cock_ansible
mkvirtualenv -p /usr/bin/python3 -a $WORKON_HOME/cock_ansible cock_ansible
pip3 install -r requirements.txt
```

Resto de ejecuciones:

```bash
source $WORKON_HOME/cock_ansible/bin/activate
source openstak_variables.sh
```

## COCK ANSIBLE 20/02/2020

```bash
ansible-playbook create_instance.yml [-e destroy=true]
```

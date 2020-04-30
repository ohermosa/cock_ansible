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

## COCK ANSIBLE 1.0 20/02/2020

```bash
git checkout tags/1.0
ansible-playbook infra.yml [-e destroy=true] --ask-become-pass
```

## COCK ANSIBLE 1.1 06/03/2020

```bash
git checkout tags/1.1
ansible-playbook my_cock.yml
```

## COCK ANSIBLE 1.2 27/03/2020

```bash
git checkout tags/1.2
ansible-playbook my_cock.yml --ask-vault-pass
```

## COCK ANSIBLE 1.3

```bash
git checkout tags/1.3

ansible-playbook backup.yml --ask-vault-pass
ansible-playbook restore.yml --ask-vault-pass

ansible-playbook update_gitea.yml --ask-vault-pass
```

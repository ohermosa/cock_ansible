# COCK ANSIBLE

- [COCK ANSIBLE](#cock-ansible)
  - [Dependencias](#dependencias)
  - [COCK ANSIBLE 1.0 20/02/2020](#cock-ansible-10-20022020)
    - [Objetivo](#objetivo)
    - [Ejecución](#ejecución)
  - [COCK ANSIBLE 1.1 06/03/2020](#cock-ansible-11-06032020)
    - [Objetivo](#objetivo-1)
    - [Ejecución](#ejecución-1)
  - [COCK ANSIBLE 1.2 27/03/2020](#cock-ansible-12-27032020)
    - [Objetivo](#objetivo-2)
    - [Ejecución](#ejecución-2)
  - [COCK ANSIBLE 1.3](#cock-ansible-13)
    - [Objetivo](#objetivo-3)
    - [Ejecución](#ejecución-3)

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

### Objetivo

Crear infraestructura para desplegar los futuros servicios

### Ejecución

```bash
git checkout tags/1.0
ansible-playbook infra.yml [-e destroy=true] --ask-become-pass
```

## COCK ANSIBLE 1.1 06/03/2020

### Objetivo

Desplegar servidor web con página estática y certificados SSL

### Ejecución

```bash
git checkout tags/1.1
ansible-playbook my_cock.yml
```

## COCK ANSIBLE 1.2 27/03/2020

### Objetivo

Desplegar servidor git con la correspondiente BBDD

### Ejecución

```bash
git checkout tags/1.2
ansible-playbook my_cock.yml --ask-vault-pass
```

## COCK ANSIBLE 1.3

### Objetivo

Implementar mecanismo de backup & restore y actualización de servidor git

### Ejecución

```bash
git checkout tags/1.3

ansible-playbook backup.yml
ansible-playbook restore.yml  -e backup_file=/tmp/gitea-dump-1234.zip --ask-vault-path

ansible-playbook update_gitea.yml
```

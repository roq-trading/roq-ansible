# roq-gateways

Ansible script to install gateways.

## Design

### Conda

Install Miniforge to /opt/conda

### systemd

Install service and start/stop timers to /etc/systemd/system

### Configuration

Gateway configurations installed to /usr/local/etc/roq


## Dedendencies

* [Ansible](https://www.ansible.com/)
* [Miniforge](https://github.com/conda-forge/miniforge)
* [systemd](https://systemd.io/)


## Prerequisites

### Ansible

If using conda, you can install ansible like this

```bash
conda install -y ansible
```

### Remote Host

This is the server you will install to.
It is identified by an IP address ("a.b.c.d") and you can log on with a user
("ansible") having sudo access.

### Inventory File

Ansible requires an inventory file (name is not important, but let's name it "example")

```
[example]
server ansible_host="a.b.c.d" ansible_user="ansible" become_user="root"
```

> We're using the label "server".

### Host Variables

If created, host specific variable will be imported from `host_vars/server.yml`.

> The filename is automatically matched to the label "server" from the inventory file.

This is the place to configure the services.

### Group Variables

Common variables can be found in `group_vars/all.yml`.

This file contains all the defaults.

> You can override the defaults by configuring host variables.


## Running

```bash
ansible-playbook -i example site.yml --ask-become-pass
```

## Using

Start gateway

```bash
systemctl start deribit
```

Status

```bash
systemctl status deribit
```

Tail logs

```bash
journalctl -f -u deribit
```


## License

The project is released under the terms of the MIT license.

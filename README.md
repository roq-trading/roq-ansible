# roq-services

Ansible script to install services.

## Design

### Directories

| what | system | user |
| --- | --- | --- |
| Miniforge3 | `/opt/conda` | `~/.local/share/conda` |
| systemd units | `/etc/systemd/system` | `~/.config/systemd/user` |
| config | `/usr/local/etc/roq` | `~/.config/roq` |
| data | `/var/lib/roq/data` | `~/.local/share/roq` |
| cache | `/var/lib/roq/cache` | `~/.local/state/roq` |


## Dedendencies

* [Ansible](https://www.ansible.com/)
* [Miniforge3](https://github.com/conda-forge/miniforge)
* [systemd](https://systemd.io/)


## Prerequisites

### Ansible

You need ansible to run the playbook.

If using conda, you can install ansible (on your local machine) like this

```bash
conda install --freeze-installed -y ansible
```

### Remote Host

This is the server you will install to.

It is identified by an IPv4 address (`a.b.c.d`) and you must be able to log on with ssh and your `ansible_user`.


### Inventory File

Ansible requires an inventory file (name is not important, we will name it "example")

```
[example]
server ansible_host="a.b.c.d" ansible_user="ansible" systemd_scope="system" become_user="root"
```

> We're using the label `server`.

> We need a `become_user` (elevated rights) when `systemd_scope="system"`.

Alternatively, we can also use the script to install the services on our workstation

```
[example]
workstation ansible_host="a.b.c.d" ansible_user="ansible" systemd_scope="user"
```

> We're using the label `workstation`.

> We don't need a `become_user`.

### Host Variables

This is the place to configure your specific services.

Host specific variable will be imported from `host_vars/server.yml` or `host_vars/workstation.yml`.

> The filename is automatically matched to the label `server` or `workstation` that you specified in your inventory file.

### Group Variables

Common variables can be found in `group_vars/all.yml`.

This file contains all the defaults.

> You can override the defaults by configuring host variables.


## Running

When installing to `systemd_scope="system"`, you need the `become_user` (typically `root`) and you then you often need to
specify a password to gain elevated permissions

```bash
ansible-playbook -i example site.yml --ask-become-pass
```

You don't need this when installing on your workstations (`systemd_scope="user"`)

```bash
ansible-playbook -i example site.yml
```


## Using

> You will need elevated permissions (`sudo`) if using systemctl on a server

> You will need to use `systemctl --user` (**no** `sudo`) when using systemctl on your workstation

> These following steps to start/stop services can also be achieved through Roq's service manager

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

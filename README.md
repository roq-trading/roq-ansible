# roq-services

Ansible script to install and control systemd services.


## Design

![UI](/static/images/service-manager.png)


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

### Container

If you want to use Podman and it's not already installed on the host

```bash
sudo apt install podman
```

If you want to use Docker and it's not already installed on the host

```bash
sudo apt install docker.io
```

### Ansible

You need ansible to run this playbook.

If using conda, you can install ansible (on your local machine) like this

```bash
conda install --freeze-installed -y ansible
```

Alternatively, you can install ansible on the host

```bash
sudo apt install ansible
```

### Remote Host

This is the server you will install to.

It is identified by an IPv4 address (`a.b.c.d` in the following) and you must be able to log on with ssh and your `ansible_user`.


### Inventory File

Ansible requires an inventory file (name is not important, we will name it "example")

In the following examples we use `server` to identify the target host.
This could be a remote host or simply `localhost` if you want to test with your user account (no root access required).

```
[example]
server ansible_host="a.b.c.d" ansible_user="ansible" become_user="root"
```

> We're using the label `server`.

> We need a `become_user` (elevated rights) if we have configured `systemd.scope == "system"` (the default).

Alternatively

```
[example]
server ansible_host="localhost" ansible_user="my_user_id"
```

> We do **not** need a `become_user` if we have configured `systemd.scope == "user"`.


### Host Variables

This is the place to configure your specific services.

Host specific variable will be imported from `host_vars/server.yml` or `host_vars/workstation.yml`.

> The filename is automatically matched to the label `server` that you specified in your inventory file.

### Group Variables

Common variables can be found in `group_vars/all.yml`.

This file contains all the defaults.

> You can override the defaults by configuring host variables.


## Running

When installing to `systemd.scope == "system"`, you need the `become_user` (typically `root`) and you then you often need to
specify a password to gain elevated permissions

```bash
ansible-playbook -i example site.yml --ask-become-pass
```

You don't need this when installing on your workstations (`systemd.scope == "user"`)

```bash
ansible-playbook -i example site.yml
```


## Using

> You will need elevated permissions (`sudo`) if using systemctl on a server

> You will need to use `systemctl --user` (**without** `sudo`) when using systemctl on your workstation

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

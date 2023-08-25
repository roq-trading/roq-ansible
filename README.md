roq-ansible

Ansible Playbook to install and configure various services.


## Prerequisites

### Initialize sub-modules

```bash
git submodule update --init --recursive
```

### Update sub-modules

```bash
git submodule update --remote --recursive
```

### Configuration

You should add your own

* Inventory file (see `inventory` for example)
* Host configuration(s) (see `host_vars/server` for example)


## Using

### Ansible Playbook

```bash
ansible-playbook -i inventory site.yml
```

> Append `--ask-become-pass` if the remote account requires a password when using sudo.

### SSH Tunnel

```bash
ssh -L 8081:localhost:1234 ubuntu@1.2.3.4 -N
```

* `http://localhost:8081/grafana/`
* `http://localhost:8081/prometheus/`
* `http://localhost:8081/roq/service/deribit/metrics`


## Notes

### Security

**THIS ANSIBLE PLAYBOOK DOES NOT INCLUDE ANY PROVISIONS FOR SECURITY**!

Our recommendation is to

* **ALWAYS USE A FIREWALL** and
* **ONLY ALLOW EXTERNAL PORT ACCESS WHEN STRICTLY NECESSARY**.

> We recommend to **ONLY ALLOW PORT 22 (SSH)** from the public Internet.
> We also recommend to configure SSH to only allow access using public/private key-pairs (no passwords!).
> These are recommendations: **SECURITY IS YOUR RESPONSIBILITY**

In the examples shown above we have demonstrated how you can establish a SSH tunnel to access the services.
Another option would be to configure a VPN.


## License

The project is released under the terms of the MIT license.

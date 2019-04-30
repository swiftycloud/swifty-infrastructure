## Swifty setup with Ansible

### Create VMs
You need at least two virtual machines (or physical) with 4vCPU, 8GB of RAM and 50GB of storage. Please use Ubuntu 18.04 as OS.


### Clone swifty-infrastructure project
```
git clone https://github.com/swiftycloud/swifty-infrastructure
```

### Change hosts file
Copy swifty-ansible/hosts.example file to hosts and change it according to your settings. Production setup assumes you have 7 virtual or physical servers with different roles. Test setup can use just 2 servers. Here is the example for 2 servers test setup:
```
[gw]
209.97.138.78 vpn_ip=192.0.0.1 tinc_hostname=swftgw public_dns=swf01.domain.com private_ip=192.0.0.1 public_ip=209.97.138.78

[mw]
178.128.162.75 vpn_ip=192.0.0.2 tinc_hostname=swftmw public_dns=swf02.domain.com private_ip=192.0.0.2 public_ip=178.128.162.75

[ui]
209.97.138.78 vpn_ip=192.0.0.1 tinc_hostname=swftgw public_dns=swf01.domain.com private_ip=192.0.0.1 public_ip=209.97.138.78

[connector]

[worker]
178.128.162.75 vpn_ip=192.0.0.2 tinc_hostname=swftmw private_ip=192.0.0.2 public_ip=178.128.162.75

[monitoring]
```

### Change encvironment variables file
Copy swifty-ansible/group_vars/all.example.yml file to all.yml and change it according to your settings. 
1. Add passwords and tokens.
2. Add domain names.
3. Skip #connector section.
4. Don't change settings for gitlab repos - we store docker images on gitlab.

Please be awar, your domain section should look like:
```
default_dashboard_domain_name: swf01.swifty.cloud
default_api_domain_name: swf01.swifty.cloud
default_s3_domain_name: swf02.swifty.cloud
...
```

### Run ansible script
```
ansible-playbook swifty.yml
```

## Repo for docs and IAC 

### Image builder ###

Usage:

```
ansible-playbook -i gitlab-runner.ci.swifty.cloud, swifty-build/tasks/main.yml --extra-vars='{"basedir": "/home/fedora/swifty"}'
```

### full version

#### Роль swft-gw:

```
1. mariadb
2. openstack keystone
3. mongod
4. docker
5. k8s static pods (master)
6. rabbitmq
7. swyadmd
8. swygate
9. nfs-server
10. tinc
```
#### Роль swft-mw:
```
1. docker
2. mongod
3. mariadb
4. swys3
5. tinc
```

#### Роль swft-slave:
```
1. k8s worker
2. docker
3. tinc
```
#### Роль swft-ui:
```
1. docker
2. tinc
```
# Contact
mailto: vp@swifty.cloud

[Join slack](https://join.slack.com/t/swiftycloud/shared_invite/enQtNDk1Nzk5NTQ1OTIzLWVhNWY3ZDZmNmQ1YTBlZGNlN2IzMmNhYmEzNTNkOGU2MzdmZWE3YTBiMjVjYWI5Y2FhMTUwMWUyOTNkZGE5OTM)

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


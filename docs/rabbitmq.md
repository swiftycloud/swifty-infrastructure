### Install erlang

```
wget https://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm
sudo rpm -Uvh erlang-solutions-1.0-1.noarch.rpm
sudo yum install erlang
```

### Install and start rabbitmq
```
wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.9/rabbitmq-server-3.6.9-1.el7.noarch.rpm
sudo rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
sudo yum install rabbitmq-server-3.6.9-1.el7.noarch.rpm
dnf -y install librabbitmq
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```
### Configure rabbitmq


```
rabbitmqctl add_user root 1OqCKIK2G9H
rabbitmqctl set_user_tags root administrator
rabbitmqctl set_permissions -p / root ".*" ".*" ".*"
rabbitmq-plugins enable rabbitmq_management
rabbitmqctl add_user s3 60baf87b7407&
rabbitmqctl set_user_tags s3 administrator
rabbitmqctl add_vhost s3
rabbitmqctl set_permissions -p s3 s3 ".*" ".*" ".*"
```

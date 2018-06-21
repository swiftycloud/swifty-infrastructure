#### Install mariadb

```
dnf -y install mariadb
yum -y install mariadb-server mariadb-server-utils
systemctl start mariadb
systemctl enable mariadb
```

#### Install openstack-pike repo and keystone components

```
dnf install https://repos.fedorapeople.org/repos/openstack/openstack-pike/rdo-release-pike-1.noarch.rpm
dnf -y install openstack-keystone httpd mod_wsgi python-openstackclient
```


#### Configure mariadb

```
mysqladmin -u root password aiNe1sah9ichu1re
mysql -u root -p

CREATE DATABASE keystone;
GRANT ALL PRIVILEGES ON keystone .* TO ' keystone '@ ' localhost ' IDENTIFIED BY ' Ja7hey6keiThoyoi ';
GRANT ALL PRIVILEGES ON keystone .* TO ' keystone '@ '% ' IDENTIFIED BY ' Ja7hey6keiThoyoi ';
```

#### Configure /etc/keystone/keystone.conf

```
[ database ]
...
connection=mysql + pymysql :// keystone : Ja7hey6keiThoyoi@controller / keystone
[ token ]
...
provider = fernet
```

#### Configure keystone

```
/bin/sh -c "keystone-manage db_sync" keystone
keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone
keystone-manage credential_setup --keystone-user keystone --keystone-group keystone
keystone-manage bootstrap --bootstrap-password Cae6ThiekuShiece --bootstrap-admin-url http://controller:35357/v3/  --bootstrap-internal-url http://controller:5000/v3/ --bootstrap-public-url http://controller:5000/v3/ --bootstrap-region-id RegionOne
```

#### Configure httpd

Change ServerName in /etc/httpd/conf/httpd.conf to

```
ServerName controller
```

Bind name to localhost in /etc/hosts

```
127.0.0.1   controller
```

Create symlink for config and start httpd

```
ln -s /usr/share/keystone/wsgi-keystone.conf /etc/httpd/conf.d/
systemctl enable httpd.service
systemctl start httpd.service
```

#### Add vars to ~/.bashrc

```
export OS_USERNAME=admin
export OS_PASSWORD=Cae6ThiekuShiece
export OS_PROJECT_NAME=admin
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_AUTH_URL=http://controller:5000/v3
export OS_IDENTITY_API_VERSION=3
```

#### Create roles and users

```
openstack role create swifty.admin
openstack role create swifty.owner
openstack role create swifty.ui
openstack domain create swifty
openstack project create --domain swifty swyadmin
openstack project create --domain swifty swyui
openstack user create --project swyadmin --domain swifty --password ZXbcUDhg7W1hoD4 swyadmin
openstack user create --project swyui --domain swifty --password ImoFW5vTJeSB swyui
openstack role add --user-domain swifty --user swyadmin --project-domain swifty --project swyadmin swifty.admin
openstack role add --user-domain swifty --user swyadmin --project-domain swifty --project swyadmin swifty.owner
openstack role add --user-domain swifty --user swyui --project-domain swifty --project swyui swifty.ui
openstack user set --project admin admin
```

#### Install mariadb

```
dnf -y install mariadb
yum -y install mariadb-server mariadb-server-utils
systemctl start mariadb
systemctl enable mariadb
```

#### Configure mariadb

```
mysqladmin -u root password aiNe1sah9ichu1re
mysql -u root -p

CREATE DATABASE keystone;
GRANT ALL PRIVILEGES ON keystone .* TO ' keystone '@ ' localhost ' IDENTIFIED BY ' Ja7hey6keiThoyoi ';
GRANT ALL PRIVILEGES ON keystone .* TO ' keystone '@ '% ' IDENTIFIED BY ' Ja7hey6keiThoyoi ';
```

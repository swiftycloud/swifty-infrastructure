#### Add mongodb repo

Add to /etc/yum.repos.d/mongodb.repo

```
[MongoDB]
name=MongoDB Repository
baseurl=http://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=0
enabled=1
```

####  Install and start mongodb

```
dnf install -y mongodb mongodb-server
mongod --version
sudo systemctl enable mongod
sudo systemctl start mongod
```

#### [gw_role] Configure databases and users in mongo shell

```

use swifty

db.createUser(
  {
    user: "swygate",
    pwd: "dt3962zew1b",
    roles: [ { role: "dbAdmin", db: "swifty" } ]
  }
)

db.createUser(
  {
    user: "swyadmd",
    pwd: "1a84cd9148bG8",
    roles: [ { role: "dbAdmin", db: "swifty" } ]
  }
)

use admin

db.createUser({ user: "swyadmd" , pwd: "1a84cd9148bG8", roles: ["userAdminAnyDatabase", "dbAdminAnyDatabase", "readWriteAnyDatabase"]})
db.createUser({ user: "root" , pwd: "ew8VKv8Kq79C", roles: ["userAdminAnyDatabase", "dbAdminAnyDatabase", "readWriteAnyDatabase"]})
```

#### [gw_role] Create collections in mongo shell

```
use swifty

db . createCollection (" Function ")
db . createCollection (" Mware ")
db . createCollection (" Logs ")
db . createCollection (" FnStats ")
db . createCollection (" Balancer ")
db . createCollection (" BalancerRS ")

```

#### [mw_role] Create db and user for s3

```
use swifty-s3


db.createUser(
  {
    user: "swifty-s3",
    pwd: "aebik0eichie0eXu",
    roles: [ { role: "dbOwner", db: "swifty-s3" } ]
  }
)
```

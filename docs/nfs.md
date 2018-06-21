##### Setup NFS on both nodes

```
dnf -y install nfs-utils
systemctl start nfs
systemctl enable nfs

```

#### Configure the master

Create dir for mount point
```
mkdir -p /home/swifty-volume
```

Add those lines to /etc/exports

```
echo "/home/swifty-volume 192.0.0.0/24(rw,sync,no_root_squash)" >> /etc/exports
```

Secure public interface. Add to /etc/hosts.allow:

```
echo "rpcbind mountd nfsd statd lockd rquotad : 192.0.0.2, 192.0.0.3, 192.0.0.4, 192.0.0.5" >> /etc/hosts.allow
```

Add to /etc/hosts.deny:

```
echo "rpcbind mountd nfsd statd lockd rquotad : ALL" >> /etc/hosts.deny
```

#### Configure slaves
Create dir for mount point
```
mkdir -p /home/swifty-volume
```

Add to /etc/fstab entry:
```
echo "192.0.0.1:/home/swifty-volume /home/swifty-volume nfs rw,sync,hard,intr,addr=192.0.0.3 0 0" >>  /etc/fstab
```
Mount nfs
```
mount /home/swifty-volume
```

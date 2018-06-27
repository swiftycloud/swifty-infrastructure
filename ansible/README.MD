##### In swifty-infrastructure/ansible/group_vars/all.yml change pass variables and master_int and worker_int vars. Master_int and worker_int are Private DNS AWS Domains.
##### In swifty-infrastructure/ansible/hosts specify Public DNS AWS Domains.
##### Make sure you have proper key-based ssh connections to AWS virtual machines.
##### For Ubuntu 16.04 install and configure ansible like this

```
apt-get -y install python3-pip openssl libssl-dev
pip3 install ansible
pip3 install --upgrade cryptography
```
##### Run deployment playbook for swifty.lite

```
cd ~/swifty-infrastructure/ansible
ansible-playbook --user root lite.yml
```

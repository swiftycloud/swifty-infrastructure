##### For Ubuntu 16.04 client

```
apt-get -y install python3-pip openssl libssl-dev
pip3 install ansible
pip3 install --upgrade cryptography
cd ~/swifty-infrastructure/ansible
ansible-playbook --user root lite.yml

```

##### In swifty-infrastructure/ansible/group_vars/all.yml change pass variables and master_int and worker_int vars. Master_int and worker_int are Private DNS AWS Domains.
##### In swifty-infrastructure/ansible/hosts specify Public DNS AWS Domains.
##### Make sure you have proper key-based ssh connections to AWS virtual machines. Add aws keypair file to ~/swifty-infrastructure/ansible directory.

##### Create aws credential file and add keys:

```
vi ~/.aws/credentials

[default]
aws_access_key_id=your_key
aws_secret_access_key=your_key

```

##### Edit group_vars/all.yml

```
ansible_ssh_private_key_file: ./ansible.pem #change this to your ssh-keypair file name

ec2_keypair: "ansible"
ec2_security_group: "sg-e0fe9c8a"
ec2_instance_type: "t2.medium"
ec2_image: "ami-e4a89a81"
ec2_subnet_id: "subnet-a7cf72cf"
ec2_region: "us-east-2"
```

##### For Ubuntu 16.04 install and configure ansible like this

```
apt-get -y install python3-pip openssl libssl-dev
pip3 install ansible
pip3 install --upgrade cryptography
```
##### Run deployment playbook for swifty.lite

```
cd ~/swifty-infrastructure/ansible
ansible-playbook -vv -i localhost lite.yml
```

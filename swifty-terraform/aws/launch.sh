#!/usr/bin/env bash

set -ex

terraform init
terraform destroy -auto-approve
python3 tfgen.py abcdef  # FIXME
terraform apply -auto-approve
terraform output -json > output.json
chmod +x ansible_inventory.py
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/swifty.yml --extra-vars="$(python ansible_inventory.py -e)"

#!/bin/bash

if [ -z "$1" ]; then
	echo "Need \"deploy\" argument (aws,digital-ocean)"
	exit 1
fi

if [ -z "$2" ]; then
	echo "Need \"type\" argument (worker,gw,mw)"
	exit 1
fi

cd "swifty-terraform/$1"
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/rebuild.yml --tags "$2" --extra-vars="ansible_ssh_user=root tag_swifty=latest $(python ansible_inventory.py -e)"

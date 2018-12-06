#### How to use with static inventory

**From ./swifty-infrastructure/swifty-ansible dir execute if you want to update ALL swifty apps:**

```
ansible-playbook rebuild.yml

```
**Also you can use tags for roles filtration and update apps separately:**

```
ansible-playbook rebuild.yml --tags gw
ansible-playbook rebuild.yml --tags mw
ansible-playbook rebuild.yml --tags worker
ansible-playbook rebuild.yml --tags ui
ansible-playbook rebuild.yml --tags connector
```

#### How to use with dynamic inventory

**From ./swifty-infrastructure/swifty-terraform/{digital-ocean,aws} dir execute if you want to update ALL swifty apps:**

```
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/rebuild.yml --extra-vars="ansible_ssh_user=root tag_swifty=latest $(python ansible_inventory.py -e)"
```

**Also you can use tags for roles filtration and update apps separately:**

```
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/rebuild.yml --tags gw  --extra-vars="ansible_ssh_user=root tag_swifty=latest $(python ansible_inventory.py -e)
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/rebuild.yml --tags mw  --extra-vars="ansible_ssh_user=root tag_swifty=latest $(python ansible_inventory.py -e)"
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/rebuild.yml --tags worker  --extra-vars="ansible_ssh_user=root tag_swifty=latest $(python ansible_inventory.py -e)
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/rebuild.yml --tags ui  --extra-vars="ansible_ssh_user=root tag_swifty=latest $(python ansible_inventory.py -e)"
ansible-playbook -i ansible_inventory.py ../../swifty-ansible/rebuild.yml --tags connector  --extra-vars="ansible_ssh_user=root tag_swifty=latest $(python ansible_inventory.py -e)"

```

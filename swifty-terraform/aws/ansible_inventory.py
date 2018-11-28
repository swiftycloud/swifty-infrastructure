#!/usr/bin/env python

import sys

import os
import json
from aws_inventory import swifty_hosts

import argparse


data = json.load(open(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'output.json'
    )
))

hosts_meta = {}

for key in data:
    host, var = key.split("::")
    if not hosts_meta.get(host):
        hosts_meta[host] = {}
    hosts_meta[host][var] = data[key]['value']

# host_meta now contains: key=name, value=dict of meta values

inv = {
    '_meta': {
        'hostvars': {}
    }
}

for host in swifty_hosts:
    for group in host.groups:
        if not inv.get(group):
            inv[group] = {'hosts': []}

        if hosts_meta[host.name]['public_dns'] not in inv[group]['hosts']:
            inv[group]['hosts'].append(hosts_meta[host.name]['public_dns'])

        # Collect metadata from Terraform
        host_meta = hosts_meta[host.name]

        # Add metadata from Inventory
        host_meta.update(host.meta)

        inv['_meta']['hostvars'][hosts_meta[host.name]['public_dns']] = host_meta

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", help="Generate Ansible inventory", action="store_true")
    parser.add_argument("-e", "--extravars", help="Generate extra_vars for Ansible", action="store_true")
    args = parser.parse_args()

    if args.list:
        # default behaviour - act as Ansible inventory generator
        print(json.dumps(inv, indent=1))

    elif args.extravars:
        hostnames = {
            'dashboard_domain_name': inv['ui']['hosts'][0],
            'api_domain_name': inv['gw']['hosts'][0],
            's3_domain_name': inv['mw']['hosts'][0],
        }

        print ' '.join(map(lambda a: "{0}={1}".format(a[0], a[1]), hostnames.items()))

    else:
        parser.print_help()

#!/usr/bin/env python

import sys

import os
import json
from do_inventory import swifty_hosts

import boto.route53


conn = boto.connect_route53()
zone = conn.get_zone("infra-ci.swifty.cloud.")
set = boto.route53.record.ResourceRecordSets(conn, zone.id)


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

        if hosts_meta[host.name] not in inv[group]['hosts']:
            inv[group]['hosts'].append(hosts_meta[host.name]['ipv4_address'])

        # Collect metadata from Terraform
        host_meta = hosts_meta[host.name]

        # Add metadata from Inventory
        host_meta.update(host.meta)

        # back compatibility with swifty-bm playbook
        host_meta.update({"public_ip": host_meta['ipv4_address']})
        host_meta.update({"private_ip": host_meta['ipv4_address_private']})

        inv['_meta']['hostvars'][hosts_meta[host.name]['ipv4_address']] = host_meta

ips = {
    'dashboard.infra-ci.swifty.cloud': inv['ui']['hosts'][0],
    'gw.infra-ci.swifty.cloud': inv['gw']['hosts'][0],
    'mw.infra-ci.swifty.cloud': inv['mw']['hosts'][0],
    'worker0.infra-ci.swifty.cloud': inv['worker']['hosts'][0],
    'worker1.infra-ci.swifty.cloud': inv['worker']['hosts'][1],
    'connector.infra-ci.swifty.cloud': inv['connector']['hosts'][0],
}


for name, ip in ips.items():
    set.add_change("UPSERT", name, type="A", ttl=60).add_value(ip)
    set.commit()

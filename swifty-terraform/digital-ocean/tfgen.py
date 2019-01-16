#!/usr/bin/env python

import sys
from jinja2 import Template
from do_inventory import swifty_hosts

with open('terraform.jinja2') as f:
    template = Template(f.read())

rendered = template.render(
    instances=swifty_hosts,
    export_vars=['ipv4_address', 'ipv4_address_private'],
    volumes=['mariadb-iac', 'mongodb-iac', 'nfs-iac'],
)

with open('do.tf', 'w') as f:
    f.write(rendered)

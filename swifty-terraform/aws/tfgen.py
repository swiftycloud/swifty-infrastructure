#!/usr/bin/env python

import sys
from jinja2 import Template
from aws_inventory import swifty_hosts

with open('terraform.jinja2') as f:
    template = Template(f.read())

rendered = template.render(
    instances=swifty_hosts,
    meta={'commit': sys.argv[1]},
    export_vars=['public_ip', 'private_ip'],
)

with open('terraform.tf', 'w') as f:
    f.write(rendered)

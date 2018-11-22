#!/usr/bin/env python


class Host(object):
    def __init__(self, name, groups,region, image, tags, size, meta=None):
        self.name = name
        self.groups = groups
        self.meta = meta or {}
        self.region = region
        self.image = image
        self.tags = tags
        self.size = size

swifty_hosts = [
    Host(
        name='swifty-gw-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-2vcpu-4gb",
        tags = 'iac',
        groups=['gw'],
        meta={
            'vpn_ip': '192.168.0.1',
            'public_dns': 'gw.infra-ci.swifty.cloud',
            'tinc_hostname': 'swygw'
        }
    ),
    Host(
        name='swifty-mw-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-2vcpu-4gb",
        tags = 'iac',
        groups=['mw'],
        meta={
            'vpn_ip': '192.168.0.2',
            'public_dns': 'mw.infra-ci.swifty.cloud',
            'tinc_hostname': 'swymw'
        }
    ),
    Host(
        name='swifty-dashboard-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-1vcpu-2gb",
        tags = 'iac',
        groups=['ui'],
        meta={
            'vpn_ip': '192.168.0.3',
            'public_dns': 'dashboard.infra-ci.swifty.cloud',
            'tinc_hostname': 'swyui'
        }
    ),
    Host(
        name='swifty-worker0-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-2vcpu-4gb",
        tags = 'iac',
        groups=['worker'],
        meta={
            'vpn_ip': '192.168.0.4',
            'public_dns': 'worker0.infra-ci.swifty.cloud',
            'tinc_hostname': 'swyworker0'
        }
    ),
    Host(
        name='swifty-worker1-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-2vcpu-4gb",
        tags = 'iac',
        groups=['worker'],
        meta={
            'vpn_ip': '192.168.0.5',
            'public_dns': 'worker1.infra-ci.swifty.cloud',
            'tinc_hostname': 'swyworker1'
        }
    ),
]

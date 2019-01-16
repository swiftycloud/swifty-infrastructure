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
            'public_dns': 'api.infra-ci.swifty.cloud',
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
            'public_dns': 's3.infra-ci.swifty.cloud',
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
        name='swifty-connector-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-1vcpu-2gb",
        tags = 'iac',
        groups=['connector'],
        meta={
            'vpn_ip': '192.168.0.4',
            'public_dns': 'connector.infra-ci.swifty.cloud',
            'tinc_hostname': 'swyconnector'
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
            'vpn_ip': '192.168.0.5',
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
            'vpn_ip': '192.168.0.6',
            'public_dns': 'worker1.infra-ci.swifty.cloud',
            'tinc_hostname': 'swyworker1'
        }
    ),
    Host(
        name='system-swifty-worker0-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-2vcpu-4gb",
        tags = 'iac',
        groups=['worker'],
        meta={
            'vpn_ip': '192.168.0.7',
            'public_dns': 'swifty-worker0.infra-ci.swifty.cloud',
            'tinc_hostname': 'systemswyworker0'
        }
    ),
    Host(
        name='system-swifty-worker1-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-2vcpu-4gb",
        tags = 'iac',
        groups=['worker'],
        meta={
            'vpn_ip': '192.168.0.8',
            'public_dns': 'swifty-worker1.infra-ci.swifty.cloud',
            'tinc_hostname': 'systemswyworker1'
        }
    ),
    Host(
        name='swifty-storage-iac',
        region = 'ams3',
        image  = 'ubuntu-18-04-x64',
        size   = "s-2vcpu-4gb",
        tags = 'iac',
        groups=['storage'],
        meta={
            'vpn_ip': '192.168.0.9',
            'public_dns': 'storage.infra-ci.swifty.cloud',
            'tinc_hostname': 'swystorage'
        }
    ),
]

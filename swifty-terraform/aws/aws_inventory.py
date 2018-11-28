#!/usr/bin/env python


class Host(object):
    def __init__(self, name, diskspace, groups, meta=None):
        self.name = name
        self.groups = groups
        self.meta = meta or {}
        self.diskspace = diskspace


swifty_hosts = [
    Host(
        name='gateway',
        diskspace=20,
        groups=['gw'],
        meta={
            'vpn_ip': '192.168.0.1',
            'tinc_hostname': 'swygw'
        }
    ),
    Host(
        name='middleware',
        diskspace=10,
        groups=['mw'],
        meta={
            'vpn_ip': '192.168.0.2',
            'tinc_hostname': 'swymw'
        }
    ),
    Host(
        name='dashboard',
        diskspace=10,
        groups=['ui'],
        meta={
            'vpn_ip': '192.168.0.3',
            'tinc_hostname': 'swyui'
        }
    ),
    Host(
        name='worker0',
        diskspace=10,
        groups=['worker'],
        meta={
            'vpn_ip': '192.168.0.4',
            'tinc_hostname': 'swyworker0'
        }
    ),
    Host(
        name='worker1',
        diskspace=10,
        groups=['worker'],
        meta={
            'vpn_ip': '192.168.0.5',
            'tinc_hostname': 'swyworker1'
        }
    ),
]

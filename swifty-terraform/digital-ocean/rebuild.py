#!/usr/bin/env python3
import requests
import os

headers = {"Authorization": "Bearer " + os.environ['TF_VAR_do_token']}
tag = "iac"

droplets = requests.get("https://api.digitalocean.com/v2/droplets?tag_name=" + tag,headers=headers).json()[u'droplets']

for drop in droplets:
    requests.post("https://api.digitalocean.com/v2/droplets/%id/actions" % drop[u'id'],data={"type":"rebuild","image":"ubuntu-18-04-x64"}, headers=headers).json()

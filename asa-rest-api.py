import urllib
import urllib2,base64
import json
import getpass
import requests
import re
import ssl
import pprint

username = raw_input("Please enter your username: ")
password = getpass.getpass(prompt='Enter password : ')

BaseURL = 'https://10.20.68.23/api'

OnDemandQueryURL = BaseURL+'/cli?context=VPN1'

Showconfig = { "commands": [ "show configuration" ] }

req = urllib2.Request(OnDemandQueryURL,json.dumps(Showconfig), {'Content-Type': 'application/json'} )

base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string) 

#### Make REST Request  ###
u = urllib2.urlopen(req, context=ssl._create_unverified_context())

#### Parse the Response sent in JSON format  ###
#resp = json.loads(u.read().decode('utf-8'))
resp = json.loads(u.read().decode('utf-8'))

#### Render the Response  ###
pprint(resp)

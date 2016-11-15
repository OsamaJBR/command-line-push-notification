#!/usr/bin/python
'''
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''
from ConfigParser import SafeConfigParser
import requests
import argparse

# Config Parsing
config = SafeConfigParser()
config.read('notifier.conf')

## FUNCTIONS
def getGroupKeys(group_name):
    try: return config.get('groups',group_name)
    except Exception as e : 
        print 'No group called %s, will send it default key.' %group_name
        return config.get('SimplePush','key')
    
def simplePushNotification(keys,title,message):
    failed_keys=[]
    for key in keys.split(','):
        request_url='%s/%s/%s/%s' %(config.get('SimplePush','url'),key,title,message)
        req = requests.get(request_url)
        if req.status_code != requests.codes.ok :
            print "Failed to send push notification, URL= %r, RESPONSE= %r" %(req.url, req.text)
            failed_keys.append(key)
    if failed_keys : return False
    return True
    
## MAIN
def main(parser):
    args = parser.parse_args()
    keys=config.get('SimplePush','key')
    if args.group and args.user:
        keys='%s,%s' %(getGroupKeys(args.group),args.user)
    if args.group:
        keys=getGroupKeys(args.group)
    if args.user:
        keys=args.user
    if args.key:
        keys=args.key
    send_req = simplePushNotification(
            keys=keys,
            title=args.title,
            message=args.message
        )
    if not send_req : exit(2)

## ENTRY
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t',action='store',dest='title')
    parser.add_argument('-m',action='store',dest='message')
    parser.add_argument('-k',action='store',dest='key')
    parser.add_argument('--group',action='store',dest='group')
    parser.add_argument('--user',action='store',dest='user')
    main(parser)

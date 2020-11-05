#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import print_function, unicode_literals
import os
import datetime
import pytz
import requests
import pprint

APIKEY = os.environ.get('APIKEY')

ENDPOINT = 'https://api.chatwork.com/v2'
ROOMID = '118327104' # My Chat

post_message_url = f'{ENDPOINT}/rooms/{ROOMID}/messages'

message = 'APIKEY : ' + str(APIKEY) + '\n' + '지금 시간 : ' + str(datetime.datetime.now(pytz.timezone('Asia/Tokyo')))

headers = { 'X-ChatWorkToken': APIKEY }
params = { 'body': message }

resp = requests.post(post_message_url,
                     headers=headers,
                     params=params)

pprint.pprint(resp.content)

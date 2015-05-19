#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from requests_oauthlib import OAuth1


client_key = '7891011'
client_secret = 'qN2AV7Ig'
token_key = '2T4rRK2x8dybmfX2NdpU9HCn6cdVEtyPLejLK6P3yMK5K5EbWnRd3ZsxmcwagH08XY'
token_secret = 'VYn4FipgxqnlzRKjjFeUuA'
_OAUTH = OAuth1(client_key=client_key, client_secret=client_secret,
               resource_owner_key=token_key, resource_owner_secret=token_secret,
               signature_type = 'auth_header')


def post_candiate():
    '''
    POST Candidate's Information
    '''
    url = 'http://api.somedestination.com/v3/candidates'
    payload = {'candidate_id': 'VHXOY9U727', 'first_name': 'Willie',
               'last_name': 'Smith',\
               'email': 'someemail@service.com', 'position_id': 'CEO',
               'explanation': 'put and post data via PYTHONS REQUESTS',
               'projects[]': ['https://github.com/mmillions',
               'https://github.com/mmillions/post-put-via-requests'],
               'source':'Some Agency'}
    headers = {'content-type': 'application/json'}
    client = requests.session()
    response = client.post(url,
                           auth=_OAUTH,
                           data=json.dumps(payload),
                           headers=headers)
    results = json.loads(response.content)
    print results
    post_candidate_resume()


def post_candidate_resume():
    '''
    PUT Candidate's Resume
    '''
    url = 'http://api.somedestination.com/v3/candidates/VHXOY9U727/resumes'
    files = {'file': open('some_file.pdf', 'rb')}
    headers = {'content-type': 'application/json'}
    client = requests.session()
    response = client.put(url,
                          auth=_OAUTH,
                          files=files)
    results = response.content
    print results

#POST a new candidate
post_candiate()

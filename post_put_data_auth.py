# -*- coding: utf-8 -*-

import base64
import json
import requests
from requests_oauthlib import OAuth1


client_key = '7891011'
client_secret = 'qN2AV7Ig'
token_key = '2T4rRK2x8dybmfX2NdpU9HCn6cdVEtyPLejLK6P3yMK5K5EbWnRd3ZsxmcwagH08XY'
token_secret = 'VYn4FipgxqnlzRKjjFeUuA'
_OAUTH = OAuth1(client_key=client_key,
                client_secret=client_secret,
                resource_owner_key=token_key,
                resource_owner_secret=token_secret,
                signature_type = 'auth_header')

#TO DO:  Handle 220 and 405 Responses
def post_candidate():
    '''
    POSTs Candidate's Information including a PDF version of their resume
    as a base64 encoded string.
    In this usecase the JSON dict of the passed object will contain the resume,
    and will look something like this:

    {u'files': {}, ...},
    u'json':
    {'candidate_id': 'VHXOY9U727',
    u'first_name': u'Willie',
    u'last_name': u'Smith',
    u'position_id': u'CEO',
    u'explanation': u'Post JSON via Pythons REQUESTS library...',
    u'source': u'Some Agency',
    u'projects[]': [u'https:...', u'https:...'],
    u'email': u'someemail@service.com',
    u'resume' = 'A0Njk5OCAwMDAwMCBuIMDAwMDQ3MjM3IDAwMDAwIG4gCjAwMDAwNTA... '}
    ...'}

    '''
    with open('some_file.pdf', 'rb') as f:
        resume = base64.b64encode(f.read())
    url = 'http://api.somedestination.com/v3/candidates'
    payload = {'candidate_id': 'VHXOY9U727',
               'first_name': 'Willie',
               'last_name': 'Smith',
               'email': 'someemail@service.com',
               'position_id': 'CEO',
               'explanation': 'put and post data via PYTHONS REQUESTS',
               'projects[]': ['https://github.com/mmillions',
               'https://github.com/mmillions/post-put-via-requests'],
               'source':'Some Agency',
               'resume': resume}
    headers = {'content-type': 'application/json'}
    client = requests.session()
    response = client.post(url,
                           auth=_OAUTH,
                           data=json.dumps(payload),
                           headers=headers)
    results = json.loads(response.content)
    #print results
    put_candidate_resume()

#TO DO:  Handle 220 and 405 Responses
def put_candidate_resume():
    '''
    PUTs Candidate's Resume by adding a PDF file associated via the
    'candidate_id' value, which was passed via the "post_candidate" function.
    In this usecase the FILE dict of the passed object will contain the resume,
    and will look something like this:

    {u'files': {'A0Njk5OCAwMDAwMCBuIAowMDAwMDQ3MjM3IDAwMDAwIG4gCjAMDAwNTA... '},
    ...},
    u'json': {}
    ...'}

    '''
    url = 'http://api.somedestination.com/v3/candidates/VHXOY9U727/resumes'
    files = {'file': open('some_file.pdf', 'rb')}
    headers = {'content-type': 'application/json'}
    client = requests.session()
    response = client.put(url,
                          auth=_OAUTH,
                          files=files)
    results = response.content
    #print results

#POST a new candidate's data
post_candidate()

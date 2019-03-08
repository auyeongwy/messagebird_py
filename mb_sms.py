# Copyright 2019 Au Yeong Wing Yau
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
A script to interface with the MessageBird REST API
Usage:

python3 mb_sms.py
"""

import mb_config
import sys 
import http.client 
import json
import urllib


def create_url(p_config):
	"""
	Constructs the URL for the REST request
	:param p_config: An mb_config.mb_config object that contains the configuration parameters
	"""
	url = '/messages'
	params = {}
	if p_config.filter_enabled == '1':
		if hasattr(p_config, 'filter_originator'):
			params['originator'] = p_config.filter_originator
		if hasattr(p_config, 'filter_recipient'):
			params['recipient'] = p_config.filter_recipient
		if hasattr(p_config, 'filter_direction'):
			params['direction'] = p_config.filter_direction
		if hasattr(p_config, 'filter_limit'):
			params['limit'] = p_config.filter_limit
		if hasattr(p_config, 'filter_offset'):
			params['offset'] = p_config.filter_offset
		if hasattr(p_config, 'filter_searchterm'):
			params['searchterm'] = p_config.filter_searchterm
		if hasattr(p_config, 'filter_type'):
			params['type'] = p_config.filter_type
		if hasattr(p_config, 'filter_contact_id'):
			params['contact_id'] = p_config.filter_contact_id
		if hasattr(p_config, 'filter_status'):
			params['status'] = p_config.filter_status
		if hasattr(p_config, 'filter_from'):
			params['from'] = p_config.filter_from
		if hasattr(p_config, 'filter_until'):
			params['until'] = p_config.filter_until
		
	if len(params) > 0:
		url = url+'?'+urllib.parse.urlencode(params)
	return url
	
	
	
def create_payload(p_config):
	"""
	Constructs the payload for the REST request
	:param p_config: An mb_config.mb_config object that contains the configuration parameters
	"""	
	payload = {}
	if p_config.filter_enabled == '1':
		if hasattr(p_config, 'filter_originator'):
			payload['originator'] = p_config.filter_originator
	
	if len(payload) > 0:
		payload = json.dumps(payload)
		
	return payload
	
	

def create_header(p_config):
	"""
	Constructs the header for the REST request
	:param p_config: An mb_config.mb_config object that contains the configuration parameters
	"""		
	header = {}
	header['Authorization'] = 'AccessKey '+p_config.sms_api_key
	return header
	
	

""" Load the config file """
try:
	config = mb_config.mb_config("config.real")
except Exception as excep:
	print(excep.args[0])
	sys.exit()

""" Get the access key """
v_payload = create_payload(config)
#print(vars(config))



v_client_conn = http.client.HTTPSConnection('rest.messagebird.com')
v_url = create_url(config)
#print(v_url)
	
try:
	v_client_conn.request("GET", v_url, None, create_header(config))
	response = v_client_conn.getresponse()
except http.client.HTTPException as he:
	print(he.args[0])
	sys.exit


""" Work with the results """
print(response.status, response.reason)
if response.status != 200: 
	print(response.read())
	
else:
	v_result = (response.read()).decode('utf-8')
	print(json.dumps(json.loads(v_result), indent=2, sort_keys=True))

v_client_conn.close()

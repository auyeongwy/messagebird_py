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



import configparser

class mb_config:
	"""
	Manages reading the config file parameters into variables.
	Usage:

	import mb_config

	try:
	my_config = mb_config.mb_config("configfile")
	except Exception as except:
		print(except.args[0])
		print("Abort")
		sys.exit()
	
	print(vars(my_config))
	"""

	def read_message_config(self, p_config):
		""" 
		Reads config options from the "Message" part of the config file into the current object's variables.
		:param p_config: The configparser.ConfigParser object that has opened the config file. 
		"""
		if "OA" in p_config["Message"]:
			self.oa = p_config["Message"]["OA"]
		if "Recipient" in p_config["Message"]:
			self.recipient = p_config["Message"]["Recipient"]
		if "Message" in p_config["Message"]:
			self.message = p_config["Message"]["Message"]		

		

	def read_filter_config(self, p_config):
		""" 
		Reads config options from the "Filter" part of the config file into the current object's variables.
		:param p_config: The configparser.ConfigParser object that has opened the config file. 
		"""		
		if "enabled" in p_config["Filter"]:
			self.filter_enabled = p_config["Filter"]["enabled"]
			if self.filter_enabled == '1':
				if "originator" in p_config["Filter"]:
					self.filter_originator = p_config["Filter"]["originator"]
				if "recipient" in p_config["Filter"]:
					self.filter_recipient = p_config["Filter"]["recipient"]
				if "direction" in p_config["Filter"]:
					self.filter_direction = p_config["Filter"]["direction"]
				if "limit" in p_config["Filter"]:
					self.filter_limit = p_config["Filter"]["limit"]
				if "offset" in p_config["Filter"]:
					self.filter_offset = p_config["Filter"]["offset"]
				if "searchterm" in p_config["Filter"]:
					self.filter_searchterm = p_config["Filter"]["searchterm"]
				if "type" in p_config["Filter"]:
					self.filter_type = p_config["Filter"]["type"]
				if "contact_id" in p_config["Filter"]:
					self.filter_recipient = p_config["Filter"]["contact_id"]
				if "status" in p_config["Filter"]:
					self.filter_status = p_config["Filter"]["status"]
				if "from" in p_config["Filter"]:
					self.filter_from = p_config["Filter"]["from"]
				if "until" in p_config["Filter"]:
					self.filter_until = p_config["Filter"]["until"]
		else:
			self.filter_enabled = '0'

		

	def read_view_config(self, p_config):
		""" 
		Reads config options from the "View" part of the config file into the current object's variables.
		:param p_config: The configparser.ConfigParser object that has opened the config file. 
		"""
		if "id" in p_config["View"]:
			self.view_id = p_config["View"]["id"]


		
	def __init__(self, p_file):
		""" 
		Reads config options from a configuration file into this object.
		:param p_file: The configuration file. 
		"""
		config = configparser.ConfigParser()
		if len(config.read(p_file)) == 0:
			raise Exception("Config file error.")

		if "SMS_API_KEY" in config["Key"]:
			self.sms_api_key = config["Key"]["SMS_API_KEY"]
		else:
			"""If API key is missing just give up."""
			raise Exception("Missing API key.") 
			
		self.read_message_config(config)
		self.read_filter_config(config)
		self.read_view_config(config)

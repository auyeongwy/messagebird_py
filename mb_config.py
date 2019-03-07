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

import configparser

class mb_config:
	
	def __init__(self, p_file):
		self.config = configparser.ConfigParser()
		if len(self.config.read(p_file)) == 0:
			raise Exception("Config file error.")
		else:
			self.sms_api_key = self.config["Message Bird"]["SMS_API_KEY"]
			self.oa = self.config["Message"]["OA"]
			self.recipient = self.config["Message"]["Recipient"]
			self.message = self.config["Message"]["Message"]
		

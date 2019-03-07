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

try:
	config = mb_config.mb_config("config")
except Exception as excep:
	print(excep.args[0])
	sys.exit()

print(config.message)
print(config.recipient)
print(config.oa)
print(config.sms_api_key)
print(vars(config))

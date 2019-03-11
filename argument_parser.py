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


def print_help():
	print("Help text")



def parse_arguments(p_args):
	result = 0
	command = None
	argument = None
	
	if len(p_args) < 2:
		print("Incorrect arguments.")
		print_help()
	
	elif p_args[1] not in ['query', 'view']:
		print("Incorrect arguments.")
		print_help()
			
	elif p_args[1] == 'view': 
		if len(p_args) < 3:
			print("Incorrect arguments.")
			print_help()
		else:
			argument = p_args[2]

	else:
		result = 1
		command = p_args[1]

	return (result, command, argument)

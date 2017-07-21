#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-13 22:00:35
# @Author  : Polly
# @Link    : wangbaoli@ict.ac.cn
# @Version : Beta 1.0

import os
import sys
import requests
import json

#sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf8')  

class Daiwan(object):
	"""docstring for Daiwan"""

	BASE_URL = "http://lolapi.games-cube.com"
	USER_API_URL = "/champion"

	token = "BE450-196CD-A9CEB-40004"

	def __init__(self, token):
		self.token = token

	def get_hero_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		return requests.get(self.BASE_URL+self.USER_API_URL, headers=headers)

	def get_free_hero_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		return requests.get(self.BASE_URL+"/Free", headers=headers)

demo = Daiwan("BE450-196CD-A9CEB-40004")
# response = demo.get_hero_info()
# print response.text
print demo.get_free_hero_info().text.encode('utf-8')
# for k,v in user_info.items():
# 	print "{}-{}".format(k, v)
		

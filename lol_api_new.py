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
# reload(sys)
# sys.setdefaultencoding('utf8')  

class Daiwan(object):
	"""docstring for Daiwan"""

	BASE_URL = "http://lolapi.games-cube.com"
	USER_AREA_URL = "/UserArea"
	USER_API_URL = "/champion"

	token = "CCDB9-D7284-EDEAD-1CE6A"

	def __init__(self, token):
		self.token = token
		self.headers = {"DAIWAN-API-TOKEN": self.token}

	def get_user_info(self):
		keyword = "Daonels"
		return requests.get(self.BASE_URL+self.USER_AREA_URL+"?keyword="+keyword, headers=self.headers)

	def get_user_hot_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		qquin = "U10233816392932256594"
		vaid = "1"
		return requests.get(self.BASE_URL+"/UserHotInfo"+"?qquin="+qquin+"&vaid="+vaid, headers=self.headers)

	def get_user_ext_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		qquin = "U10233816392932256594"
		vaid = "1"
		return requests.get(self.BASE_URL+"/UserExtInfo"+"?qquin="+qquin+"&vaid="+vaid, headers=self.headers)

	def get_battle_summay_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		qquin = "U10233816392932256594"
		vaid = "1"
		return requests.get(self.BASE_URL+"/BattleSummaryInfo"+"?qquin="+qquin+"&vaid="+vaid, headers=self.headers)

	def get_combat_list_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		qquin = "U10233816392932256594"
		vaid = "1"
		p = "1"
		return requests.get(self.BASE_URL+"/CombatList"+"?qquin="+qquin+"&vaid="+vaid+"&p="+p, headers=self.headers)

	def get_combat_detail_info(self, gameid):
		headers = {"DAIWAN-API-TOKEN": self.token}
		qquin = "U10233816392932256594"
		vaid = "1"
		gameid = str(gameid)
		return requests.get(self.BASE_URL+"/GameDetail"+"?qquin="+qquin+"&vaid="+vaid+"&gameid="+gameid, headers=self.headers)

	def get_hero_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		return requests.get(self.BASE_URL+self.USER_API_URL, headers=self.headers)

	def get_free_hero_info(self):
		headers = {"DAIWAN-API-TOKEN": self.token}
		return requests.get(self.BASE_URL+"/Free", headers=self.headers)


demo = Daiwan("44714-D1C11-17A76-AF4DE")

#response = demo.get_user_info()
#response = demo.get_user_hot_info()
#response = demo.get_user_ext_info()
#response = demo.get_battle_summay_info()
response = demo.get_combat_list_info()
#response = demo.get_combat_detail_info()
print response.encoding
#print response.text
game_list = json.loads(response.text)
game_list = game_list.get("data")[0].get("battle_list")
game_list = [(g.get("battle_time"),g.get("game_id")) for g in game_list]
for g in game_list:
	r = demo.get_combat_detail_info(g[1])
	game_info = json.loads(r.text)
	try:
		print "Battle Time:{}".format(g[0])
		for data in game_info.get("data"):
			records = data.get("battle").get("gamer_records")
			for r in records:
				print r.get("name")
			print "-------------------------"
	except:
		pass

#game_detail_info = json.loads(response.text)

# for data in game_detail_info.get("data"):
# 	records = data.get("battle").get("gamer_records")
# 	for r in records:
# 		print r.get("name")

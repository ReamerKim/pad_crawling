#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re
import requests
import json
from bs4 import BeautifulSoup

class LeaderSkill(object):
	_name = ""
	_desc = ""
	_subDesc = ""
	_monsterList = []
	_monsterNum = 0

	def __init__(self, _name = "",	_desc = "",	_subDesc = "",	_monsterList = [],	_monsterNum = 0):
		self._name = _name
		self._desc = _desc
		self._subDesc = _subDesc
		self._monsterList = _monsterList
		self._monsterNum = _monsterNum

	def showSkill(self):
		print "name: %s"%self._name
		print "_desc %s"% self._desc
		print "_subDesc %s"% self._subDesc
		print "_monsterNum: %d"% self._monsterNum
		print ""



# Get Skill List from web site
def getLeaderSkillListFromUrl():
	url = 'http://www.thisisgame.com/pad/info/skill/list.php?class1=2' # all skill List site
	u = urllib.urlopen(url)
	c = u.read()
	u.close()

	soup = BeautifulSoup(c)
	rst = soup.find_all("tbody")
	c = rst[0]
	skill_list = c.find_all('tr')
	_skillList = [];

	for _skill in skill_list:
		# 1st get name
		name = _skill.contents[0].contents[1].encode('utf-8').strip()
		desc = _skill.contents[1].contents[0].encode('utf-8').strip()
		try:
			subDesc = _skill.contents[1].contents[1].contents[0].encode('utf-8').strip()
		except:
			subDesc = ""
		rgx_mon_num = re.compile("icon_([\d]+)")
		try:
			monsterList = rgx_mon_num.findall(_skill.contents[2].contents[1].contents[0].encode('utf-8'))
			monsterNum = len(monsterList)
		except:
			monsterList = []
			monsterNum = 0
		_s = LeaderSkill(name, desc, subDesc, monsterList, monsterNum)
		_s.showSkill()
		_skillList.append(_s);
	return _skillList



if __name__ == "__main__":
	getLeaderSkillListFromUrl();


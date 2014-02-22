#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re
import requests
import json
from bs4 import BeautifulSoup

class Skill(object):
	_name = ""
	_maxLevel = 0
	_turn = 0xffff
	_desc = ""
	_subDesc = ""
	_monsterList = []
	_monsterNum = 0

	def __init__(self, _name = "",	_maxLevel = 0,	_turn = 0xffff,	_desc = "",	_subDesc = "",	_monsterList = [],	_monsterNum = 0):
		self._name = _name
		self._maxLevel = _maxLevel
		self._turn = _turn
		self._desc = _desc
		self._subDesc = _subDesc
		self._monsterList = _monsterList
		self._monsterNum = _monsterNum

	def showSkill(self):
		print "name: %s"%self._name
		print "_maxLevel: %d"%self._maxLevel
		print "_turn: %d"% self._turn
		print "_desc %s"% self._desc
		print "_subDesc %s"% self._subDesc
		print "_monsterNum: %d"% self._monsterNum
		print ""



# Get Skill List from web site
def getSkillListFromUrl():
	url = 'http://www.thisisgame.com/pad/info/skill/list.php?class1=1' # all skill List site
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
		# turn과 level을 여기서 가져온다.
		try:
			lv_text = _skill.contents[0].contents[2].contents[1].contents[0].encode('utf-8').strip()
		except:
			lv_text = ""
		if lv_text == "":
			try:
				lv_text = _skill.contents[0].contents[2].contents[0].contents[0].encode('utf-8').strip()
			except:
				continue
			
		rgx_turns = re.compile("([\d]+)")
		lvTurn = rgx_turns.findall(lv_text)
		turn = int(lvTurn[1])
		maxLevel = int(lvTurn[2])
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
		_s = Skill(name, maxLevel, turn, desc, subDesc, monsterList, monsterNum)
		
		_skillList.append(_s);
	return _skillList



if __name__ == "__main__":
	getSkillListFromUrl();


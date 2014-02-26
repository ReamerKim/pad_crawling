#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re
import requests
import json

_no = re.compile(r"""<div class="no">No. ([^<]+)</div>""");
_name = re.compile(r"""<div class="name">([^<]+)</div>""")
_icon = re.compile(r"""<img class="imgicon" src="([^"]+)" /></div>""")
_cost = re.compile(r"""<div class="cost"><dl><dt>[^<]+</dt><dd>([^<]+)</dd>""")
_exp = re.compile(r"""<div class="exp"><dl><dt>[^<]+</dt><dd style="width: 92px;"><span style="float:left;">([^<]+)</span> """);
_status= re.compile(r"""<div class="block stateInfo">([^@]{3,5000}?)</div>""");
_attr= re.compile(r"""fonticon_attr_([\d]+)""");
_type=re.compile(r"""fonticon/fonticon_type_([\d]+)""");
_skill = re.compile(r"""<div class="block skillInfo">([^@]+)<div class="block awakenInfo">""");
_awakeSkill = re.compile(r"""<div class="block awakenInfo">([^@]{3,5000}?)</div>""");


''' 
Get monster data from inven json structure
monstercode: int
maxattack: int
monsterattribute: int
recoverymod: str
monstername: unicode
exptype: int
needexp: int
hpmod: str
attack: int
exp: int
maxhp: int
maxrecovery: int
attackmod: str
maxlevel: int
hp: int
recovery: int
'''
def get_monster_default_data(monster_num):
	data = { 'code': '%d'%monster_num, 'mode': '2' }
	url = r"""http://m.inven.co.kr/site/pad/monster_info.ajax.php"""
	r = requests.post(url,data=data)
	t = r.text
	rst = json.loads(t)
	return rst;


def get_charactor_num(uni_c):
	com = re.compile(_no);
	rst = com.findall(uni_c)
	if len(rst) != 0:
		return int(rst[0],10)
	else:
		raise Exception("ERROR")

def get_charactor_name(uni_c):
	com = re.compile(_name);
	rst = com.findall(uni_c)
	if len(rst) != 0:
		return rst[0]
	else:
		raise Exception("ERROR")

def get_charactor_icon_url(uni_c):
	com = re.compile(_icon);
	rst = com.findall(uni_c)
	if len(rst) != 0:
		return rst[0]
	else:
		raise Exception("ERROR")

def get_charactor_cost(uni_c):
	com = re.compile(_cost);
	rst = com.findall(uni_c)
	if len(rst) != 0:
		return int(rst[0])
	else:
		raise Exception("ERROR")

def get_charactor_exp(uni_c):
	com = re.compile(_exp);
	rst = com.findall(uni_c)
	if len(rst) != 0:
		return int(rst[0].replace(",",""))
	else:
		raise Exception("ERROR")

def get_charactor_status(uni_c):
	# return Max_Lv, min_hp, max_hp, min_attack, max_attack, min_heal, max_heal
	com = re.compile(_status);
	rst = com.findall(uni_c)

	com2 = re.compile(r"""th>Lv.1</th>\s+<th class="nobg">Lv.([^<]+)</th>\s+</tr>\s+<tr>\s+<td height="26">HP</td>\s+<td>([^<]+)</td>\s+<td class="nobg">([^<]+) <span class="green">[^<]+</span></td>\s+</tr>\s+<tr>\s+<td height="24">[^<]+</td>\s+<td>([^<]+)</td>\s+<td class="nobg">([^<]+) <span class="green">[^<]+</span></td>\s+</tr>\s+<tr>\s+<td height="23">[^<]+</td>\s+<td>([^<]+)</td>\s+<td class="nobg">([^<]+)""")


	if len(rst) != 0:
		#require get data from HTML Table
		r = com2.findall(rst[0]);
		return int(r[0][0]), int(r[0][1]), int(r[0][2]), int(r[0][3]), int(r[0][4]), int(r[0][5]), int(r[0][6])
		
	else:
		raise Exception("ERROR")

def get_charactor_attr(uni_c):
	com = re.compile(_attr);
	rst = com.findall(uni_c)
	if len(rst) != 0:
		rr = []
		for r in rst:
			rr.append(int(r))
		return rr
	else:
		raise Exception("ERROR")

def get_charactor_type(uni_c):
	com = re.compile(_type);
	rst = com.findall(uni_c)
	if len(rst) != 0:
		rr = []
		for r in rst:
			rr.append(int(r))
		return rr
	else:
		raise Exception("ERROR")

	

class Monster(object):
	def __init__(self, _no= 0, _name= "None", _cost= 0, _exp= 0, _expType=0, _maxLevel= 0, _minAttackPoint= 0, _maxAttackPoint= 0, _attackPointType= 0, _minHealthPoint= 0, _maxHealthPoint= 0, _healthPointType= 0, _minHealPoint= 0, _maxHealPoint= 0, _healPointType= 0, _mainAttribute= 0, _subAttribute= 0, _mainType= 0, _subType= 0, _skill= 0, _LeaderSKill= 0, _AwakeSkill= "None", _prevEvolution= 0, _nextEvolution= 0, _imageUrl= "None"):
		self._no = _no;
		self._name = _name;
		self._cost = _cost;	
		self._exp = _exp;
		self._expType = _expType;
		self._maxLevel = _maxLevel;
		self._minAttackPoint = _minAttackPoint;
		self._maxAttackPoint = _maxAttackPoint;
		self._attackPointType = _attackPointType;
		self._minHealthPoint = _minHealthPoint;
		self._maxHealthPoint = _maxHealthPoint;
		self._healthPointType = _healthPointType;
		self._minHealPoint = _minHealPoint;
		self._maxHealPoint = _maxHealPoint;
		self._healPointType = _healPointType;
		self._mainAttribute = _mainAttribute; 
		self._subAttribute = _subAttribute; 
		self._mainType = _mainType;	
		self._subType = _subType;	
		self._skill = _skill;			#
		self._LeaderSKill = _LeaderSKill;	#
		self._AwakeSkill = _AwakeSkill;		#
		self._prevEvolution = _prevEvolution;	#
		self._nextEvolution = _nextEvolution;	#
		self._imageUrl = _imageUrl;



	# c is euc-kr string !
	@classmethod
	def get_charactor_info_from_string(cls, c):
		# All String Save the UTF-8
		#uni_c = unicode(c,'euc-kr').encode('utf-8')
		uni_c = c
		#print get_charactor_num(uni_c), get_charactor_icon_url(uni_c), get_charactor_cost(uni_c), get_charactor_exp(uni_c), get_charactor_status(uni_c), get_charactor_attr(uni_c), get_charactor_type(uni_c)
		#추후 작업을 계속 하여야 한다.  이부분에 아직 데이터가 정제가 되지 않았음 
		return cls(_no = get_charactor_num(uni_c), _name= get_charactor_name(uni_c), _cost= get_charactor_cost(uni_c), _exp = get_charactor_exp(uni_c))

	@classmethod
	def get_charactor_info_from_file(cls, _path):
		# All String Save the UTF-8
		f = open(_path)
		c = f.read()
		f.close()
		return cls.get_charactor_info_from_string(c);

	@classmethod
	def get_charactor_info_from_url(cls, id_num):
		# get Monster Data from inven
		url  = "http://m.inven.co.kr/site/pad/monster.php?code=%d"%id_num
		u = urllib.urlopen(url);
		c = u.read()
		u.close()
		return cls.get_charactor_info_from_string(c);

	@classmethod
	def get_charactor_info_from_json(cls, id_num):
		try:
			#print 'get %d'%id_num
			rst = get_monster_default_data(id_num)
			m = cls(_no=rst['monstercode'], _name=rst['monstername'].encode('utf-8'), _maxLevel=rst['maxlevel'], _minAttackPoint=rst['attack'], _maxAttackPoint=rst['maxattack'], _attackPointType = float(rst['attackmod']) , _minHealthPoint= rst['hp'], _maxHealthPoint= rst['maxhp'] , _healthPointType=float(rst['hpmod']), _minHealPoint=rst['recovery'], _maxHealPoint=rst['maxrecovery'], _healPointType=float(rst['recoverymod']), _exp = rst['exp'], _expType = rst['exptype'])
			'''
			추후 추가해야 할 부분들 
			self._skill = _skill;			#
			self._LeaderSKill = _LeaderSKill;	#
			self._AwakeSkill = _AwakeSkill;		#
			self._prevEvolution = _prevEvolution;	#
			self._nextEvolution = _nextEvolution;	#
			'''
			url  = "http://m.inven.co.kr/site/pad/monster.php?code=%d"%id_num
			u = urllib.urlopen(url);
			c = u.read()
			u.close()
			m._cost = get_charactor_cost(c);
			attr = get_charactor_attr(c);
			if len(attr) == 1:
				m._mainAttribute = attr[0]
			elif len(attr) == 2:
				m._mainAttribute = attr[0]
				m._subAttribute = attr[1]
			types = get_charactor_type(c);
			if len(types) == 1:
				m._mainType = types[0]
			elif len(types) == 2:
				m._mainType = types[0]
				m._subType = types[1]
			m._imageUrl = get_charactor_icon_url(c);
			
			return m
		except Exception as e:
			print "Not find (%d) monster"%id_num
			print 'Error - ', e
			return None;

	def showData(self):
		print "id:",self._no
		print "name: ",self._name
		print "cost: ", self._cost
		print "exp: ", self._exp
		print "attribute: ",self._mainAttribute, self._subAttribute
		print "type: ", self._mainType, self._subType

	# 해당 lv에 몬스터의 hp, attack, recovery 를 구한다.
	def get_monster_status(self,lv,HPplusEgg=0,AttackPlusEgg=0,RecoveryPlusEgg=0):
		if lv > self._maxLevel:
			lv = self._maxLevel
		calc = lambda minVal,maxVal,level,maxLevel,mod:int(round(float(minVal)  + (float(maxVal) - float(minVal))*pow((float(level) - 1) / (float(maxLevel) - 1) , float(mod))))
		hp = calc(self._minHealthPoint, self._maxHealthPoint, lv, self._maxLevel, self._healthPointType) + HPplusEgg*10
		attack = calc(self._minAttackPoint, self._maxAttackPoint, lv, self._maxLevel, self._attackPointType) + AttackPlusEgg*5
		recovery = calc(self._minHealPoint, self._maxHealPoint, lv, self._maxLevel, self._healPointType) + RecoveryPlusEgg*3
		return hp, attack, recovery





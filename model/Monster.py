#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re


_no = re.compile(r"""<div class="no">No. ([^<]+)</div>""");
_name = re.compile(r"""<div class="name">([^<]+)</div>""")
_icon = re.compile(r"""<img class="imgicon" src="([^"]+)" /></div>""")
_cost = re.compile(r"""<div class="cost"><dl><dt>[^<]+</dt><dd>([^<]+)</dd>""")
_exp = re.compile(r"""<div class="exp"><dl><dt>[^<]+</dt><dd style="width: 92px;"><span style="float:left;">([^<]+)</span> """);
_status= re.compile(r"""<div class="block stateInfo">([^@]{3,5000}?)</div>""");
_attr= re.compile(r"""fonticon_attr_([\d_]+).png""");
_type=re.compile(r"""fonticon/fonticon_type_([\d_]+).png""");
_skill = re.compile(r"""<div class="block skillInfo">([^@]+)<div class="block awakenInfo">""");
_awakeSkill = re.compile(r"""<div class="block awakenInfo">([^@]{3,5000}?)</div>""");

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
		return int(rst[0])
	else:
		raise Exception("ERROR")

def get_charactor_status(uni_c):
	# return Max_Lv, min_hp, max_hp, min_attack, max_attack, min_heal, max_heal
	com = re.compile(_status);
	rst = com.findall(uni_c)

	if len(rst) != 0:
		#require get data from HTML Table
		print rst[0]
		
	else:
		raise Exception("ERROR")


class Monster(object):
	_no = 0
	_name = "None"
	_maxLevel = 0
	_attackPointList = []
	_healPointList = []
	_healthPointList = []
	_mainType = 0
	_subType = 0
	_skill = 0
	_LeaderSKill = 0
	_AwakeSkill = 0
	_prevEvolution = 0
	_nextEvolution = 0
	_imageUrl = ""

	# c is euc-kr string !
	def get_charactor_info_from_string(self, c):
		# All String Save the UTF-8
		uni_c = unicode(c,'euc-kr').encode('utf-8')
		#print get_charactor_num(uni_c), get_charactor_name(uni_c), get_charactor_icon_url(uni_c), get_charactor_cost(uni_c), get_charactor_exp(uni_c)
		get_charactor_status(uni_c)


	def get_charactor_info_from_file(self, _path):
		# All String Save the UTF-8
		f = open(_path)
		c = f.read()
		f.close()
		return self.get_charactor_info_from_string(c);


	def get_charactor_info_from_url(self, id_num):
		# get Monster Data from inven
		url  = "http://m.inven.co.kr/site/pad/monster.php?code=%d"%id_num
		u = urllib.urlopen(url);
		c = u.read()
		u.close()
		return self.get_charactor_info_from_string(c);


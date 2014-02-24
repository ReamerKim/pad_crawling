#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

import model.Monster
import controller.MonsterController
import _mysql

if __name__ == "__main__":
	#m = model.Monster.Monster();
	#m = model.Monster.Monster.get_charactor_info_from_url(102);
	#m.showData();
	
	#m.showData()
	db=_mysql.connect(host="localhost",user="root", passwd="admin", db="pad")

	# insert Monster Data
	for i in range(1,1100):
		m = model.Monster.Monster.get_charactor_info_from_json(i);
		if m != None:
			controller.MonsterController.moster_insert_data(db, m);
	#for i in range(1,300,3):
	#	m.get_charactor_info_from_url(i);
	#m.get_charactor_info_from_url(151);
	raw_input();	

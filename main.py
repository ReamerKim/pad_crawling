#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time 

import model.Monster
import controller.MonsterController
import _mysql

if __name__ == "__main__":
	#m = model.Monster.Monster();
	#m = model.Monster.Monster.get_charactor_info_from_url(102);
	#m.showData();
	#m = model.Monster.Monster.get_charactor_info_from_json(891);
	#m.showData();

	#m.showData()
	db=_mysql.connect(host="localhost",user="root", passwd="root", db="pad")
	db.set_character_set("utf8")

	# insert Monster Data
	for i in range(1,1100):
		m = model.Monster.Monster.get_charactor_info_from_json(i);
		if m != None:
			controller.MonsterController.moster_insert_data(db, m);
			if i%100 == 99:
				time.sleep(1);
	#for i in range(1,300,3):
	#	m.get_charactor_info_from_url(i);
	#m.get_charactor_info_from_url(151);
	raw_input();	

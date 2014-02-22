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
	m = model.Monster.Monster.get_charactor_info_from_json(891);
	m.showData()
	controller.MonsterController.moster_insert_data(m);
	#for i in range(1,300,3):
	#	m.get_charactor_info_from_url(i);
	#m.get_charactor_info_from_url(151);
	raw_input();	

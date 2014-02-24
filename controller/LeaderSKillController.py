#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import _mysql

def leader_skill_insert_data(db, leader_skill):
	#db=_mysql.connect(host="localhost",user="root", passwd="admin", db="pad")
	query = r"""INSERT INTO `pad`.`monstor` (`no`, `name`, `cost`, `exp`, `maxLevel`, `expType`, `maxLevel`, `minAttackPoint`, `maxAttackPoint`, `attackPointType`, `minHealthPoint`, `maxHealthPoint`, `healthPointType`, `minHealPoint`, `maxHealPoint`, `healPointType`, `mainAttribute`, `subAttribute`,	`mainType`,	`subType`, 'imageUrl') VALUES ('%d', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d', '%f', '%d', '%d', '%f', `%d`, `%d`,`%d`, `%d`, `%s`); """%(mon._no, mon._name, mon._exp, mon._expType, mon._maxLevel, mon._expType, mon._maxLevel, mon._minAttackPoint, mon._maxAttackPoint, mon._attackPointType, mon._minHealthPoint, mon._maxHealthPoint, mon._healthPointType, mon._minHealPoint, mon._maxHealPoint, mon._healPointType,	mon._mainAttribute,	mon._subAttribute, mon._mainType, mon._subType, mon._imageUrl)
	print query

	#db.query(query)


def leader_skill_create_table(db):
	query = '''CREATE TABLE `leader_skill` (
	`no` INT(10) UNSIGNED NOT NULL,					#unique data
	`name` CHAR(50) NOT NULL COLLATE 'utf8_bin',	
	`turn` INT(10) UNSIGNED NOT NULL,					#unique data
	`desc` CHAR(100) NOT NULL COLLATE 'utf8_bin',	
	`subdesc` CHAR(100) NOT NULL COLLATE 'utf8_bin',	
	`monsterlist` CHAR(200) NOT NULL COLLATE 'utf8_bin',	
	`monsternum` INT(10) UNSIGNED NOT NULL,


	INDEX `no` (`no`)
)
COMMENT='no'
COLLATE='utf8_bin'
ENGINE=InnoDB;'''
	#db=_mysql.connect(host="localhost",user="root", passwd="admin", db="pad")
	db.query(query)

#moster_create_table();

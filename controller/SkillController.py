#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import _mysql

def moster_insert_data(mon):
	db=_mysql.connect(host="localhost",user="root", passwd="admin", db="pad")
	query = r"""INSERT INTO `pad`.`monstor` (`no`, `name`, `cost`, `exp`, `maxLevel`, `expType`, `maxLevel`, `minAttackPoint`, `maxAttackPoint`, `attackPointType`, `minHealthPoint`, `maxHealthPoint`, `healthPointType`, `minHealPoint`, `maxHealPoint`, `healPointType`, `mainAttribute`, `subAttribute`,	`mainType`,	`subType`, 'imageUrl') VALUES ('%d', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d', '%f', '%d', '%d', '%f', `%d`, `%d`,`%d`, `%d`, `%s`); """%(mon._no, mon._name, mon._exp, mon._expType, mon._maxLevel, mon._expType, mon._maxLevel, mon._minAttackPoint, mon._maxAttackPoint, mon._attackPointType, mon._minHealthPoint, mon._maxHealthPoint, mon._healthPointType, mon._minHealPoint, mon._maxHealPoint, mon._healPointType,	mon._mainAttribute,	mon._subAttribute, mon._mainType, mon._subType, mon._imageUrl)
	print query

	#db.query(query)

def moster_create_table():
	query = '''CREATE TABLE `monster` (
	`no` INT(10) UNSIGNED NOT NULL,
	`name` CHAR(30) NOT NULL COLLATE 'utf8_bin',
	`cost` INT(10) UNSIGNED NOT NULL,
	`exp` INT(10) UNSIGNED NOT NULL,
	`expType` INT(10) UNSIGNED NOT NULL,
	`maxLevel` INT(10) UNSIGNED NOT NULL,

	`minAttackPoint` INT(10) UNSIGNED NOT NULL,
	`maxAttackPoint` INT(10) UNSIGNED NOT NULL,
	`attackPointType` FLOAT(10) UNSIGNED NOT NULL,

	`minHealthPoint` INT(10) UNSIGNED NOT NULL,
	`maxHealthPoint` INT(10) UNSIGNED NOT NULL,
	`healthPointType` FLOAT(10) UNSIGNED NOT NULL,

	`minHealPoint` INT(10) UNSIGNED NOT NULL,
	`maxHealPoint` INT(10) UNSIGNED NOT NULL,
	`healPointType` FLOAT(10) UNSIGNED NOT NULL,

	`mainAttribute` INT(10) UNSIGNED NOT NULL,
	`subAttribute` INT(10) UNSIGNED NOT NULL,
	`mainType` INT(10) UNSIGNED NOT NULL,
	`subType` INT(10) UNSIGNED NOT NULL,
	`skill` INT(10) UNSIGNED NOT NULL,
	`leaderSkill` INT(10) UNSIGNED NOT NULL,
	`awakeSkillList` INT(10) UNSIGNED NOT NULL,
	`prevEvolution` INT(10) UNSIGNED NOT NULL,
	`nextEvolution` INT(10) UNSIGNED NOT NULL,
	`imageUrl` CHAR(80) NOT NULL COLLATE 'utf8_bin',
	INDEX `no` (`no`)
)
COMMENT='no'
COLLATE='utf8_bin'
ENGINE=InnoDB;'''
	db=_mysql.connect(host="localhost",user="root", passwd="admin", db="pad")
	db.query(query)

#moster_create_table();

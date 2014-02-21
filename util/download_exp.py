import os
import requests
import json

def getStat(level, minHp, maxHp, mod):
        level = float(level)
        return round(minHp  + (maxHp - minHp)*pow((level - 1) / (99 - 1) , mod))


def getMonsterData(mon_num):
        data = { 'code': '%d'%mon_num, 'mode': '2' }
        url = r"""http://m.inven.co.kr/site/pad/monster_info.ajax.php"""
        r = requests.post(url,data=data)
        t = r.text
        rst = json.loads(t)
        return rst

print getMonsterData(30000)



        



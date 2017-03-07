# -*- coding: utf8 -*-
import datetime
#版本号
VERSION = 0.7
#程序启动时间
STARTTIME = datetime.datetime.now()
#调试文件名
debugname = "debug.txt"
#贴吧十大：强制程序启动时更新十大消息4
TIEBA_UPDATE_FORCE = 0
#记录用户ID文件名
recordname = "record.txt"
#贴吧十大：对普通用户开放百大吗
TIEBA_TOP100_TONONVIP = 1
#漂流瓶文件
floaterdbname = "floater_pool.txt"


#邮件模块设置
mail_host="mail.xxxx"  #设置服务器
mail_user="xxxxxxxx@xxx"    #用户名
mail_pass="xxxxxxxx"   #口令 
var = {}
var["TIEBA_UPDATE_TO"] = ""
var['TIEBA_SHIDA'] = []
var['TIEBA_SHIDA_UPDATE'] = ""
var['TIEBA_UPDATETIME'] = "18-00"

def set_value(svar,value):
	var[svar] = value

def get_value(svar):
	try:
		return var[svar]
	except:
		return None
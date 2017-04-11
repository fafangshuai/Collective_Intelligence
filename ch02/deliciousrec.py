# coding=utf-8
import pdb
from pydelicious import get_popular,get_userposts,get_urlposts

def initializeUserDict(tag,count=5):
	user_dict={}
	# pdb.set_trace()
	# 获取前count个最受欢迎的链接张贴记录
	for p1 in get_popular(tag=tag)[0:count]:
		# 查找所有张贴该链接的用户
		for p2 in get_urlposts(p1['href']):
			user=p2['user']
			user_dict[user]={}
	return user_dict


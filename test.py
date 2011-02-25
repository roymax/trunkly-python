#!/usr/bin/env python
# encoding: utf-8
from trunkly import Trunkly
import hashlib

TRUNK_KEY='your api key' 

if __name__ == '__main__':
	t = Trunkly(TRUNK_KEY) 
	
	# print 'check /api/v1/user/'
	# data = t.user()          
	# # print 'name %s' % data['username']    
	# for k, v in data.iteritems():
	# 	print '%s = %s' % (k,v )    
	# 
	# print 'check /api/v1/user/id/&ltuid>/'
	# #a user object for specified user ID 
	# user = t.user_id__uid(parameters={'uid':data['uid']},method='GET') 
	# for k, v in user.iteritems():
	# 	print '%s = %s' % (k,v )
	# 
	# print 'check /api/v1/user/followers/'	
	# followings = t.get_user_followers()
	# for k, v in followings.iteritems():
	# 	print '%s = %s' % (k,v )      
	# 	                             
	# print 'check /api/v1/link/'
	# link = t.post_link(parameters={
	# 	'url': 'http://blog.roynotes.com',
	# 	'title': 'roy的博客'
	# })
	# for k, v in link.iteritems():
	# 	print '%s = %s' % (k,v )       
		                               
	# print 'check /api/v1/api_key/'
	# username = raw_input('Username: ').strip() 
	# password = raw_input('Password: ').strip() 
	# apikey = t.get_api_key(username=username,password=password)
	# for k, v in apikey.iteritems():
	# 	print '%s = %s' % (k,v )   
	
	url='http://www.nytimes.com/2011/01/02/opinion/02sun2.html?_r=2&emc=tnt&tntemail1=y' 
	#hashlib.md5(url).hexdigest()
	#urlhash = '4c649790a138927eb482d1889ca4f720'
	site = t.get_link(parameters={'url': url})
	for k, v in site.iteritems():
		print '%s = %s' % (k,v )       
	

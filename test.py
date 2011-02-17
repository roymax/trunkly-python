#!/usr/bin/env python
# encoding: utf-8
from trunkly import Trunkly

TRUNK_KEY='5229-4bdad3ab-650d-4f6d-9e8e-8912cb841d76' 

if __name__ == '__main__':
	t = Trunkly(TRUNK_KEY) 

	print 'check /api/v1/user/'
	data = t.user()          
	# print 'name %s' % data['username']    
	for k, v in data.iteritems():
		print '%s = %s' % (k,v )    
	
	print 'check /api/v1/user/id/&ltuid>/'
	#a user object for specified user ID 
	user = t.user_id__uid(parameters={'uid':data['uid']},method='GET') 
	for k, v in user.iteritems():
		print '%s = %s' % (k,v )
	
	print 'check /api/v1/user/followers/'	
	followings = t.get_user_followers()
	for k, v in followings.iteritems():
		print '%s = %s' % (k,v )      
		                             
	print 'check /api/v1/link/'
	link = t.post_link(parameters={
		'url': 'http://blog.roynotes.com',
		'title': 'roy的博客'
	})
	for k, v in link.iteritems():
		print '%s = %s' % (k,v )      
		
	print 'check /api/v1/api_key/'
	username = raw_input('Username: ').strip() 
	password = raw_input('Password: ').strip() 
	apikey = t.get_api_key(username=username,password=password)
	for k, v in apikey.iteritems():
		print '%s = %s' % (k,v )
	
	
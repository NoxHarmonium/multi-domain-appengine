#
# Main Handler File
#

# Python imports
import os
import webapp2
from webapp2_extras import routes
from google.appengine.ext.webapp import template
import mimetypes
import logging
import time
from datetime import date
from datetime import timedelta

# User code imports
import utils

# Constants
subpath 	  =	'html' 
cache-control =	'Public, max-age=31536000'
expire-length =	timedelta(days=365)


class MainHandler(webapp2.RequestHandler):
	def get (self,path):
		# Initialise the mime type utility
		if not(mimetypes.inited):
			mimetypes.init()			
		
		# No path defaults to home page
		if path is None or path == '/' or path == '':
			path = 'index.html'
		
		# Get the file location on the server
		path = os.path.join(os.path.dirname (__file__), self.request.route.name,subpath, path)
		
		# Set response headers
		self.response.headers['Content-Type'] = mimetypes.guess_type(path)[0];
		self.response.headers['Cache-Control'] = cache-control;
		self.response.headers['Expires'] = formatDate(date.today() + expire-length)
		
		lastUpdateTime = None
		
		# If there is an 'If-Modified-Since' header, use it to see if the 
		# the file has changed since the client last downloaded it.
		try:					
			lastUpdateTime = self.request.headers['If-Modified-Since'];
		except:
			pass		
		if not (lastUpdateTime is None or lastUpdateTime == ''):
			lastUpdateTime = parseDate(lastUpdateTime)
			fileModTime = os.stat(path).st_mtime
			if lastUpdateTime < fileModTime:
				# Status code 304 means the file hasn't changed (send no data)
				self.response.set_status(304)			
			
		else:
			# Read the server file
			out = open(path,'rb').read()
			
			# Write the server file out to the client
			self.response.out.write (out)



app = webapp2.WSGIApplication([
	routes.DomainRoute('www.exampledomain1.com', [
		webapp2.Route('/<path:.*?>', handler=MainHandler,  name='www.exampledomain1.com'),
	]),
	routes.DomainRoute('www.exampledomain2.com', [
		webapp2.Route('/<path:.*?>', handler=MainHandler, name='www.exampledomain2.com'),
	]),
	# localhost defaults to first domain
	routes.DomainRoute('localhost', [
		webapp2.Route('/<path:.*?>', handler=MainHandler, name='www.exampledomain1.com'),
	])
		
], debug=True)	
		

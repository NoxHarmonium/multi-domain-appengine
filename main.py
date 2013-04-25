#
# Host Statuc
#
import os
import webapp2
from webapp2_extras import routes
from google.appengine.ext.webapp import template
import mimetypes
import logging
import time
from datetime import date
from datetime import timedelta

def parseDate(date):
	return datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
def formatDate(date):
	return date.strftime("%a, %d %b %Y %H:%M:%S %Z")

class MainHandler(webapp2.RequestHandler):
	def get (self,path):
		# Initialise the mime type utility
		if not(mimetypes.inited):
			mimetypes.init()
			
		
		# No path defaults to home page
		if path is None or path == '/' or path == '':
			path = 'index.html'
		
		# Get the file location on the server
		path = os.path.join(os.path.dirname (__file__), self.request.route.name,"html", path)
		
		# Set response headers
		self.response.headers['Content-Type'] = mimetypes.guess_type(path)[0];
		self.response.headers['Cache-Control'] = 'Public, max-age=31536000';
		self.response.headers['Expires'] = formatDate(date.today() + timedelta(days=365))
		
		lastUpdateTime = None
		
		try:		
			lastUpdateTime = self.request.headers['If-Modified-Since'];
		except:
			pass
		
		if not (lastUpdateTime is None or lastUpdateTime == ''):
			lastUpdateTime = parseDate(lastUpdateTime)
			fileModTime = os.stat(path).st_mtime
			if lastUpdateTime < fileModTime:
				self.response.set_status(304)
		
		else:
			# Read the server file
			out = open(path,'rb').read()
			
			# Write the server file out to the client
			self.response.out.write (out)



app = webapp2.WSGIApplication([
	routes.DomainRoute('www.noxharmonium.com', [
		webapp2.Route('/<path:.*?>', handler=MainHandler,  name='www.noxharmonium.com'),
	]),
	routes.DomainRoute('www.seandawson.info', [
		webapp2.Route('/<path:.*?>', handler=MainHandler, name='www.seandawson.info'),
	]),
	routes.DomainRoute('localhost', [
		webapp2.Route('/<path:.*?>', handler=MainHandler, name='www.seandawson.info'),
	])
		
], debug=True)	
		

#
# Simple utility functions for use
# by App Engine apps.
#

def parseDate(date):
	return datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
	
def formatDate(date):
	return date.strftime("%a, %d %b %Y %H:%M:%S %Z")
multi-domain-appengine
======================

Template for building a multi domain web host on the Google App Engine platform.
-------------------------------------------------------------------------------

All the magic happens in the route entries inside app.yaml. For example:

	routes.DomainRoute('<domain name>', [
		webapp2.Route('/<path:.*?>', handler=MainHandler,  name='<root directory>')
	])

Simply replace '<domain name>' with the name of the domain you wish to catch and set '<root directory>' to the root directory of the matching website. 

Make sure that you add your domain to your Google account by going to 'Application Settings' in the App Engine dashboard and clicking 'Add Domain'. Also make sure that you point your DNS entries to Google's servers by adding a CNAME entry to "ghs.googlehosted.com"


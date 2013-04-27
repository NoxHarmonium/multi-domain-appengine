multi-domain-appengine
======================

### Template for hosting multiple domains on a single Google App Engine instance.

All the magic happens in the route entries inside app.yaml. For example:

	routes.DomainRoute('<domain name>', [
		webapp2.Route('/<path:.*?>', handler=MainHandler,  name='<root directory>')
	])

Simply replace '&lt;domain name&gt;' with the name of the domain you wish to catch and set '&lt;root directory&gt;' to the root directory of the matching website. 

Make sure that you add your domain to your Google account by going to 'Application Settings' in the App Engine dashboard and clicking 'Add Domain'. Also make sure that you point your DNS entries to Google's servers by adding a CNAME entry to "ghs.googlehosted.com".

Also, as the files are not being served through the App Engine 'static' handler which is designed to serve static files but actually through your application, I recommend a caching proxy such as CloudFlare so that your server gets less hammered.


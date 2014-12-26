__author__ = 'syedaali'

'''
12/24/2014

This program is a demonstration of the Google Cloud Platform Python Library
Specifically, it uses the Compute Python Library.
The program connects to Google Compute Engine using the API and  lists
the instances in a given project.

Requirements: You need to download from GCP the secret key for your service
account, and name the file p12.p12. Keep the file in the same directory as this program.

Change the items in the section 'User replaceable items'.

How to run this program: python gce_api.py
'''

'''
We need to import 3 different modules, one to connect via HTTP to the API,
the other to server->server authentication without a browser, and lastly to
build the request
'''

import httplib2
from oauth2client.client import SignedJwtAssertionCredentials
from apiclient.discovery import build

# User replaceable items
PROJECT_ID = 'replace with your project-id'
DEFAULT_ZONE = 'replace with a GCE zone here'
client_email = 'replace with an email from GCP Service Account OAuth'
# End user replaceable items

API_VERSION = 'v1'
GCE_URL = 'https://www.googleapis.com/compute/%s/projects/' % (API_VERSION)

#download P12 file from API & Auth->Credentials
with open("p12.p12") as f:
    private_key = f.read()

#you can change the URL for compute to be for different services
credentials = SignedJwtAssertionCredentials(client_email, private_key,
                                            'https://www.googleapis.com'
                                            '/auth/compute')

#create a new http object
http = httplib2.Http()

#authorize this object
auth_http = credentials.authorize(http)

gce_service = build('compute', API_VERSION)
project_url = '%s%s' % (GCE_URL, PROJECT_ID)

#build the request for instances, don't send it yet
request = gce_service.instances().list(
    project=PROJECT_ID, filter=None, zone=DEFAULT_ZONE)

#this is the meat of the code, requesting the instances
response = request.execute(http=auth_http)

#now print the instances
if response and 'items' in response:
    instances = response['items']
    for instance in instances:
        print instance['name']
else:
    print 'No instances to list.'

__author__ = 'syedaali'

'''
This is a sample program that shows you how to connection to GCP using
Apache libcloud.
'''

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

Driver = get_driver(Provider.GCE)

#replace email with service account email
#replace private-key-filename with private key filename
#replace region with GCP region
#replace project with GCP project name
gce = Driver('email', 'private-key-filename',
             datacenter='region',
             project='project')


sizes = gce.list_sizes()
images = gce.list_images()

print images



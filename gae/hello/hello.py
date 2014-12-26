__author__ = 'syedaali'

'''
This program is a demonstration of Google App Engine.
It uses webapp2 framework to print "Hello Google!'.

How to use this program:
  Download the Google Python SDK, including the dev app server
  Run 'dev_appserver.py hello'. Hello should be the directory that contains hello.py and app.yaml
  Following that in you browser visit http://localhost:8080
'''

import webapp2

MAIN_PAGE = 'Hello Google!'

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(MAIN_PAGE)

application = webapp2.WSGIApplication([
  ('/',MainPage),
  ], debug=True)
